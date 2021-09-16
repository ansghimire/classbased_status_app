from django.urls import reverse_lazy
from django.views.generic import CreateView,ListView
from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from status.models import UserStatus

from .forms import UserModelForm
from django.conf import global_settings

User = get_user_model()


class RegisterCreateView(CreateView):
    model = User
    form_class = UserModelForm
    template_name = 'accounts/register.html'
    success_url = 'accounts/login'
    context_object_name = 'form'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object = self.object.set_password(self.object.password)
        return super().form_valid(form)


@method_decorator(login_required(), name="dispatch")
class Profile(ListView):
    template_name = 'accounts/profile.html'
    context_object_name = 'datas'

    def get_queryset(self):
        return UserStatus.objects.filter(user=self.request.user)
        # return UserStatus.objects.all()


class Login(LoginView):
    template_name = 'accounts/login.html'


class Logout(LogoutView):
    next_page = reverse_lazy('login')
