from django.shortcuts import render,redirect

from django.urls import reverse_lazy

# Create your views here.

from django.views.generic import ListView

from django.views.generic.edit import UpdateView,FormView

from django.contrib.auth.views import PasswordChangeView,PasswordChangeDoneView

from django.contrib.auth.forms import PasswordChangeForm

from .models import ads,User

from .forms import eidit_profile_form

from django.db.models  import Q


class dashboard(ListView):

    template_name='dashboard.html'

    model=ads

    paginate_by=5


    def get_queryset(self):
         qs=super().get_queryset()
         return qs.filter(user=self.request.user).order_by('-created_at')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'u':User.objects.get(username=self.request.user)}) 
        return context
    
    



class Edit_Profile(UpdateView):

    model=User

    template_name="user-profile.html"
    
    form_class=eidit_profile_form

    def get_success_url(self):
        #i can't use redirect here
        return reverse_lazy("Edit_Profile",args=[self.request.user.id])

    def get_queryset(self):
         qs=super().get_queryset()
         return qs.filter(username=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["person"] = User.objects.get(username=self.request.user)
        context.update({'FORM':PasswordChangeForm(self.request.user)})
        return context
    

class change_password(PasswordChangeView):
    template_name="user-profile.html"

    form_class=PasswordChangeForm

    success_url=reverse_lazy('change_password_done')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["person"] = User.objects.get(username=self.request.user)
        context["form"] = eidit_profile_form(initial={'username':self.request.user,'email':self.request.user.email
        ,'last_name':self.request.user.last_name,'first_name':self.request.user.first_name,'phone':self.request.user.phone})
        print(PasswordChangeForm(self.request.user))
        context.update({'FORM':PasswordChangeForm(self.request.user)})
        return context
    


class change_password_done(PasswordChangeView):

    template_name="change_password_done.html"


def delete_avatar(request,pk):


    User.objects.filter(Q(id=pk)&Q(username=request.user)).update(avatar=None)

    return redirect("Edit_Profile",pk)

def delete_ads(request,pk):

    ads.objects.filter(Q(id=pk)&Q(user=request.user)).delete()

    return redirect('dashboard')









    

