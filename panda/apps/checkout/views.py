from oscar.apps.checkout import views
from oscar.apps.payment.models import Source
from oscar.apps.payment.models import SourceType

class PaymentDetailsView(views.PaymentDetailsView):
    def handle_payment(self, order_number, total, **kwargs):
        source_type, is_created = SourceType.objects.get_or_create(name='Cash on Delivery')
        source = Source(
            source_type=source_type,
            currency=total.currency,
            amount_allocated=total.incl_tax,
            amount_debited=total.incl_tax
        )
        self.add_payment_source(source)