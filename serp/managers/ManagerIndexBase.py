from serp.utils import join_table_name, fetch_first_column, parse_table_name

class ManagerIndexBase(object):
    typ = None
    manager = None

    def __init__(self, erp):
        self.erp = erp

    def __getitem__(self, name:str):
        if not name.startswith(self.typ):
            name = join_table_name(self.typ, name)
        return self.manager(self.erp, name)

    def all(self):
        return [self[name] for name in self.list_tables(self.typ)
                if parse_table_name(name)[2] == None]

    def list_tables(self, ext = None):
        query = "SELECT name FROM sqlite_master WHERE type='table'"

        if ext is not None:
            query += " AND name LIKE '{}.%'".format(ext);

        query += ';'
        cursor = self.erp.execute(query)
        return fetch_first_column(cursor.fetchall())

    def list_inner(self, name):
        query = """
        SELECT name
        FROM sqlite_master
        WHERE type='table' AND name LIKE ? || '.' || ? || '.%';
        """
        cursor = self.erp.db.execute(query, (self.typ, name))
        return fetch_first_column(cursor.fetchall())

    def _create(self, name, fields=None, tables=None, ext=None):
        fields = fields or {}
        tables = tables or []
        fullname = join_table_name(self.typ, name, ext)

        fields = ', '.join(["%s %s" % (k, v) for k, v in fields.items()])
        query = 'CREATE TABLE \'{}\' ({})'.format(fullname, fields)

        self.erp.db.execute(query)

    def remove(self, tablename):
        fullname = join_table_name(self.typ, tablename)
        query = 'DROP TABLE IF EXISTS \'{}\';'.format(fullname)
        self.erp.db.execute(query)
        self.remove_inner(tablename)

    def remove_inner(self, tablename):
        for innername in self.list_inner(tablename):
            self.erp.db.execute('DROP TABLE \'{}\';'.format(innername))

