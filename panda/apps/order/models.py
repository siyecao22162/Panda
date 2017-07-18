from oscar.apps.address.abstract_models import AbstractShippingAddress

class ShippingAddress(AbstractShippingAddress):
    # don't know why direct overwrite phone_number is not working. Just for django abstract class?
    AbstractShippingAddress._meta.get_field('phone_number').blank = False

    # Add "GEMALTO 13600 LA CIOTAT" as default address to suit PRE-OPENING cases. TODO: maybe all France later?
    AbstractShippingAddress._meta.get_field('postcode').default = "13600"
    AbstractShippingAddress._meta.get_field('line1').default = "GEMALTO"
    AbstractShippingAddress._meta.get_field('line4').default = "LA CIOTAT"


# Need to keep this to avoid oscar app get migrate first
from oscar.apps.order.models import *