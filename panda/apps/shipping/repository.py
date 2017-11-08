"""

Custimize oscar shipping repository
"""

from oscar.apps.shipping import repository
from . import methods as shipping_methods


class Repository(repository.Repository):
    methods = (shipping_methods.StandardDinner(), shipping_methods.StandardLunch())