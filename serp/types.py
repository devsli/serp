import logging
logger = logging.getLogger(__name__)

__all__ = ["Int", "Datetime", "String", "Table", "CatRef", "DocRef"]

Int = "int"
Datetime = "datetime"
String = "varchar"

class Table(dict):
    pass

# TODO: references
class Ref(object):
    def __init__(self, prefix, target_name):
        self.target = "%s.%s" % (prefix, target_name)

    def __str__(self):
        logger.warn("References are not implemented yet, referenced: %s",
                    self.target)
        return Int

class CatRef(Ref):
    def __init__(self, catname):
        super().__init__('cat', catname)

class DocRef(Ref):
    def __init__(self, docname):
        super().__init__('doc', docname)
