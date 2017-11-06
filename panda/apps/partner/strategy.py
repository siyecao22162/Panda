from decimal import Decimal as D

from oscar.apps.partner import strategy, prices

TAX_RATE_FR = D('0.2')


class Selector(strategy.Selector):
    """
    Custom selector to return a FR-specific strategy that charges VAT
    """

    def strategy(self, request=None, user=None, **kwargs):
        return FRStrategy(request)


class FrenchFixedRateTax(strategy.FixedRateTax):
    """
    Customize tax rate
    """
    rate = TAX_RATE_FR


class FRStrategy(
        strategy.UseFirstStockRecord,
        strategy.StockRequired,
        FrenchFixedRateTax,
        strategy.Structured):
    """
    Typical FR strategy for physical goods.
    - There's only one warehouse/partner so we use the first and only stockrecord
    - Enforce stock level.  Don't allow purchases when we don't have stock.
    - Charge FR VAT on prices.  Assume everything is standard-rated.
    """