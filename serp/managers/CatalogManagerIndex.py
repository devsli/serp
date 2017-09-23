from .ManagerIndexBase import ManagerIndexBase
from .CatalogManager import CatalogManager

class CatalogManagerIndex(ManagerIndexBase):
    typ = 'cat'
    manager = CatalogManager
