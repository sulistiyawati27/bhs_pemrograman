import mysql.connector

# Koneksi ke database
cnx = mysql.connector.connect(user='username', password='password', host='hostname', database='nama_database')

# Membuat cursor
cursor = cnx.cursor()

# Menjalankan perintah SQL
cursor.execute("SELECT * FROM tabel_nama")

# Menampilkan hasil query
for (col1, col2) in cursor:
  print("{}, {}".format(col1, col2))

# Menutup koneksi
cursor.close()
cnx.close()

