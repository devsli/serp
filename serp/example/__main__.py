from . import models

from .models.catalogs import *
from .models.documents import *

from serp import SERP, database
from peewee import SqliteDatabase

erp = SERP(SqliteDatabase("example.sqlite"))

erp.create_tables()
# database.create_tables([ItemLost])


newdoc = ItemLost()

newdoc.store = Stores.get_or_create(name="main")[0]

import ipdb; ipdb.set_trace()

newdoc.save()
newdoc.issue()
