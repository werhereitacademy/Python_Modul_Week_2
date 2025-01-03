import json

# Dosya yolu
json_dosyasi = "customer.json"

# Müşteri ID sayacı
id_sayaci = 1

# JSON dosyasını yükleme veya yeni bir dosya oluşturma
def dosya_yukle():
    try:
        with open(json_dosyasi, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# JSON dosyasını kaydetme
def dosya_kaydet(data):
    with open(json_dosyasi, "w") as file:
        json.dump(data, file, indent=4)

# Yeni müşteri ekleme
def musteri_ekle():
    global id_sayaci
    musteri_adi_soyadi = input("Müşteri Adı Soyadı: ")
    telefon = input("Telefon: ")
    email = input("Email: ")
    
    # Dosyayı yükle
    musteri_liste = dosya_yukle()

    # Yeni ID oluştur
    yeni_id = str(id_sayaci)
    id_sayaci += 1  # ID sayacını bir artır

    # Müşteri bilgilerini listeye ekle
    musteri_liste[yeni_id] = {"ad_soyad": musteri_adi_soyadi, "telefon": telefon, "email": email}
    
    # Dosyayı kaydet
    dosya_kaydet(musteri_liste)
    print(f"{musteri_adi_soyadi} başarıyla eklendi! (Müşteri ID: {yeni_id})")

# Müşteri bilgilerini düzenleme
def musteri_duzenle():
    musteri_liste = dosya_yukle()
    musteri_id = input("Düzenlemek istediğiniz müşteri ID'si: ")

    if musteri_id in musteri_liste:
        print(f"Mevcut Bilgiler: Ad Soyad: {musteri_liste[musteri_id]['ad_soyad']}, Telefon: {musteri_liste[musteri_id]['telefon']}, Email: {musteri_liste[musteri_id]['email']}")
        
        yeni_ad_soyad = input("Yeni Ad Soyad (değiştirmeyecekseniz boş bırakın): ")
        yeni_telefon = input("Yeni Telefon (değiştirmeyecekseniz boş bırakın): ")
        yeni_email = input("Yeni Email (değiştirmeyecekseniz boş bırakın): ")

        if yeni_ad_soyad:
            musteri_liste[musteri_id]["ad_soyad"] = yeni_ad_soyad
        if yeni_telefon:
            musteri_liste[musteri_id]["telefon"] = yeni_telefon
        if yeni_email:
            musteri_liste[musteri_id]["email"] = yeni_email

        dosya_kaydet(musteri_liste)
        print(f"Müşteri ID {musteri_id} başarıyla güncellendi!")
    else:
        print("Bu ID'ye sahip bir müşteri bulunamadı.")

# Müşteri silme
def musteri_sil():
    musteri_liste = dosya_yukle()
    musteri_id = input("Silmek istediğiniz müşteri ID'si: ")

    if musteri_id in musteri_liste:
        del musteri_liste[musteri_id]
        dosya_kaydet(musteri_liste)
        print(f"Müşteri ID {musteri_id} başarıyla silindi!")
    else:
        print("Bu ID'ye sahip bir müşteri bulunamadı.")

# Tüm müşterileri listeleme
def musterileri_goruntule():
    musteri_liste = dosya_yukle()
    if musteri_liste:
        print("\nTüm Müşteriler:")
        for musteri_id, bilgiler in musteri_liste.items():
            print(f"ID: {musteri_id} - Ad Soyad: {bilgiler['ad_soyad']}, Telefon: {bilgiler['telefon']}, Email: {bilgiler['email']}")
    else:
        print("Hiç müşteri bulunamadı.")

# Ana menü
while True:
    print("\nİşlem Menüsü:")
    print("1- Yeni Müşteri Ekle")
    print("2- Müşteri Bilgilerini Düzenle")
    print("3- Müşteri Sil")
    print("4- Tüm Müşterileri Görüntüle")
    print("5- Çıkış")

    secim = input("Bir işlem seçiniz: ")

    if secim == "1":
        musteri_ekle()
    elif secim == "2":
        musteri_duzenle()
    elif secim == "3":
        musteri_sil()
    elif secim == "4":
        musterileri_goruntule()
    elif secim == "5":
        print("Çıkış yapılıyor...")
        break
    else:
        print("Geçersiz seçim. Lütfen tekrar deneyin!")
