from serp import *
from peewee import *

from serp.example.models.catalogs import Items, Stores
from serp.example.models.accumulators import ItemsInStores

__all__ = ["ItemLost", "ItemFound"]

class ItemLost(Document):
    __affects__ = (
        ItemsInStores
    )

    comment = CharField(null=True)
    store = ForeignKeyField(Stores)

    # print(Items)

    def _issue(self):
        return
        for row in self.items:
            print(row)
            yield ItemsInStores.change(
                store=self.store,
                item=row.item,
                amount=-row.amount
            )

ItemLost.table(
    "items",

    item = ForeignKeyField(Items),
    amount = IntegerField()
)

class ItemFound(ItemLost):
    def _issue(self):
        for row in self.items:
            ItemsInStores.change(
                store=self.store,
                item=row.item,
                amount=+row.amount
            )
