from oscar.apps.shipping import methods
from decimal import Decimal as D
from oscar.core import prices


class StandardLunch(methods.Base):
    code = 'standard lunch'
    name = 'Lunch Time Delivery'

    charge_per_order = D('3')
    threshold = D('15.00')

    description = "Charge of delivery: 3€ (total < 15€); FREE (total >= 15€)"

    def calculate(self, basket):
        # Free for orders over some threshold
        if basket.total_incl_tax > self.threshold:
            return prices.Price(
                currency=basket.currency,
                excl_tax=D('0.00'),
                incl_tax=D('0.00'))

        # Simple method - charge 0.99 per item
        total = self.charge_per_order

        return prices.Price(
            currency=basket.currency,
            excl_tax=total,
            incl_tax=total)

class StandardDinner(methods.Base):
    code = 'standar ddinner'
    name = 'Diner Time Delivery'

    charge_per_order = D('3')
    threshold = D('15.00')

    description = "Charge of delivery: 3€ (total < 15€); FREE (total >= 15€)"

    def calculate(self, basket):
        # Free for orders over some threshold
        if basket.total_incl_tax > self.threshold:
            return prices.Price(
                currency=basket.currency,
                excl_tax=D('0.00'),
                incl_tax=D('0.00'))

        # Simple method - charge 0.99 per item
        total = self.charge_per_order

        return prices.Price(
            currency=basket.currency,
            excl_tax=total,
            incl_tax=total)
