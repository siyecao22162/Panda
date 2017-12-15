#-*- coding: utf-8 -*-

from oscar.apps.shipping import methods
from decimal import Decimal as D
from oscar.core import prices


class StandardLunch(methods.Base):
    code = 'standard lunch'
    name = 'A MIDI DANS 3 JOURS'

    charge_per_order = D('3.00')
    threshold = D('14.99')

    description = "Livraison à midi dans 3 jours; Téléphone: +33 07 84 92 06 66"

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
    name = 'A SOIR DANS 3 JOURS'

    charge_per_order = D('3.00')
    threshold = D('14.99')

    description = "Livraison à soir dans 3 jours; Téléphone: +33 07 84 92 06 66"

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
