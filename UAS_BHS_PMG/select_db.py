import mysql.connector

mydb = mysql.connector.connect(
  host="172.18.102.103",
  port=23306,
  user="root",
  password="p455w0rd",
  database="basis_data"
)

db = mydb.cursor()

db.execute("SELECT * FROM students")

res = db.fetchall()

for x in res:
  print(x)
  