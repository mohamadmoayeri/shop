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

    tokens = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['username', 'password','tokens']

    def get_tokens(self, obj):
        print(obj,10000000000000000000000000000000000000000000000000000000000000)
        user = User.objects.get(username=obj['username'])

        return {
            'refresh': user.tokens()['refresh'],
            'access': user.tokens()['access']
        }

    def validate(self, attrs):
        username = attrs.get('username', '')
        password = attrs.get('password', '')
        filtered_user_by_username = User.objects.filter(username=username)
        user = auth.authenticate(username=username, password=password)

        if filtered_user_by_username.exists() and filtered_user_by_username[0].auth_provider != 'username':
            raise AuthenticationFailed(
                detail='Please continue your login using ' + filtered_user_by_username[0].auth_provider)

        if not user:
            raise AuthenticationFailed('Invalid credentials, try again')
        if not user.is_active:
            raise AuthenticationFailed('Account disabled, contact admin')
        if not user.is_verified:
            raise AuthenticationFailed('Username is not verified')

        return {
            'username': user.username,
            'tokens': user.tokens
        }

        return super().validate(attrs)




    