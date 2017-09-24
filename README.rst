Stupid ERP
~~~~~~~~~~

*Not for production use*

Before clone
~~~~~~~~~~~~

To properly save/load SQLite3 database you first need to tune your git::

  cat <<'EOF'> ~/bin/sqlite3.clean
  #!/bin/sh
  DB=$(mktemp)
  cat - > $DB
  sqlite3 $DB .dump
  rm $DB
  EOF
  chmod +x ~/bin/sqlite3.clean
  
  cat <<'EOF'> ~/bin/sqlite3.smudge
  #!/bin/sh
  DB=$(mktemp)
  cat - | sqlite3 $DB
  cat $DB
  rm $DB
  EOF
  chmod +x ~/bin/sqlite3.smudge
  
  git config --global filter.sqlite.clean sqlite3.clean
  git config --global filter.sqlite.smudge sqlite3.smudge

Table structure
~~~~~~~~~~~~~~~

Document
========

::

   doc.DOCUMENT_NAME
   * rowid (implicit)
   * date
   * comment
   * author
   * owner
   * active
   * <custom fields>

Document inner table
====================

::

   doc.DOCUMENT_NAME.TABLE_NAME
   * doc_id
   * lineno
   * <custom fields>

Catalog
=======

::

   cat.CATALOG_NAME
   * rowid (implicit)
   * name
   * comment
   * <custom fields>

Accumulation register
=====================

::

   acc.ACCUMULATE_REGISTER
   * doctype (ie. 'doc.DOCUMENT_TYPE')
   * docref (document rowid)
   * date
   * <metrics>
   * <values>

Information register
====================

::

   inf.INFORMATION_REGISTER
   * doctype
   * docref
   * date
   * <metrics>
   * <values>
