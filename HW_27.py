import mysql.connector as mysql

db = mysql.connect(
    host="localhost",
    user="root",
    passwd="Hn1930013@",
    database="nastya_test_db"
)

cursor = db.cursor()
#cursor.execute("CREATE TABLE orders (order_number INT(255), purch_amt FLOAT(6,2), ord_date DATE, customer_id INT(255), salesman_id INT(255))")
#cursor.execute("ALTER TABLE orders ADD COLUMN id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY FIRST")

# query = "INSERT INTO orders (order_number, purch_amt, ord_date, customer_id, salesman_id) VALUES (%s, %s, %s, %s, %s)"
# values = [
#     (70001, 150.5, "2012-10-05", 3005, 5002),
#     (70009, 270.65, "2012-09-10", 3001, 5005),
#     (70002, 65.26, "2012-10-05", 3002, 5001),
#     (70004, 110.5, "2012-08-17", 3009,5003),
#     (70007, 948.5, "2012-09-10", 3005, 5002),
#     (70005, 2400.6, "2012-07-27", 3007, 5001),
#     (70008, 5760, "2012-09-10", 3002, 5001),
#     (70010, 1983.43, "2012-10-10", 3004, 5006),
#     (70003, 2480.4, "2012-10-10", 3009, 5003),
#     (70012, 250.45, "2012-06-27", 3008, 5002),
#     (70011, 75.29, "2012-08-17", 3003, 5007),
#     (70013, 3045.6, "2012-04-25", 3002, 5001)
# ]
# cursor.executemany(query, values)
# db.commit()
# print(cursor.rowcount, "records inserted")

query = "SELECT order_number, purch_amt, ord_date FROM orders where salesman_id=5002"
cursor.execute(query)
print(cursor.fetchall())

query_2 = "SELECT DISTINCT salesman_id FROM orders"
cursor.execute(query_2)
print(cursor.fetchall())

query_3 = "SELECT ord_date, salesman_id, order_number, purch_amt FROM orders ORDER BY ord_date ASC"
cursor.execute(query_3)
print(cursor.fetchall())

query_4 = "SELECT * FROM orders WHERE order_number BETWEEN 70001 AND 70007"
cursor.execute(query_4)
print(cursor.fetchall())