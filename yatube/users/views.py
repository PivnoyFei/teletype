from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.core.mail import send_mail

from .forms import CreationForm, ProfileForm, UserEditForm, SocialForm


class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy('posts:index')
    template_name = 'users/signup.html'


@login_required
def profile_edit(request, username):
    if request.method == 'POST':
        user_form = UserEditForm(
            instance=request.user, data=request.POST
        )
        profile_form = ProfileForm(
            instance=request.user.profile,
            data=request.POST,
            files=request.FILES
        )
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect("posts:profile", request.user.username)
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
        context = {"user_form": user_form,
                   "profile_form": profile_form}
        return render(request, 'posts/profile_edit.html', context)


@login_required
def profile_social_edit(request, username):
    if request.method == 'POST':
        social_form = SocialForm(
            instance=request.user.profile,
            data=request.POST,
            files=request.FILES
        )
        if social_form.is_valid():
            social_form.save()
            return redirect("posts:profile", request.user.username)
    else:
        social_form = SocialForm(instance=request.user.profile)
        context = {"is_edit": True,
                   "social_form": social_form}
        return render(request, 'posts/profile_edit.html', context)


# send_mail(
#    'Subject here',
#    'Here is the message.',
 #   'from@example.com',
 #   ['to@example.com'],
 #   fail_silently=False,
#)
