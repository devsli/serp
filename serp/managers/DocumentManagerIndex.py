import logging
logger = logging.getLogger(__name__)

from serp.utils import join_table_name
from serp.types import Table

from .ManagerIndexBase import ManagerIndexBase
from .DocumentManager import DocumentManager

class DocumentManagerIndex(ManagerIndexBase):
    typ = 'doc'
    manager = DocumentManager
    default_columns = {
        'date': 'datetime',
        'comment': 'varchar',
        'author': 'int',
        'owner': 'int',
        'active': 'int'
    }
    inner_default_columns = {
        'doc_id': 'int',
        'lineno': 'int'
    }

    def create(self, name, **fields):
        logger.info("Creating document: %s", name)
        tables     = dict([(k, v) for k, v in fields.items() if type(v) is Table])
        own_fields = dict([(k, v) for k, v in fields.items() if type(v) is not Table])

        columns = {}
        columns.update(self.default_columns)
        columns.update(own_fields)

        self._create(name, fields=columns)
        for tname, tfields in tables.items():
            self.create_inner(name, tname, tfields)


    def create_inner(self, name, ext, fields={}):
        columns = {}
        columns.update(fields)
        columns.update(self.inner_default_columns)

        self._create(
            name = name,
            ext = ext,
            fields = columns
        )
