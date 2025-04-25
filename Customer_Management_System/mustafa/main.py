musteriler = [12345, 23456, 34567]
bilgileri = [["ahmet Mümtaz", "ahmet@gmail.com", 685001122], ["Fırat Tanış", "fırat@gmail.com", 685112233],
             ["Taner Birsel", "taner@gmail.com", 685223344]]
musteri_bilgi = dict(zip(musteriler, bilgileri))

while True:
    print("Tüm Müşterileri Listelemek İçin 1,\nYeni Müşteri Eklemek İçin 2,\nMüşteri Bilgilerini Güncellemek İçin 3,\n" \
    "Müşteriyi Silmek için 4,\n Çıkış Yapmak İçin 5,\nYazınız")
    secim = input("...")

    if secim == '1':
        if not musteri_bilgi:
          print("Henüz Herhangi Bir Müşteri Girlmemiştir.")
        else:
           print("Film Deporsunun Güncel Hali: ")
           for id, info in musteri_bilgi.items():
              print(f"{id} ID numaralı müşterinin, İsmi: {info[0]}, Mail Adresi: {info[1]}, Telefon Numarası: {info[2]}")

    elif secim == '2':
        while True:
            id = int(input("Müşterinin ID'si"))
            if id in musteri_bilgi:
                print("Girdiğiniz ID'li müşteri zaten kayıtlı.")
            else:
                musteri_bilgi[id] = [
                    input("Müşterinin Adı: "),
                    input("Müşterinin Mail Adresi: "),
                    input("Müşterinin Telefon Numarası: "),
                ]
           
                while True:
                    enyeni_id = input("Eğer yeni bir müşteri daha girecekseniz 'E',\nAna menüye dönecekseniz 'M'\nYazınız")
                    if enyeni_id.lower() == 'e':
                        break
                    elif enyeni_id.lower() == 'm':
                        for id, bilgileri in musteri_bilgi.items():
                            print(f"""Güncel Müşteri Listesi: 
                                  \n{id} ID numaralı müşterinin \nAdı: {bilgileri[0]}, 
                                  Mail Adresi: {bilgileri[1]}, 
                                  Telefon Numarası: {bilgileri[2]}""") 
                        break
                    else:
                        print("Geçersiz bir giriş yaptınız.")
                
                if enyeni_id.lower() == 'm':
                    break
    
    elif secim == '3':
        if not musteri_bilgi:
            print("Müşteri Listsi Boştur.")
        print("Düzenlemek İstediğiniz Müşterinin ID'sini Giriniz: ")

        secim3 = int(input("GÜncellenecek Müşteri ID'si: "))
        try:
            secim3 = int(input("Güncellenecek Müşteri ID'si: "))
        except ValueError:
            print("Geçerli bir sayısal ID giriniz.")
            continue

        if secim3 in musteri_bilgi:
            print(f"{secim3} ID'li müşteri bulundu.")
            print(f"Mevcut Bilgileri: \nAdı: {secim3[0]}\nMaili: {secim3[1]}\nTelefonu: {secim3[2]}")

            musteri_bilgi[secim3] = [
                input("Müşterinin Adı: "), 
                input("Müşterinin Maili: "), 
                input("Müşterinin Telefonu: ")
            ]
            print("Müşteri Bilgileri Güncellendi.")
        else:
            print("Girdiğiniz ID'li müşteri listede yok.")

    elif secim == '4':
        if not musteri_bilgi:
            print("Müşteri Listsi Boştur.")
            continue

        while True:
            try:
                secim4 = int(input("Silmek İstenen Müşteri ID'si: "))
                if secim4 in musteri_bilgi:
                    onay = input(f"{secim4} ID'li müşteriyi silmek istediğinize emin misiniz? Evet ise 'E' basınız.")
                    if onay.lower == 'e':
                        del musteri_bilgi[secim4]
                        print(f"{secim4} ID'li müşteri bilgileri listeden silindi.")
                    else:
                        print("Silme işlemi iptal edildi.")
                else:
                    print(f"{secim4} ID'li müşteri listede yok.")
                    break
            except ValueError:
                print("Geçerli bir sayısal ID giriniz.")

    elif secim == '5':
        print("Çıkılıyor...")
        break
    
    else:
        print("Hatalı Giriş Yaptınmız, 1-5 arasında bir değer giriniz.")
              
