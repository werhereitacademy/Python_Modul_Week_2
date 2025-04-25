# Film kolleksiyonu oluşturma ve yönetme

import json

# Film verilerini başta yükle
try:
    with open("filmler.json", "r", encoding="utf-8") as f:
        filmler = json.load(f)
except FileNotFoundError:
    filmler = {}

# Film Menüsü
msayi = int(input("Film ekleme için 1'e, \nfilm listelemek için 2'ye, \nfilm güncelleme için 3'e, \nfilm silmek için 4'e basın: "))
if msayi == 1:

    #Film Kolleksiyon Girişi

    while True:
        film_adi = input("Film adı (çıkmak için 'q' girin): ")
        if film_adi.lower() == 'q':
            break
        yil = input("Yıl: ")
        yonetmen = input("Yönetmen: ")
        tur = input("Tür: ")
        
        # Film bilgilerini sözlükte sakla
        filmler[film_adi] = {
            'yil': yil,
            'yonetmen': yonetmen,
            'tur': tur
        }

        with open("filmler.json", "w", encoding="utf-8") as f:
            json.dump(filmler, f, ensure_ascii=False, indent=4)
        print(f"{film_adi} filmi koleksiyona eklendi.")

elif msayi == 2:
    # Film Listeleme (Tüm Liste veya Türe göre Filtreleme)
        filtre = input("Filtrelemek ister misiniz? (E/H): ").lower()
        if filtre == 'e':
            tur_filtre = input("Filtrelemek istediğiniz tür: ")
            print(f"{tur_filtre} türündeki filmler:")
            for film, bilgiler in filmler.items():
                if bilgiler['tur'].lower() == tur_filtre.lower():
                    print(f"Film: {film}, Yıl: {bilgiler['yil']}, Yönetmen: {bilgiler['yonetmen']}, Tür: {bilgiler['tur']}")
        else:
            print("Tüm filmler:")
            for film, bilgiler in filmler.items():
                print(f"Film: {film}, Yıl: {bilgiler['yil']}, Yönetmen: {bilgiler['yonetmen']}, Tür: {bilgiler['tur']}")


elif msayi == 3:
    # Film Güncelleme
        film_adi = input("Güncellemek istediğiniz film adı: ")
        if film_adi in filmler:
            yil = input("Yeni yıl: ")
            yonetmen = input("Yeni yönetmen: ")
            tur = input("Yeni tür: ")
            
            # Film bilgilerini güncelle
            filmler[film_adi] = {
                'yil': yil,
                'yonetmen': yonetmen,
                'tur': tur
            }
            with open("filmler.json", "w", encoding="utf-8") as f:
                json.dump(filmler, f, ensure_ascii=False, indent=4)
            print(f"{film_adi} filmi güncellendi.")
        else:
            print(f"{film_adi} filmi bulunamadı.")

elif msayi == 4:

    # Film Silme
        film_adi = input("Silmek istediğiniz film adı: ")
        if film_adi in filmler:
            del filmler[film_adi]
            with open("filmler.json", "w", encoding="utf-8") as f:
                json.dump(filmler, f, ensure_ascii=False, indent=4)
            print(f"{film_adi} filmi silindi.")
        else:
            print(f"{film_adi} filmi bulunamadı.")
