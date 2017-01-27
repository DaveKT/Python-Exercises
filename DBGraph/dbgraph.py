#!/usr/local/bin/python3

import argparse
import sqlite3
import re


parser = argparse.ArgumentParser()
parser.add_argument("db", help="The name of the DB to connect to")
args=parser.parse_args()

conn = sqlite3.connect(args.db)
c = conn.cursor()

tables = []

for row in c.execute("""SELECT tbl_name FROM sqlite_master WHERE type = 'table'"""):
	tables.append(row)

print(tables)