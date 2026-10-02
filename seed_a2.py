"""Builds a2.db for Assignment 2. Run: python seed_a2.py"""
import sqlite3, os, random

random.seed(20260922)
if os.path.exists("a2.db"):
    os.remove("a2.db")

conn = sqlite3.connect("a2.db")
c = conn.cursor()
c.execute("CREATE TABLE users  (id INTEGER, name TEXT, city TEXT, age INTEGER)")
c.execute("CREATE TABLE orders (id INTEGER, user_id INTEGER, total REAL, status TEXT)")

names = ["Alice","Brandon","Chen","Dara","Elena","Femi","Grace","Hassan","Iris",
         "Jamal","Kiara","Luis","Maya","Noah","Olga","Priya","Quinn","Rosa",
         "Samir","Tessa","Umar","Vera","Wes","Xiomara","Yusuf"]
cities = ["Raleigh","Greenville","Durham","Charlotte","Wilmington"]
users = [(i+1, n, random.choice(cities), random.randint(19, 64)) for i, n in enumerate(names)]
c.executemany("INSERT INTO users VALUES (?,?,?,?)", users)

statuses = ["shipped","pending","cancelled","delivered"]
orders = []
oid = 1
for uid in range(1, len(names)+1):
    for _ in range(random.randint(0, 4)):          # some users have no orders
        orders.append((oid, uid, round(random.uniform(8.0, 480.0), 2),
                       random.choice(statuses)))
        oid += 1
c.executemany("INSERT INTO orders VALUES (?,?,?,?)", orders)

conn.commit()
print("users:", len(users), " orders:", len(orders))
for row in c.execute("SELECT * FROM users LIMIT 4"): print(row)
for row in c.execute("SELECT * FROM orders LIMIT 4"): print(row)
conn.close()
