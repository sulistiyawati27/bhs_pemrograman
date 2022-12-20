import matplotlib.pyplot as plt

labels = ['Karyawan', 'Guru', 'Tukang Kebon', 'Pedagang']
quantity = [3, 10, 12, 15]
colors = ['yellowgreen', 'red', 'lightskyblue', 'lightcoral']

plt.title('Daftar Pekerjaan Orang Tua Siswa Kelas X')
plt.pie(quantity, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=90)

plt.axis('equal')
plt.show()

