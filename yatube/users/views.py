from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import CustomUserCreationForm, ProfileForm, SocialForm


class SingUPView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('posts:index')
    template_name = 'users/signup.html'


@login_required
def profile_edit(request, username):
    if request.method == 'POST':
        user_form = ProfileForm(
            instance=request.user,
            data=request.POST,
            files=request.FILES
        )
        if user_form.is_valid():
            user_form.save()
            return redirect("posts:profile", request.user.username)
    else:
        user_form = ProfileForm(instance=request.user)
        context = {"user_form": user_form}
        return render(request, 'posts/profile_edit.html', context)


@login_required
def profile_social_edit(request, username):
    if request.method == 'POST':
        social_form = SocialForm(
            instance=request.user,
            data=request.POST,
            files=request.FILES
        )
        if social_form.is_valid():
            social_form.save()
            return redirect("posts:profile", request.user.username)
    else:
        social_form = SocialForm(instance=request.user)
        context = {"is_edit": True,
                   "social_form": social_form}
        return render(request, 'posts/profile_edit.html', context)
