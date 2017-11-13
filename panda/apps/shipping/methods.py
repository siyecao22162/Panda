from oscar.apps.shipping import methods
from decimal import Decimal as D
from oscar.core import prices


class StandardLunch(methods.Base):
    code = 'standard lunch'
    name = 'Recupez sur Marché'

    charge_per_order = D('0.00')
    threshold = D('2.00')

    description = "Mardi et Dimanche au Marché de La Ciotat; +33 07 84 92 06 66"

    def calculate(self, basket):
        # Free for orderHs over some threshold
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
    code = 'standard dinner'
    name = 'DEMAIN SOIR'

    charge_per_order = D('3.00')
    threshold = D('18.99')

    description = "18h ~ 20h demain soir;&emsp; Gratuite (total >= 18.99€); +33 07 84 92 06 66"

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
