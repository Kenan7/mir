from django.shortcuts import render
from django.views.generic import RedirectView
from django.views.generic.edit import FormView
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.conf import settings
from django.contrib import messages

from core.forms import ContactForm
from core.models import ContactRequest


class HomePageView(RedirectView):
    url = '/blog/articles/'


class ContactView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact')

    def form_valid(self, form):
        ContactRequest.objects.create(
            name=form.cleaned_data['name'],
            email=form.cleaned_data['email'],
            message=form.cleaned_data['content']
        )

        # Delegate this to a Celery task for production
        send_mail(
            subject=f"Contact Request from {form.cleaned_data['name']}",
            message=form.cleaned_data['content'],
            from_email=settings.CONTACT_FORM_SENDER,
            recipient_list=settings.CONTACT_FORM_RECIPIENTS,
            fail_silently=False,
        )

        messages.success(self.request, 'Your message was sent successfully!')

        return super().form_valid(form)
