ogrenciler = {
    'Ahmet YILMAZ': [85, 90, 78],
    'Mehmet DEMİR': [92, 88, 76],
    'Ayşe KAYA': [78, 89, 95],
    'Zeynep ÇELİK': [65, 70, 80],
    'Ali KARA': [50, 60, 55],
    'Fatma YILDIZ': [88, 85, 90],
    'Murat AYDIN': [72, 68, 74],
    'Elif AKSOY': [95, 90, 88],
    'Hakan ÖZTÜRK': [45, 50, 55],
    'Canan TAŞ': [80, 75, 82]
}

#Her öğrencinin ortalaması notlarının yanına eklendi
for isim, notlar in ogrenciler.items():
    ortalama = round(sum(notlar) / len(notlar),2)
    ogrenciler[isim] = {
        'notlar': notlar,
        'ortalama': ortalama
    }

#En yüksek ortalamayı bulma
ogrenci_listesi = list(ogrenciler.items())
en_yuksek_ogrenci = ogrenci_listesi[0]
for ogrenci in ogrenci_listesi[1:]:
    if ogrenci[1]['ortalama'] > en_yuksek_ogrenci[1]['ortalama']:
        en_yuksek_ogrenci = ogrenci

en_yuksek_isim = en_yuksek_ogrenci[0]
en_yuksek_ortalama = en_yuksek_ogrenci[1]['ortalama']
print(f"En yüksek ortalaması olan öğrenci: {en_yuksek_isim}")
print(f"En yüksek ortalama: {en_yuksek_ortalama}")

#Her öğrencinin adını soyadından ayırıp ayrı bir tuple saklayıp bir listeye ekleyin
ad_soyad_listesi = []
for isim in ogrenciler.keys():
    ad, soyad = isim.split()
    ad_soyad_listesi.append((ad, soyad))
print(ad_soyad_listesi)

#İsimleri alfabetik sıraya göre sıralayın ve sıralanmış listeyi ekrana yazdırın.
alfabetik_sira = sorted(ogrenciler.keys())
print(alfabetik_sira)

#GNO'su 70'in altında olan öğrencileri bir kümede (kümede) tutun.
ogrenciler = {
    'Ahmet YILMAZ': [85, 90, 78],
    'Mehmet DEMİR': [92, 88, 76],
    'Ayşe KAYA': [78, 89, 95],
    'Zeynep ÇELİK': [65, 70, 80],
    'Ali KARA': [50, 60, 55],
    'Fatma YILDIZ': [88, 85, 90],
    'Murat AYDIN': [72, 68, 74],
    'Elif AKSOY': [95, 90, 88],
    'Hakan ÖZTÜRK': [45, 50, 55],
    'Canan TAŞ': [80, 75, 82]
}

ortalama = {}
for isim, notlar in ogrenciler.items():
    ort = sum(notlar)/len(notlar)
    ortalama[isim] = round(ort, 2)

alti_70 = set()
for isim, ort in ortalama.items():
    if ort < 70:
        alti_70.add(isim)
print("70'in altındaki öğrenciler kümesi: ", alti_70)
