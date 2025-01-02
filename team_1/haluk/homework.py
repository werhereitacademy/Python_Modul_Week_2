

   # Question1



students = {
    'Ahmet Yılmaz': [85, 90, 78],
    'Mehmet Demir': [92, 88, 76],
    'Ayşe Kaya': [78, 89, 95],
    'Zeynep Çelik': [65, 70, 80],
    'Ali Kara': [50, 60, 55],
    'Fatma Yıldız': [88, 85, 90],
    'Murat Aydın': [72, 68, 74],
    'Elif Aksoy': [95, 90, 88],
    'Hakan Öztürk': [45, 50, 55],
    'Canan Taş': [80, 75, 82]
}
print("\n1- Calculate each student's GPA and add it to the dictionary\n2- Find the student with the highest GPA and print it on the screen.\n3- Separate each student's name from their surname and store them in a separate tuple and add them to a list.\n4- Sort the names in alphabetical order and print the sorted list on the screen.\n5- Keep students with a GPA below 70 in a cluster (set).")
while True:
    secim = int(input("\nSeçiminizi giriniz: "))
    if secim == 1:
        for ogrenci in students:
            notlar = students[ogrenci]
            notlar.append(sum(notlar)/len(notlar))
        print(students)


    elif secim == 2:
        en_yuksek_ortalama = 0
        en_iyi_ogrenci = ""

        for ogrenci, notlar in students.items():
            ortalama = sum(notlar)//len(notlar)
            if ortalama > en_yuksek_ortalama:
                en_yuksek_ortalama = ortalama
                en_iyi_ogrenci = ogrenci

        print('En basarili ogrenci :', en_iyi_ogrenci ,' - ','GPA :', en_yuksek_ortalama)

    elif secim == 3:
        isimler = []
        soyisimler = []
        for ogrenci in students.keys():
            isimler.append(ogrenci.split()[0])
        tupleisimler= tuple(isimler)
        for ogrenci in students.keys():
            soyisimler.append(ogrenci.split()[1])
        tuplesoyisimler= tuple(soyisimler)
        print(tupleisimler)
        print(tuplesoyisimler)
    elif secim == 4:
        names = []
        for isim in students.keys():
            names.append(isim)
        print(sorted(names))


    elif secim == 5:
        basarisizlar=[]
        for ogrenci, notlar in students.items():
            ortalama = sum(notlar) // len(notlar)
            if ortalama < 70:
                basarisizlar.append(ogrenci)
        basarisizlarkumesi = set(basarisizlar)
        print(basarisizlarkumesi)

    else:
        print('Gecerli bir sayi giriniz :')




   # Question2




print('\n1. Film Ekleyin\n2. Filmi Duzenleyin\n3. Koleksiyonu Goruntuleyin\n')
tumfilmler = {}

while True:
    try:
        secim1 = int(input("Seciminizi giriniz: "))
        if secim1 == 1:
            ad = input('Film adini giriniz : ')
            tur = input('Film turunu giriniz : ')
            yonetmen = input('Yonetmen adini giriniz : ')
            yil = input('Yayin yilini giriniz : ')
            yenikayit = {'Film adi': ad, 'Film turu': tur, 'Yonetmen': yonetmen, 'Yayin yili': yil}
            tumfilmler[ad] = yenikayit
            print("\nFilm başarıyla eklendi!\n")

        elif secim1 == 2:
            film_adi = input('Düzenlemek veya silmek istediğiniz filmin adını giriniz: ')
            if film_adi in tumfilmler:
                print(f"\nMevcut bilgiler: {tumfilmler[film_adi]}")
                print('\n1. Filmi Düzenle\n2. Filmi Sil\n')
                try:
                    alt_secim = int(input("Seçiminizi giriniz: "))
                    if alt_secim == 1:
                        tur = input('Yeni film turunu giriniz : ')
                        yonetmen = input('Yeni yönetmen adını giriniz : ')
                        yil = input('Yeni yayın yılını giriniz : ')
                        tumfilmler[film_adi] = {'Film adi': film_adi, 'Film turu': tur, 'Yonetmen': yonetmen, 'Yayin yili': yil}
                        print("\nFilm başarıyla güncellendi!\n")
                    elif alt_secim == 2:
                        del tumfilmler[film_adi]
                        print(f"\n'{film_adi}' adlı film başarıyla silindi.\n")
                    else:
                        print("\nGeçersiz seçim, lütfen tekrar deneyiniz.")
                except ValueError:
                    print("\nLütfen geçerli bir sayı giriniz.")
            else:
                print("\nFilm bulunamadı.\n")

        elif secim1 == 3:
            if not tumfilmler:
                print("\nKoleksiyonda film bulunmuyor.\n")
            else:
                print("\nKoleksiyondaki Filmler:")
                for film in tumfilmler.values():
                    print(f"- {film}")

        else:
            print("\nGeçersiz seçim, tekrar deneyiniz.")
    except ValueError:
        print("\nLütfen geçerli bir sayı giriniz.")

    devam = input("\nDevam etmek istiyor musunuz? (e/h): ")
    if devam.lower() != 'e':
        print("\nProgramdan çıkılıyor...")
        break


   #Question3



print('\n1. Müşteri Ekleyin\n2. Müşteriyi Düzenleyin\n3. Müşteri Silin\n4. Müşteri Listesini Görüntüleyin\n')
musteriler = {}
id_counter = 1

while True:
    try:
        secim = int(input("Seçiminizi giriniz: "))
        if secim == 1:
            ad = input('Müşteri adı: ')
            soyad = input('Müşteri soyadı: ')
            telefon = input('Telefon numarası: ')
            email = input('E-posta adresi: ')
            yeni_musteri = {'ID': id_counter, 'Ad': ad, 'Soyad': soyad, 'Telefon': telefon, 'Email': email}
            musteriler[id_counter] = yeni_musteri
            print(f"\nMüşteri başarıyla eklendi! Müşteri ID: {id_counter}\n")
            id_counter += 1
        elif secim == 2:
            try:
                musteri_id = int(input('Düzenlemek istediğiniz müşterinin ID numarasını giriniz: '))
                if musteri_id in musteriler:
                    print(f"\nMevcut bilgiler: {musteriler[musteri_id]}")
                    ad = input('Yeni müşteri adı: ')
                    soyad = input('Yeni müşteri soyadı: ')
                    telefon = input('Yeni telefon numarası: ')
                    email = input('Yeni e-posta adresi: ')
                    musteriler[musteri_id] = {'ID': musteri_id, 'Ad': ad, 'Soyad': soyad, 'Telefon': telefon, 'Email': email}
                    print("\nMüşteri başarıyla güncellendi!\n")
                else:
                    print("\nGirilen ID ile eşleşen müşteri bulunamadı.\n")
            except ValueError:
                print("\nLütfen geçerli bir sayı giriniz.")
        elif secim == 3:
            try:
                musteri_id = int(input('Silmek istediğiniz müşterinin ID numarasını giriniz: '))
                if musteri_id in musteriler:
                    del musteriler[musteri_id]
                    print(f"\nMüşteri başarıyla silindi (ID: {musteri_id}).\n")
                else:
                    print("\nGirilen ID ile eşleşen müşteri bulunamadı.\n")
            except ValueError:
                print("\nLütfen geçerli bir sayı giriniz.")
        elif secim == 4:
            if not musteriler:
                print("\nSistemde kayıtlı müşteri bulunmuyor.\n")
            else:
                print("\nKayıtlı Müşteriler:")
                for musteri in musteriler.values():
                    print(f"- ID: {musteri['ID']}, Ad: {musteri['Ad']}, Soyad: {musteri['Soyad']}, Telefon: {musteri['Telefon']}, Email: {musteri['Email']}")
        else:
            print("\nGeçersiz seçim, tekrar deneyiniz.")
    except ValueError:
        print("\nLütfen geçerli bir sayı giriniz.")
    devam = input("\nDevam etmek istiyor musunuz? (e/h): ")
    if devam.lower() != 'e':
        print("\nProgramdan çıkılıyor...")
        break

