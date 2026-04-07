LEARNING JOURNAL — DAY 8
Date: April 7, 2026
Study Duration: 120 minutes
Main Material: Mini Project (Student Grades)
1. Concepts I Learned Today
How to combine multiple concepts into a single program, including variables, user input, dictionaries, basic mathematics, f-strings, integers, and if/elif/else logic.
2. New Things I Discovered
I realized that all the code I’ve been learning since Day 1 can actually be integrated into one cohesive program or script.
3. Code I Wrote Today
student = {
    "name": input("Student name: "),
    "math_score": int(input("Math score: ")),
    "lang_score": int(input("Language score: ")),
}

average = (student["math_score"] + student["lang_score"]) / 2

if average >= 90:
    grade = "A"
elif average >= 80:
    grade = "B"
elif average >= 70:
    grade = "C"
else:
    grade = "D"

print(f"Name: {student['name']}")
print(f"Average: {average}")
print(f"Grade: {grade}")

4. Errors Found & How I Fixed Them
When I tried to run the program, I realized it didn't show any results. I fixed it by ensuring there were print() statements at the end of the program to display the output.
5. Things That Still Confuse Me
None.
6. My Understanding Score Today (1-10)
9.5/10
Pro tip: Karena skor lo udah 9.5/10,


JURNAL BELAJAR — DAY 8
======================

Tanggal        : 7 - 4 - 2026
Durasi belajar : 120 minutes 
Materi utama   : minim project (nilai siswa)

1. Konsep yang gw pelajari hari ini
cara gabungin atau bikin yang di mana satu progam isinya variabel 
input dictionary matematika f string int if/Elif/else


2. Hal baru yang gw tau
 ternyata kode yang gw pelajarin dari day 1 semua nya bisa di
gabungin jadi satu progam atau code


3. Kode yang gw tulis hari ini

siswa = {
	"nama" : input("nama siswa: "),
	"nilai_mtk" : int(input("nilai matematika: ")),
	"nilai_bhs" : int(input("nilai bahasa: ")),
}
rata_rata = (siswa["nilai_mtk"] + siswa["nilai_bhs"]) /2
if rata_rata >= 90:
	predikat = "A"
elif rata_rata >= 80:
	predikat = "B"
elif rata_rata>= 70:
	predikat = "C"
else:
	predikat = "D"
print(f"Nama: {siswa['nama']}")
print(f"Rata-Rata: {rata_rata}")
print(f"nilai: {predikat}")


4. Error yang gw temuin & cara gw fixnya 
pas mau bikin atau jalanin progamnya eh ternyata fix nya harus 
ada print nya di akhir progam 


5. Yang masih bikin gw bingung
gak ada


6. Skor pemahaman gw hari ini (1-10)
9,5/10
