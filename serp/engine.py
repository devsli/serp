import logging
import sqlite3
logger = logging.getLogger(__name__)

from . import managers

class SERP(object):
    def connect(self, path):
        self.db = sqlite3.connect(path)
        self.init()
        logger.info('Connected to {}'.format(path))

    def init(self):
        self.catalogs = managers.CatalogManagerIndex(self)
        self.documents = managers.DocumentManagerIndex(self)

    def execute(self, query, *args):
        c = self.db.cursor()
        c.execute(query, args)
        return c
