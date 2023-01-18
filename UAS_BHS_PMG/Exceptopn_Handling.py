try:
    # kode yang mungkin menyebabkan exception
    result = 10 / 0
except ZeroDivisionError:
    # kode yang akan dijalankan jika terjadi exception ZeroDivisionError
    print("Tidak bisa melakukan pembagian dengan nol.")
