from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy, reverse
from .forms import SignUpForm
from django.views import generic
from django.http import HttpResponseRedirect , HttpResponsePermanentRedirect 
from django.utils import timezone
from django.contrib.auth.decorators import login_required

# Create your views here.



# Create your views here.
class SignUpView(generic.CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
   

def SignUpForm(request):
    form_class = SignUpForm
    print("hellooooooooooooooooooooo")
    # success_url = reverse_lazy('login')
    # template_name = 'registration/signup.html'
    # context ={
    #     "my_signup":form_class
    # }
    return render(request, "registration/signup.html", {})
    
    
    