
from django.views.generic import TemplateView
from django.utils.translation import ugettext_lazy as _
from .forms import ContactForm
from django.shortcuts import render

from django.core.mail import send_mail
from django.template.loader import get_template
from django.template import Context

class HomePageView(TemplateView):
    template_name = 'homepage/home.html'
    page_title = _('Home Page')
    active_tab = 'Home Page'


class PromotionPageView(TemplateView):
    template_name = 'homepage/promotion.html'
    page_title = _('Promotion Page')
    active_tab = 'Promotion Page'


def msg_sent(request):
    form = ContactForm(request.POST)

    if form.is_valid():
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
        print("Sending email" + msg)

        recipients = ['pandaannielai@gmail.com']
        send_mail('You got a message from user',
                  msg, email,
                  recipients)
        return render(request, 'homepage/msg_sent.html', {'form': form})
