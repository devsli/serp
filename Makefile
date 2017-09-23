.sql.sqlite:
	sqlite3 $@ < $<

.sqlite.sql:
	sqlite3 $< .dump > $@

.SUFFIXES: .sql .sqlite

