from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView
from django.utils.translation import ugettext_lazy as _

from .forms import ContactForm
from django.core.mail import send_mail
from django.template.loader import get_template
from django.template import Context
from django.conf import settings


class HomePageView(FormView):
    template_name = 'homepage/home.html'
    page_title = _('Home Page')
    active_tab = 'Home Page'
    form_class = ContactForm
    success_url = reverse_lazy('message_sent')

    def form_valid(self, form):
        name = form.cleaned_data['name']
        place = form.cleaned_data['place']
        email = form.cleaned_data['email']
        phone = form.cleaned_data['phone']
        message = form.cleaned_data['message']

        msg = get_template('homepage/email.txt').render(Context({
            'name': name,
            'place': place,
            'phone': phone,
            'email': email,
            'message': message
        }))

        recipients = [settings.EMAIL_HOST_USER]
        send_mail('You got a message from user',
                  msg, settings.EMAIL_HOST_USER,
                  recipients)
        return super(HomePageView, self).form_valid(form)


class PromotionPageView(TemplateView):
    template_name = 'homepage/promotion.html'
    page_title = _('Promotion Page')
    active_tab = 'Promotion Page'


class MsgSendView(TemplateView):
    template_name = 'homepage/msg_sent.html'
    page_title = _('Thanks Page')
    active_tab = 'Thanks Page'

