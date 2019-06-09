#! usr/bin/env python3

import sqlite3
from ttrader import User
from schema import build_user

build_user()

mike = User(**{
    "pk": 2,
    "username": "mikebloom",
    "password": "password",
    "realname": "Mike Bloom",
    "balance": 10000.0
})

assert mike.password == "password"

mike.save()

user1 = User.frompk(1)

assert User1.username == "mikebloom"

mike.password = "12345"
mike.save() #saving password into his data

mikeagain = User.frompk(1) # loading mike again as we are updating his password

assert mikeagain.password == "12345"

print("tests passed")
