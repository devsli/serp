def parse_table_name(fullname:str):
    # returns [type, name, ext?] list
    parts = fullname.split('.')
    if len(parts) == 2:
        parts.append(None)
    return tuple(parts)

def join_table_name(typ, name, ext=None):
    result = '{}.{}'.format(typ, name)
    if ext is not None:
        result += '.' + ext
    return result

def fetch_first_column(fetch_result):
    return [x[0] for x in fetch_result]
