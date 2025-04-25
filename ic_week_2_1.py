# Öğrenci isimlerini ve notlarının girişi ve oratlama hesabı


# i=1
# ogrenciler = {} 
# while i<=10:
    
#     adi=str(input("Öğrenci adını giriniz:"))
#     final = float(input("Öğrenci final notunu giriniz:"))
#     vize = float(input("Öğrenci vize notunu giriniz:"))
#     notlar=[final, vize, (final + vize) / 2]
#     ogrenciler[adi]= [notlar]

#     i += 1
# print(ogrenciler)

students = {
    'Ahmet Yılmaz': [85, 90, 78],  # Midterm: 85, Final: 90, Oral: 78
    'Mehmet Demir': [92, 88, 76],  # Midterm: 92, Final: 88, Oral: 76
    'Ayşe Kaya': [78, 89, 95],    # Midterm: 78, Final: 89, Oral: 95
    'Zeynep Çelik': [65, 70, 80],  # Midterm: 65, Final: 70, Oral: 80
    'Ali Kara': [50, 60, 55],     # Midterm: 50, Final: 60, Oral: 55
    'Fatma Yıldız': [88, 85, 90],  # Midterm: 88, Final: 85, Oral: 90
    'Murat Aydın': [72, 68, 74],   # Midterm: 72, Final: 68, Oral: 74
    'Elif Aksoy': [95, 90, 88],   # Midterm: 95, Final: 90, Oral: 88
    'Hakan Öztürk': [45, 50, 55],  # Midterm: 45, Final: 50, Oral: 55
    'Canan Taş': [80, 75, 82]     # Midterm: 80, Final: 75, Oral: 82
}
en_yuksek_ort = max(students.items(), key=lambda x: x[1][2])
print(f"En yüksek ortalamaya sahip öğrenci: {en_yuksek_ort[0]} Ortalama: {en_yuksek_ort[1][2]}")

# Ad ve Soyad bilgilerini ayırma

students = {
    'Ahmet Yılmaz': [85, 90, 78],  # Midterm: 85, Final: 90, Oral: 78
    'Mehmet Demir': [92, 88, 76],  # Midterm: 92, Final: 88, Oral: 76
    'Ayşe Kaya': [78, 89, 95],    # Midterm: 78, Final: 89, Oral: 95
    'Zeynep Çelik': [65, 70, 80],  # Midterm: 65, Final: 70, Oral: 80
    'Ali Kara': [50, 60, 55],     # Midterm: 50, Final: 60, Oral: 55
    'Fatma Yıldız': [88, 85, 90],  # Midterm: 88, Final: 85, Oral: 90
    'Murat Aydın': [72, 68, 74],   # Midterm: 72, Final: 68, Oral: 74
    'Elif Aksoy': [95, 90, 88],   # Midterm: 95, Final: 90, Oral: 88
    'Hakan Öztürk': [45, 50, 55],  # Midterm: 45, Final: 50, Oral: 55
    'Canan Taş': [80, 75, 82]     # Midterm: 80, Final: 75, Oral: 82
}

ad_soyad_tuple = []
ad_soyad_tuple = tuple((ad_soyad.split()[0], ad_soyad.split()[1]) for ad_soyad in students.keys())
print(ad_soyad_tuple)
print(type(ad_soyad_tuple))
# İsme göre sıralama

students = {
    'Ahmet Yılmaz': [85, 90, 78],  # Midterm: 85, Final: 90, Oral: 78
    'Mehmet Demir': [92, 88, 76],  # Midterm: 92, Final: 88, Oral: 76
    'Ayşe Kaya': [78, 89, 95],    # Midterm: 78, Final: 89, Oral: 95
    'Zeynep Çelik': [65, 70, 80],  # Midterm: 65, Final: 70, Oral: 80
    'Ali Kara': [50, 60, 55],     # Midterm: 50, Final: 60, Oral: 55
    'Fatma Yıldız': [88, 85, 90],  # Midterm: 88, Final: 85, Oral: 90
    'Murat Aydın': [72, 68, 74],   # Midterm: 72, Final: 68, Oral: 74
    'Elif Aksoy': [95, 90, 88],   # Midterm: 95, Final: 90, Oral: 88
    'Hakan Öztürk': [45, 50, 55],  # Midterm: 45, Final: 50, Oral: 55
    'Canan Taş': [80, 75, 82]     # Midterm: 80, Final: 75, Oral: 82
}

ad_soyad_tuple = []
ad_soyad_tuple = tuple((ad_soyad.split()[0], ad_soyad.split()[1]) for ad_soyad in students.keys())
ad_soyad_sort = sorted(ad_soyad_tuple)
print(ad_soyad_sort)
# GNO ortalaması 70 altında olan öğrencileri bir listede toplama

students = {
    'Ahmet Yılmaz': [85, 90, 78],  # Midterm: 85, Final: 90, Oral: 78
    'Mehmet Demir': [92, 88, 76],  # Midterm: 92, Final: 88, Oral: 76
    'Ayşe Kaya': [78, 89, 95],    # Midterm: 78, Final: 89, Oral: 95
    'Zeynep Çelik': [65, 70, 80],  # Midterm: 65, Final: 70, Oral: 80
    'Ali Kara': [50, 60, 55],     # Midterm: 50, Final: 60, Oral: 55
    'Fatma Yıldız': [88, 85, 90],  # Midterm: 88, Final: 85, Oral: 90
    'Murat Aydın': [72, 68, 74],   # Midterm: 72, Final: 68, Oral: 74
    'Elif Aksoy': [95, 90, 88],   # Midterm: 95, Final: 90, Oral: 88
    'Hakan Öztürk': [45, 50, 55],  # Midterm: 45, Final: 50, Oral: 55
    'Canan Taş': [80, 75, 82]     # Midterm: 80, Final: 75, Oral: 82
}

gno_70 = []
for adsoyad, notlar in students.items():
    if notlar[2] < 70:
        gno_70.append((adsoyad, notlar[2]))
print(gno_70)

