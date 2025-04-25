def add_customer(customers, next_id):
    print("Yeni musteri ekleme islemi:")

    name = input("Musteri adi: ")
    surname = input("Musteri soyadi: ")
    email = input("E-posta adresi: ")
    phone = input("Telefon numarasi: ")

    # Yeni musteri bilgilerini sozluge ekle
    customers[next_id] = {
        "name": name,
        "surname": surname,
        "email": email,
        "phone": phone
    }

    print(f"{next_id} ID numarasi ile musteri eklendi.")
    return next_id + 1  # Sonraki musteri ID'si icin bir sonraki numarayi dondur
