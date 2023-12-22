from django.shortcuts import render, redirect
from .models import User
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from .forms import CustomUserCreationForm
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
# Create your views here.
n_cache = [never_cache,]

class HomeView(TemplateView):
    template_name = 'user/index.html'

@method_decorator(n_cache, name='dispatch')
class DasboardView(LoginRequiredMixin, TemplateView):
    template_name = 'user/dashboard.html'

class CustomLoginView(LoginView):
    template_name = 'user/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('dashboard')
    

class CustomRegistrationView(FormView):
    template_name = 'user/register.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        user = form.save()
        if user:
            login(self.request, user)
        return super().form_valid(form)
    
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('dashboard')
        return super(CustomRegistrationView, self).get(*args, **kwargs)
    
