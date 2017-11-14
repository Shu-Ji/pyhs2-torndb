# pyhs2-torndb

python hive client with pyhs2 which likes torndb


Used like [torndb](https://github.com/bdarnell/torndb) .

This project provides three methods: `db.query`, `db.get`, `db.execute`.

`db.query` and `db.get` are used like torndb.

Only `db.execute` will return None, while `torndb.execute` returns lastrowid.


封装一下 pyhs2，让其使用起来和 torndb 一样简单好用。

提供 db.query、db.get、db.execute 三个方法，用法和 torndb 完全一样。

query 和 get 返回值数据类型也完全一样; 惟一不同的是 execute 方法，torndb 中会返回 lastrowid，本文中返回 None
