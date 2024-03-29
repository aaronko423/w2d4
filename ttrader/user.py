#! usr/bin/env python3

import sqlite3

DBNAME = "trade.db"
TABLENAME = "user_info"

class User:

    def __init__(self, **kwargs):
        self.pk = kwargs.get("pk")
        self.username = kwargs.get("username")
        self.password = kwargs.get("password")
        self.realname = kwargs.get("realname")
        self.balance = kwargs.get("balance", 0.0)
    
    def save(self):
        if self.pk is None:
            self._insert()
        else:
            self._update()

    def _insert(self):
        with sqlite3.connect(DBname) as conn:
            cur = conn.cursor()
            SQL = """
INSERT INTO user_info(username, password, realname, balance)
VALUES(?, ?, ?, ?);"""
            cur.execute(SQL, (self.username, self.password, self.realname, self.balance))
            self.pk = cur.lastrowid

    def _update(self):
        with sqlite3.connect(DBNAME) as conn:
            cur = conn.cursor()
            SQL = """
UPDATE user_info SET username=?, password=?, realname=?, balance=? WHERE pk=?;"""
            cur.execute(SQL, (self.username, self.password, self.realname, self.balance, self.pk))


    @classmethod
    def frompk(cls, pk):
        with sqlite3.connect(DBNAME) as conn:
            conn.rowfactory = sqlite3.Row
            cur = conn.cursor()
            SQL = """
SELECT * FROM user_info WHERE pk=?;"""
            cur.execute(SQL, (pk,))
            row = cur.fetchone()
            if not row:
                return None
            user = cls(**row)
            return user
