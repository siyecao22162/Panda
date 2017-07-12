from oscar.apps.address.abstract_models import AbstractShippingAddress

class ShippingAddress(AbstractShippingAddress):
    # don't know why direct overwrite phone_number is not working. Just for django abstract class?
    AbstractShippingAddress._meta.get_field('phone_number').blank = False

# Need to keep this to avoid oscar app get migrate first
from oscar.apps.order.models import *