from django.shortcuts import render
from django.views.generic import CreateView, TemplateView, ListView
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect

from .forms import SignUpForm
from .models import Shop
# Create your views here.


class SignupView(CreateView):
    form_class = SignUpForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('shopapp:login')


class LoginView(TemplateView):
    template_name = 'registration/login.html'

    def post(self, request, **kwargs):
        user = authenticate(email=request.POST.get('email', False), password=request.POST.get('password', False))
        print(user)
        if user:
            print('hey there ')
            login(request, user)
            return HttpResponseRedirect(reverse('shopapp:shops_list'))
        return render(request, self.template_name)


class LogoutView(TemplateView):
    template_name = 'registration/logout.html'

    def get(self, request, **kwargs):
        logout(request)
        return render(request, self.template_name)


class ShopsListView(ListView):
    model = Shop
