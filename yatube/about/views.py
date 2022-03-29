from .models import Contact
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
from .forms import ContactForm


class AboutAuthorView(TemplateView):
    success_url = reverse_lazy('posts:index')
    template_name = 'about/author.html'


class AboutTechView(TemplateView):
    success_url = reverse_lazy('posts:index')
    template_name = 'about/tech.html'


class ContactCreate(CreateView):
    model = Contact
    success_url = reverse_lazy('posts:index')
    form_class = ContactForm

    def form_valid(self, form):
        return super().form_valid(form)
