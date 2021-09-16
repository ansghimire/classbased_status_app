from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import UserStatusModelForm
from .models import UserStatus


@method_decorator(login_required(), name="dispatch")
class StatusCreateView(CreateView):
    template_name = 'status/create.html'
    form_class = UserStatusModelForm
    success_url = reverse_lazy('profile')
    context_object_name = 'form'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


@method_decorator(login_required(), name="dispatch")
class StatusDeleteView(DeleteView):
    model = UserStatusModelForm.Meta.model
    success_url = reverse_lazy('profile')

    def get_queryset(self):
        return UserStatus.objects.filter(
            user=self.request.user
        )
    # passing from get to post
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


@method_decorator(login_required(), name="dispatch")
class StatusUpdateView(UpdateView):
    form_class = UserStatusModelForm
    template_name = 'status/update.html'
    context_object_name = 'form'
    success_url = reverse_lazy('profile')

    def get_queryset(self):
        return UserStatus.objects.filter(user=self.request.user)


