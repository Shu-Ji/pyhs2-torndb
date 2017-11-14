# coding: u8

import pyhs2
from pyhs2.error import Pyhs2Exception


class Row(dict):
    """A dict that allows for object-like property access syntax."""
    def __getattr__(self, name):
        try:
            return self[name]
        except KeyError:
            raise AttributeError(name)


class Connection(object):
    def __init__(self, db_host, user, database, port=10000,
            authMechanism="PLAIN"):
        """
        create connection to hive server2
        """

        self.conn = pyhs2.connect(host=db_host,
                port=port,
                authMechanism=authMechanism,
                user=user,
                database=database,
                )

    def query(self, sql):
        """Returns a row list for the given query and parameters."""
        with self.conn.cursor() as cursor:
            self._execute(cursor, sql)
            column_names = [i['columnName'] for i in cursor.getSchema()]
            return [Row(zip(column_names, row)) for row in cursor]

    def _execute(self, cursor, sql):
        try:
            return cursor.execute(sql)
        except Pyhs2Exception as e:
            self.close()
            raise(e)

    def get(self, sql):
        """Returns the (singular) row returned by the given query.
        If the query has no results, returns None.  If it has
        more than one result, raises an exception.
        """

        rows = self.query(sql)
        if not rows:
            return None
        elif len(rows) > 1:
            raise Exception("Multiple rows returned for get() query")
        else:
            return rows[0]

    def execute(self, sql):
        """Executes the given query, returning None."""

        with self.conn.cursor() as cursor:
            self._execute(cursor, sql)

    def close(self):
        if hasattr(self, 'conn'):
            self.conn.close()

    def __del__(self):
        self.close()
