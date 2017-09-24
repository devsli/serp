from datetime import datetime

from peewee import *


database = Proxy()


def get_subclasses(cls):
    for subclass in cls.__subclasses__():
        yield from get_subclasses(subclass)
        yield subclass

def get_models():
    for i in [Document, Catalog, Accumulator, InnerTable]:
        yield from get_subclasses(i)


class SERP:
    def __init__(self, db):
        database.initialize(db)

    def create_tables(self):
        database.create_tables(get_models())



class BaseModel(Model):
    __type__ = ""

    class Meta:
        database = database

        def db_table_func(cls):
            prefix = cls.__type__
            name = cls.__qualname__.lower()
            return "%s.%s" % (prefix, name)


class _ModelWithTables(BaseModel):
    @classmethod
    def table(cls, name, **kwargs):
        name = "%s.%s" % (cls.__qualname__.lower(), name)
        inherits = (InnerTable,)

        kwargs["ref"] = ForeignKeyField(cls, related_name=name)
        kwargs["__type__"] = cls.__type__

        return type(name, inherits, kwargs)


class InnerTable(BaseModel):
    line_no = IntegerField()


class CatRef(ForeignKeyField):
    pass


class Document(_ModelWithTables):
    __type__ = "doc"

    date = DateTimeField(default=datetime.utcnow)
    issued = BooleanField(default=False)

    def issue(self):
        for i in self._issue():
            print(i)


class Catalog(_ModelWithTables):
    __type__ = "cat"
    name = CharField(unique=True)


class Accumulator(BaseModel):
    __type__ = "acc"
    @classmethod
    def change(cls, **kwargs):
        print(cls)


class AccVal(BaseModel):
    def __init__(self, typ):
        pass
