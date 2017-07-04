
from django.views.generic import TemplateView
from django.utils.translation import ugettext_lazy as _


class HomePageView(TemplateView):
    template_name = 'homepage/home.html'
    page_title = _('Home Page')
    active_tab = 'Home Page'


class PromotionPageView(TemplateView):
    template_name = 'homepage/promotion.html'
    page_title = _('Promotion Page')
    active_tab = 'Promotion Page'


