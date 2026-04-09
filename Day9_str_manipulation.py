JURNAL BELAJAR — DAY 9
======================

Tanggal        : 9 -04-2026
Durasi belajar : 60 menit
Materi utama   : String Manipulation

1. Konsep yang gw pelajari hari ini
------------------------------------
- .lower()  → ubah semua huruf jadi kecil
- .upper()  → ubah semua huruf jadi besar
- .replace() → ganti kata tertentu
- .strip()  → hapus spasi di ujung kiri & kanan
- .split()  → potong teks jadi list berdasarkan pemisah
- Method chaining → gabungin beberapa method sekaligus dalam satu baris

2. Hal baru yang gw tau
------------------------
- Method chaining: kalimat.lower().strip().split(",")
- .split() menghasilkan LIST — ini berhubungan langsung dengan
  tokenisasi di NLP nanti!

3. Kode yang gw tulis hari ini
-------------------------------
kalimat = input("Tulis kalimat lo: ")
hasil = kalimat.lower().strip().split(",")
print(hasil)

4. Error yang gw temuin & cara gw fixnya
-----------------------------------------
- .stripp() → typo, harusnya .strip()

5. Yang masih bikin gw bingung
fungsinya ke lmm ini gimana bro ah kira kir


6. Skor pemahaman gw hari ini (1-10)
-8,5/10


======================================
ENGLISH VERSION — DAY 9
======================================

Date           : 9-04-2026
Study duration : 60 minutes 
Main topic     : String Manipulation

1. Concepts I learned today
-----------------------------
- .lower()   → convert all letters to lowercase
- .upper()   → convert all letters to uppercase
- .replace() → replace a specific word
- .strip()   → remove whitespace at both edges
- .split()   → cut text into a list based on separator
- Method chaining → combine multiple methods in one line

2. New things I discovered
---------------------------
- Method chaining: kalimat.lower().strip().split(",")
- .split() returns a LIST — this directly connects to
  tokenization in NLP!

3. Code I wrote today
----------------------
kalimat = input("Write your sentence: ")
hasil = kalimat.lower().strip().split(",")
print(hasil)

4. Errors I found & how I fixed them
--------------------------------------
- .stripp() → typo, should be .strip()

5. Things I still don't understand
------------------------------------


6. My understanding score today (1-10)
8,5/10
