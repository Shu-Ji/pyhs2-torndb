# coding: u8

from __future__ import unicode_literals, print_function

from tornhivedb import Connection


def test_query(db):
    sql = """
    SELECT cate_id_tail, platform, dt
    FROM  gjdb.dw_m_log_pv_format
    WHERE dt='20170827'
    LIMIT 3
    """
    rows = db.query(sql)
    for row in rows:
        print(row)


def test_get(db):
    # get() should only return one row, else will raise an error
    sql = """
    SELECT cate_id_tail, platform, dt
    FROM  gjdb.dw_m_log_pv_format
    WHERE dt='20170829'
    LIMIT 1
    """
    row = db.get(sql)
    print(row)
    # row is an dict-like object
    print(row.dt)
    print(row['dt'])


def test_execute(db):
    # `UPDATE` or `DELETE` is DANGER!!!
    # sql = """
    # UPDATE xxx
    # """
    # db.execute(sql)
    pass


def main():
    host = '127.0.0.1'
    db = Connection(db_host=host, port=10000, user='my_hadoop_user',
            database='mydb', authMechanism='PLAIN')

    test_query(db)
    test_get(db)
    test_execute(db)


if __name__ == '__main__':
    main()
