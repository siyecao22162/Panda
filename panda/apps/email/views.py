import logging

from django.views.generic import TemplateView
from django.utils.translation import ugettext_lazy as _
from oscar.core.compat import get_user_model
from oscar.core.loading import get_model, get_class
from django.core.urlresolvers import reverse
from django import http

logger = logging.getLogger('email')
User = get_user_model()
CommunicationEventType = get_model('customer', 'CommunicationEventType')
Dispatcher = get_class('customer.utils', 'Dispatcher')


class BroadcastView(TemplateView):
    template_name = 'email/broadcast.html'
    page_title = _('Broadcast email')
    active_tab = 'Broadcast'

    def post(self, request, *args, **kwargs):
        communication_type_code = 'broadcast_email'
        context = {'something_else': 'Some more context.'}

        try:
            event_type = CommunicationEventType.objects.get(code=communication_type_code)
        except CommunicationEventType.DoesNotExist:
            messages = CommunicationEventType.objects.get_and_render(communication_type_code, context)
        else:
            messages = event_type.get_messages(context)

        dispatch = Dispatcher()
        users = User.objects.all()
        for user in users:
            if not user.is_staff:
                dispatch.send_user_email_messages(user, messages)

        return http.HttpResponseRedirect(reverse('broadcast'))
