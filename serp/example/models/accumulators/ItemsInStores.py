from peewee import *
from serp import Accumulator, AccVal

from serp.example.models.catalogs import Items, Stores

class ItemsInStores(Accumulator):
    store = ForeignKeyField(Stores)
    item = ForeignKeyField(Items)

    amount = AccVal(IntegerField())
