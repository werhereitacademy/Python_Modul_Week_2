film_deposu = {
    'Forrest Gump': [1994, 'Dram', 'Robert Zemeckis'],
    'Terminator 2': [1991, 'Aksiyon', 'James Cameron'],
    'İnception': [2010, 'Bilim Kurgu', 'Christopher Nolan'], 
    'Piyanist': [2002, 'Trajedi', 'Roman Polnaski'], 
    'Prestij': [2006, 'Dram', 'Christopher Nolan']               
}  

while True:
    print("Film listelerini görüntülemek için 1,\nFİlm eklemek için 2, \nFilm düzenlemek için 3, \nFilm silmek için 4 yazınız.")
    secim1 = input("...")

    if secim1 == '1':
        if not film_deposu:
            print("Henüz film eklenmemiştir.")
        else:
            print("Film Deposunun Güncel Hali: ")
            for film, bilgiler in film_deposu.items():
                print(f"- {film}: Yapım Yılı: {bilgiler[0]}, Tür: {bilgiler[1]}, Yönetmen: {bilgiler[2]}")


    elif secim1 == '2': 
        while True:
            film_adi = input("Filmin Adı: ")
            film_deposu[film_adi] = [
                input("Yapım Yılı: "), 
                input("Türü: "),
                input("Yönetmeni: ")
            ]
            
            while True:
                yeni_film = input("Yeni bir film daha girecekseniz 'E', \nMenüde devam etmek için ise 'M' harfine basınız: ")
                if yeni_film.lower() == 'e':
                    break  
                elif yeni_film.lower() == 'm':
                    print("Film Deposunun Güncel Hali:")
                    for film, bilgiler in film_deposu.items():
                        print(f"- {film}: Yapım Yılı: {bilgiler[0]}, Tür: {bilgiler[1]}, Yönetmen: {bilgiler[2]}")
                    break 
                else:
                    print("Geçersiz bir seçim yaptınız.")
            
            if yeni_film.lower() == 'm':
                break  

    elif secim1 == '3':
        if not film_deposu:
            print("Henüz film eklenmemiştir.")
            continue
        print("Düzenlemek istediğiniz filmi seçiniz: ")
        film_listesi = list(film_deposu.keys())
        for i, film in enumerate(film_listesi, 1):
            print(f"{i}. {film}")

        try:
            secim2 = int(input("Film Numarasını Giriniz: ")) - 1
            film_adi = film_listesi[secim2]

            print("Mevcut Bilgiler: ")
            print("1- Yapım Yılı: ", film_deposu[film_adi][0])
            print("2- Türü: ", film_deposu[film_adi][1])
            print("3- Yönetmeni: ", film_deposu[film_adi][2])

            degisiklik = input("Hangi bilgiyi düzenlemek istiyorsunuz? 1, 2 veya 3 Yazınız: ")

            if degisiklik == '1':
                film_deposu[film_adi][0] = input("Yeni yapım yılı: ")
            elif degisiklik == '2':
                film_deposu[film_adi][1] = input("Yeni Tür: ")
            elif degisiklik == '3':
                film_deposu[film_adi][2] = input("Yeni Yönetmen: ")
            else:
                print("Geçersiz seçim.")
        except (IndexError, ValueError):
            print("Geçersiz Film Numarası")

    elif secim1 == '4':
        if not film_deposu:
            print("Henüz film eklenmemiştir.")
            continue
        print("Silmek istediğiniz filmi seçiniz: ")
        film_listesi = list(film_deposu.keys())
        for i, film in enumerate(film_listesi, 1):
            print(f"{i}, {film}")

        try:
            secim3 = int(input("Film Numarasını Giriniz: ")) - 1
            film_adi = film_listesi[secim3]
            del film_deposu[film_adi]
            print(f"{film_adi} filmi silindi.")
        except (IndexError, ValueError):
            print("Geçersiz Film Numarası")

        
        