LEARNING JOURNAL — DAY 3
==========================
Date : 1-04-2026
Study Duration :1 Hour
Main Topic :if else
1. Concepts I Learned Today
If, Else, and Elif statements.
2. New Insights
I learned that when setting ranges, I need to use both >= and <= operators to define boundaries clearly.
However, if the conditions are written in a specific order (from largest to smallest or vice versa), the logic can be more streamlined.
3. Code I Wrote Today
name = input("What's your name: ")
age  = int(input("How old are you: "))

if age <= 12:
    status = "Elementary School"
elif age >= 13 and age <= 15:
    status = "Junior High School"
elif age >= 16 and age <= 18:
    status = "Senior High School"
elif age >= 19:
    status = "Working/College"

print(f"Hello {name}, you are {age} years old and your status is {status}!")

4. Errors Found & How I Fixed Them
Issue: I initially struggled with displaying the status or age in the final
output because I was trying to use print inside each if and elif block incorrectly.
Solution: I fixed it by assigning the result to a variable called status inside 
the conditional blocks first, then using a single print statement at the end to display everything.
5. Current Lingering Doubts
None.
6. Understanding Score
7/10

JURNAL BELAJAR — DAY 3
======================

Tanggal        : 1-04-2026
Durasi belajar : 1 jam
Materi utama   : if else

1. Konsep yang gw pelajari hari ini
If else elif


2. Hal baru yang gw tau
Kalok mau bikin >= harus di kasih <=
Kecuali jika berurutan dari yang besar ke kecil 


3. Kode yang gw tulis hari ini

nama  = input("nam lo siapa : ")
umur  = int(input("umur lo berapa : "))
if umur <= 12 :
	status = "sd"
elif umur  >= 13 and umur <= 15:
	status = "smp"
elif umur >= 16 and umur <= 18 :
	status = "sma"
elif umur >= 19:
	status =  "kerja/kuliah"
print(f"Halo {nama} umur kamu {umur} kamu kelas {status}!")


4. Error yang gw temuin & cara gw fixnya

Yah itu pas mau nambahin variabel Elif Ama if nya ke print itu gak bisa muncul kelas nya atau usia nya 
Dan cara ngefix nya adalah tinggal ubah kata print di If dan  Elif jadi status 


5. Yang masih bikin gw bingung
Gak ada


6. Skor pemahaman gw hari ini (1-10)
7/10
