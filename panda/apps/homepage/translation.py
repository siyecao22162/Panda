from modeltranslation.translator import register, TranslationOptions
from oscar.apps.catalogue.models import Product
from modeltranslation.admin import TranslationAdmin


@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)
    required_languages = ('en-gb', 'fr')


class ProductAdmin(TranslationAdmin):
    pass

