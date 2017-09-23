import logging
logger = logging.getLogger(__name__)

from serp.utils import join_table_name
from serp.types import Table, Int, String, Datetime

from .ManagerIndexBase import ManagerIndexBase
from .DocumentManager import DocumentManager

class DocumentManagerIndex(ManagerIndexBase):
    typ = 'doc'
    manager = DocumentManager
    default_columns = dict(
        date    = Datetime,
        comment = String,
        author  = Int,
        owner   = Int,
        active  = Int
    )

    inner_default_columns = dict(
        doc_id = Int,
        lineno = Int
    )

    def create(self, name:str, **fields):
        logger.info("Creating the document: %s", name)

        tables     = dict([(k, v) for k, v in fields.items()
                           if type(v) is Table])
        own_fields = dict([(k, v) for k, v in fields.items()
                           if type(v) is not Table])

        columns = {}
        columns.update(self.default_columns)
        columns.update(own_fields)

        self._create(name, fields=columns)
        for tname, tfields in tables.items():
            self.create_inner(name, tname, tfields)


    def create_inner(self, name:str, ext:str, fields:dict=None):
        fields = fields or {}
        columns = {}

        columns.update(fields)
        columns.update(self.inner_default_columns)

        self._create(name, fields=columns, ext=ext)
