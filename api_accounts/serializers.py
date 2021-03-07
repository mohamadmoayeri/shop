from rest_framework import serializers

from profiles.models import User

from django.contrib import auth

from rest_framework.exceptions import AuthenticationFailed

from rest_framework_simplejwt.tokens import RefreshToken, TokenError



class register_serial(serializers.ModelSerializer):

    class Meta:

        model=User

        fields=['username','email','password']

        extra_kwargs={'password':{'write_only':True},
        }

    def validate(self,data):
        p2=self.context.get('p2')

        if data['password']!=p2:

            raise serializers.ValidationError("Password don't match")
    
        return data

    def create(self,validated_data):

        user=super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    


class login_serial(serializers.ModelSerializer):
    #email = serializers.EmailField(max_length=255, min_length=3,read_only=True)

    password = serializers.CharField( max_length=68, min_length=3, write_only=True)

    username = serializers.CharField(max_length=255, min_length=3, )

    tokens = serializers.SerializerMethodField()

    def get_tokens(self, obj):

        user = User.objects.get(username=obj['username'])

        return {
            'refresh': user.tokens()['refresh'],
            'access': user.tokens()['access']
        }

    class Meta:
        model = User
        fields = ['email', 'password', 'username', 'tokens']

    def validate(self, attrs):
        username = attrs.get('username', '')
        password = attrs.get('password', '')
        u= User.objects.filter(username=username)
        if u:
            user = auth.authenticate(username=username, password=password)
        elif u and User.objects.get(username=username).is_authenticated:
           raise AuthenticationFailed(detail=f'Please continue your login using {username}')

        elif u and  not u[0].is_active:
            raise AuthenticationFailed('Account disabled, contact admin')

        elif not u:
           raise AuthenticationFailed('Invalid credentials, try again ')

        
        #if not user.is_verified:
        #    raise AuthenticationFailed('Email is not verified')

        return attrs

        
  
class logout_serial(serializers.Serializer):
    refresh = serializers.CharField()

    default_error_message = {
        'bad_token': ('Token is expired or invalid')
    }

    def validate(self, attrs):
        print(attrs)
        self.token = attrs['refresh']
        return attrs

    def save(self, **kwargs):

        try:
            RefreshToken(self.token).blacklist()

        except TokenError:
            self.fail('bad_token')