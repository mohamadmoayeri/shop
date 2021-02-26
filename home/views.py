from django.shortcuts import render

# Create your views here.

from django.views.generic import TemplateView,ListView

from profiles.models import User,ads

from datetime import datetime



class home(TemplateView):

    def get(self,request):
        last_ads=ads.objects.values()
       


        context={
            'last_ads':last_ads
        }

        return render(request,'index.html',context)


class categories(ListView):

    template_name='category.html'

    model=ads

    def get_queryset(self):
        qs=super().get_queryset()
        category=self.kwargs['category']

        return qs.filter(category=category)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update ( {'categ':self.kwargs['category'],'date':datetime.now().date,
        'count':ads.objects.filter(category=self.kwargs['category']).count()})
        return context
    
    