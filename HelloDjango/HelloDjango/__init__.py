import pymysql
from django.db.backends.mysql.operations import DatabaseOperations


def my_last_executed_query(self, cursor, sql, params):
    query = getattr(cursor, '_executed', None)
    if query is not None:
        query = query.encode(errors='replace')
    return query


# 重写django的类方法
DatabaseOperations.last_executed_query = my_last_executed_query

# 重写pymysql的属性
pymysql.version_info = (1, 3, 13, "final", 0)

# 伪装
pymysql.install_as_MySQLdb()
