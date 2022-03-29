from django.forms import ModelForm, Textarea
from .models import Contact
from captcha.fields import CaptchaField


class ContactForm(ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']
        labels = {
            "name": "Имя",
            "message": "Текст сообщения"
        }
        widgets = {
            'message': Textarea(
                attrs={
                    'placeholder': 'Напишите тут ваше сообщение'
                }
            )
        }