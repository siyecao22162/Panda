from oscar.apps.shipping import methods
from decimal import Decimal as D
from oscar.core import prices


class StandardLunch(methods.Base):
    code = 'standard lunch'
    name = 'Recupez sur Marché'

    charge_per_order = D('0.00')
    threshold = D('2.00')

    description = "Mardi et Dimanche au Marché de La Ciotat;&emsp; Vendredi au Marché de Ceyrest"

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
    threshold = D('15.00')

    description = "18h ~ 20h;&emsp; Gratuite (total >= 14.99€)"

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
