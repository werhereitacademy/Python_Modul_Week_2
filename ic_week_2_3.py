# Müşteri Yönetim Sistemi

import json

# Müşteri verilerini başta yükle
try:
    with open("musteriler.json", "r", encoding="utf-8") as f:
        musteriler = json.load(f)
except FileNotFoundError:
    musteriler = {}

# Müşteri Yönemit Sistemi Ana Menüsü
# msayi = int(input("Müşteri Ekleme için 1'e, \nMüşteri Bilgilerini Listelemek için 2'ye, \nMüşteri Bilgilerini Güncelleme için 3'e, \nMüşteri Silmek için 4'e,\nProgramdan Çıkmak için 5'e basın: "))
# if msayi == 1:

    #Müşteri Bilgi Girişi

while True:
    # Müşteri Yönemit Sistemi Ana Menüsü
    # Kullanıcıdan işlem seçmesini iste
    msayi = int(input("\n1- Müşteri Ekleme \n2- Müşteri Bilgilerini Listeleme \n3- Müşteri Bilgilerini Güncelleme \n4- Müşteri Silmek\n5- Programdan Çıkış \n\nDevam etmek için bir sayı giriniz :"))
    if msayi == 1:
        
        # Müşteri Bilgi Girişi
        while True:
            mid = input("Müsteri ID giriniz veya \n(**Müşteri Eklemeden Çıkmak Q'ya basınız**): ")
            if mid.lower() == "q":
                print("Müşteri ekleme işlemi iptal edildi.")
                break
            elif mid in musteriler:
                print("Bu müşteri ID'si zaten mevcut.")
                continue
           
            # Müşteri bilgilerini al
            adi = input("Adı : ")
            soyadi = input("Soyadı: ")
            eposta = input("E-posta: ")
            telefon = input("Telefon: ")
            
            # Müşteri bilgilerini sözlükte sakla
            musteriler[mid] = {
                'adi': adi,
                'soyadi': soyadi,
                'eposta': eposta,
                'telefon': telefon
            }

            # Müşteri bilgilerini JSON dosyasına yaz
            with open("musteriler.json", "w", encoding="utf-8") as f:
                json.dump(musteriler, f, ensure_ascii=False, indent=4)
            print(f"{mid} {adi} {soyadi} programa kayıt edildi.")

    elif msayi == 2:
        # Müşteri Listeleme (Tüm Liste veya Türe göre Filtreleme)
            filtre = input("Filtrelemek ister misiniz? (E/H): ").lower()
            if filtre == 'e':
                adi_filtre = input("Filtrelemek istediğiniz Adlar: ")
                print(f"{adi_filtre} Adındaki Müşteriler:")
                for musteri, bilgiler in musteriler.items():
                    if bilgiler['adi'].lower() == adi_filtre.lower():
                        print(f"Müşteri: {musteri}  Adı: {bilgiler['adi']}, Soyadı: {bilgiler['soyadi']}, E-Posta: {bilgiler['eposta']}, Telefon: {bilgiler['telefon']}")
            else:
                print("Tüm Müşteriler:")
                for musteri, bilgiler in musteriler.items():
                    print(f"Müşteri: {musteri}  Adı: {bilgiler['adi']}, Soyadı: {bilgiler['soyadi']}, E-Posta: {bilgiler['eposta']}, Telefon: {bilgiler['telefon']}")

    # Müşteri Bilgilerini Güncelleme
    elif msayi == 3:

        print("Tüm Müşteriler:")
        for musteri, bilgiler in musteriler.items():
            print(f"Müşteri: {musteri}  Adı: {bilgiler['adi']}, Soyadı: {bilgiler['soyadi']}, E-Posta: {bilgiler['eposta']}, Telefon: {bilgiler['telefon']}")

        musteri_id = input("Güncellemek istediğiniz Müşteri ID: ")
        if musteri_id in musteriler:
            adi = input("Yeni Adı: ")
            soyadi = input("Yeni Soyadı: ")
            eposta = input("Yeni E-Posta: ")
            telefon = input("Yeni telefon: ")
                
            # Müşteri bilgilerini güncelle
            musteriler[musteri_id] = {
                'adi': adi,
                'soyadi': soyadi,
                'eposta': eposta,
                'telefon': telefon
                }
            with open("musteriler.json", "w", encoding="utf-8") as f:
                json.dump(musteriler, f, ensure_ascii=False, indent=4)
            print(f"{musteri_id} nolu müşteri güncellendi.")
        else:
            print(f"{musteri_id} nolu müşteri bulunamadı.")

    # Müşteri Bilgilerini Silme
    elif msayi == 4:
            print("Tüm Müşteriler:")
            for musteri, bilgiler in musteriler.items():
                print(f"Müşteri: {musteri}  Adı: {bilgiler['adi']}, Soyadı: {bilgiler['soyadi']}, E-Posta: {bilgiler['eposta']}, Telefon: {bilgiler['telefon']}")

            musteri_id = input("Silmek istediğiniz Müşteri ID: ")
            if musteri_id in musteriler:
                del musteriler[musteri_id]
                with open("musteriler.json", "w", encoding="utf-8") as f:
                    json.dump(musteriler, f, ensure_ascii=False, indent=4)
                print(f"{musteri_id} nolu müşteri silindi.")
            else:
                print(f"{musteri_id} nolu müşteri bulunamadı.")
    elif msayi == 5:
        # Programdan Çıkma
        print("Programdan çıkılıyor...")
        exit()
