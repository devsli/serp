from serp.exc import ItemNotFoundException
from serp.utils import parse_table_name

class ManagerBase(object):
    def __init__(self, erp, tablename:str):
        self.erp = erp
        self.tablename = tablename
        self.typ, self.name, self.ext = parse_table_name(tablename)
        self.human_name = format_system_name(self.name)

    def __repr__(self):
        return "<%s \"%s\">" % (self.__class__.__name__, self.human_name, )

    def __len__(self):
        c = self.erp.db.cursor()
        c.execute('SELECT COUNT(*) FROM \'{}\';'.format(self.tablename))
        return c.fetchone()[0]

    def __getitem__(self, id:int):
        return self.get_by_id(id)

    def get_by_id(self, id:int):
        c = self.erp.db.cursor()
        c.execute('SELECT * FROM \'{}\' WHERE rowid = ?;'.format(self.tablename), (id, ))
        data = c.fetchone()
        if data is None:
            raise ItemNotFoundException({
                "message": "Item not found",
                "section": self,
                "id": id
            })

        entity = self.entity()
        entity.load(c.fetchone())
        return entity

def format_system_name(name:str):
    return name.capitalize().replace('_', ' ')
