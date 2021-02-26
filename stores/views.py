from django.shortcuts import render

# Create your views here.

from profiles.models import User,ads

from django.views.generic.edit import CreateView,UpdateView



class upload_ads(CreateView):
    model=ads

    template_name='upload-ads.html'

    fields=['image','title','price','category','available']

    success_url="/profiles/dashboard"


    def get_queryset(self):
        
        qs=super().get_queryset()
        return qs.filter(user=self.request.user)
  

    def form_valid(self,form):
        user=User.objects.get(username=self.request.user)
        form.instance.user=user
        return super().form_valid(form)

class edit_ads(UpdateView):

    model=ads

    template_name='edit-ads.html'

    success_url="/profiles/dashboard"

    fields=['image','title','price','category','available']


    def get_queryset(self):
        
        qs=super().get_queryset()
        return qs.filter(user=self.request.user)

        

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'ads_id':self.kwargs['pk']}) 
        return context

def delete_account(request):

    User.objects.filter(username=request.user).delete()

    return redirect("/")