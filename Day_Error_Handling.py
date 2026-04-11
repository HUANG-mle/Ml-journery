LEARNING JOURNAL — DAY 11
=========================

Date           : 11-04-2026
Study duration : 45 minutes
Main topic     : Error Handling (try/except)

1. Concepts I learned today
-----------------------------
- try → attempt to run this code
- except → backup if the code fails
- ValueError → error when converting wrong data type
- ZeroDivisionError → error when dividing by zero
- Multiple except → handle different errors separately

2. New things I discovered
---------------------------
- Without try/except, program crashes with red error
- With try/except, program catches the error and responds friendly
- Can stack multiple except blocks for specific errors

3. Code I wrote today
----------------------
try:
    angka1 = int(input("masukan angka pertama: "))
    angka2 = int(input("masukan angka kedua: "))
    print(angka1 / angka2)
except ZeroDivisionError:
    print("gak bisa bagi angka 0")
except ValueError:
    print("itu bukan angka")
except:
    print("ada error lain!")

4. Errors I found & how I fixed them
--------------------------------------
The except block only caught general errors. To handle 
specific errors, I added ZeroDivisionError for dividing 
by zero and ValueError for invalid input type.

5. Things I still don't understand
------------------------------------
None

6. My understanding score today (1-10)
----------------------------------------
8.5 / 10


======================================
JURNAL BELAJAR — DAY 11
======================================

Tanggal        :  11-04-2025
Durasi belajar : 45 menit 
Materi utama   : Error Handling (try/except)

1. Konsep yang gw pelajari hari ini
------------------------------------
- try    → coba jalanin kode ini
- except → backup kalau gagal
- ValueError → error konversi tipe data yang salah
- ZeroDivisionError → error bagi dengan angka 0
- Multiple except → handle error yang berbeda secara terpisah

2. Hal baru yang gw tau
------------------------
- Tanpa try/except, program crash dengan error merah
- Dengan try/except, program nangkep error dan kasih respon friendly
- Bisa tumpuk beberapa except buat error yang spesifik

3. Kode yang gw tulis hari ini
-------------------------------
try:
    angka1 = int(input("masukan angka pertama: "))
    angka2 = int(input("masukan angka kedua: "))
    print(angka1 / angka2)
except ZeroDivisionError:
    print("gak bisa bagi angka 0")
except ValueError:
    print("itu bukan angka")
except:
    print("ada error lain!")

4. Error yang gw temuin & cara gw fixnya
-----------------------------------------
Except nya cuma nangkep error umum. Biar bisa handle 
error spesifik, gw tambahin ZeroDivisionError buat 
bagi angka 0 dan ValueError buat input yang salah tipe.

5. Yang masih bikin gw bingung
-------------------------------
Tidak ada

6. Skor pemahaman gw hari ini (1-10)
--------------------------------------
8.5 / 10
