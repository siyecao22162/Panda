
from django.shortcuts import render

def index(request):
    # depricated
    return render(request, 'home/index.html')

"for testing. will delete"
"""
CommunicationEventType = get_model('customer', 'CommunicationEventType')
commtype_code = 'NEWS'
context = {'something_else': 'Some more context.'}

try:
    event_type = CommunicationEventType.objects.get(code=commtype_code)
except CommunicationEventType.DoesNotExist:
    messages = CommunicationEventType.objects.get_and_render(commtype_code, context)
else:
    messages = event_type.get_messages(context)

dispatch = Dispatcher()
dispatch.send_email_messages('nkannielai@gmail.com', messages)
"""