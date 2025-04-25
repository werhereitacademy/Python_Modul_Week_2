#yapay zeka'nın yardımıyla yapildi.


def film_ekle(filmler):
    film = {
        'isim': input("Film adı: "),
        'yonetmen': input("Yönetmen: "),
        'yayin_yili': input("Yayın yılı: "),
        'tur': input("Tür: ")
    }
    filmler.append(film)
    print("Film eklendi!")

def film_duzenle(filmler):
    film_adi = input("Düzenlemek istediğiniz film adı: ")
    for film in filmler:
        if film['isim'].lower() == film_adi.lower():
            film['isim'] = input("Yeni film adı: ")
            film['yonetmen'] = input("Yeni yönetmen: ")
            film['yayin_yili'] = input("Yeni yayın yılı: ")
            film['tur'] = input("Yeni tür: ")
            print("Film düzenlendi!")
            return
    print("Film bulunamadı.")

def film_sil(filmler):
    film_adi = input("Silmek istediğiniz film adı: ")
    for film in filmler:
        if film['isim'].lower() == film_adi.lower():
            filmler.remove(film)
            print("Film silindi!")
            return
    print("Film bulunamadı.")

def koleksiyonu_goruntule(filmler):
    filtre = input("Tüm filmleri görüntüle (hepsi) veya tür/yıl ile filtrele (tur/yil): ").lower()
    if filtre == 'hepsi':
        for film in filmler:
            print(film)
    elif filtre == 'tur':
        tur = input("Tür: ")
        for film in filmler:
            if film['tur'].lower() == tur.lower():
                print(film)
    elif filtre == 'yil':
        yil = input("Yayın yılı: ")
        for film in filmler:
            if film['yayin_yili'] == yil:
                print(film)
    else:
        print("Geçersiz seçenek.")

def main():
    filmler = []
    while True:
        print("\n1. Film ekle\n2. Film düzenle\n3. Film sil\n4. Koleksiyonu görüntüle\n5. Çıkış")
        secim = input("Seçiminiz: ")
        if secim == '1':
            film_ekle(filmler)
        elif secim == '2':
            film_duzenle(filmler)
        elif secim == '3':
            film_sil(filmler)
        elif secim == '4':
            koleksiyonu_goruntule(filmler)
        elif secim == '5':
            print("Çıkılıyor.")
            break
        else:
            print("Geçersiz seçim.")

if __name__ == "__main__":
    main()
