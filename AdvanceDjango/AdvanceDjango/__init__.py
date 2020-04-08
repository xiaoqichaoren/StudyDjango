import pymysql
from django.db.backends.mysql.operations import DatabaseOperations


def my_last_executed_query(self, cursor, sql, params):
    query = getattr(cursor, '_executed', None)
    if query is not None:
        query = query.encode(errors='replace')
    return query


DatabaseOperations.last_executed_query = my_last_executed_query
pymysql.version_info = (1, 3, 13, "final", 0)
pymysql.install_as_MySQLdb()
