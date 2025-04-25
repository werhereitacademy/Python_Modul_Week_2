students = {
    'Ahmet Yılmaz': [85, 90, 78],  # Midterm: 85, Final: 90, Oral: 78
    'Mehmet Demir': [92, 88, 76],  # Midterm: 92, Final: 88, Oral: 76
    'Ayşe Kaya': [78, 89, 95],    # Midterm: 78, Final: 89, Oral: 95
    'Zeynep Çelik': [65, 70, 80],  # Midterm: 65, Final: 70, Oral: 80
    'Ali Kara': [50, 60, 55],     # Midterm: 50, Final: 60, Oral: 55
    'Fatma Yıldız': [88, 85, 90],  # Midterm: 88, Final: 85, Oral: 90
    'Murat Aydın': [72, 68, 74],   # Midterm: 72, Final: 68, Oral: 74
    'Elif Aksoy': [95, 90, 88],    # Midterm: 95, Final: 90, Oral: 88
    'Hakan Öztürk': [45, 50, 55],  # Midterm: 45, Final: 50, Oral: 55
    'Canan Taş': [80, 75, 82]     # Midterm: 80, Final: 75, Oral: 82
}
yukseknot = 0
yuksekogrenci = ""
ads = []
soyads= []
alfabetik = []
zayif = []
for student, noot in students.items():
    mid,final,oral = noot
    ort= (mid * 0.3 + final * 0.5 + oral * 0.2)
    if ort > yukseknot:
        yukseknot = ort
        yuksekogrenci = student
    if ort < 70:
        zayif.append(student)
print("En yüksek notu alan öğrenci: ", yuksekogrenci)
for isim in students.keys():
    ad, soyad = isim.split()
    ads.append(ad)
    soyads.append(soyad)
print("Ogrenciler: ")
for isim in sorted(students.keys()):
    print(isim)
print("70 altı GPA ya sahip olan ogrenciler: ",zayif)
