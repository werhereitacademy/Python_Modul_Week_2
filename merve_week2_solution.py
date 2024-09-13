#SORU 1

ogrenci_bil={}
  
#1-
for i in range (10):
    ad_soyad=input( "ad-soyad:")
    vize=float(input(f"{ad_soyad} vize notu:"))
    final=float(input(f"{ad_soyad} final notu:"))
    sozlu=float(input(f"{ad_soyad} sozlu notu:"))
    ogrenci_bil[ad_soyad]={'vize':vize,'final':final,'sozlu':sozlu}
 

#2-
max_ortalama=0
max_adsoyad=""

for ad_soyad,deger in ogrenci_bil.items():
    vize=deger['vize']
    final=deger['final']
    sozlu=deger['sozlu']
    ortalama=(vize+final+sozlu)/3
    
    ogrenci_bil[ad_soyad]['ortalama']=ortalama
  
    ortalama=deger['ortalama']
    print(f"{ad_soyad}'in ortalamasi:",ortalama)

    if ortalama>max_ortalama:
        max_ortalama=ortalama
        max_adsoyad=ad_soyad
print(f"en basarili kisi:{max_adsoyad},Ortalama:{max_ortalama}")
    
 #3-       
liste_ad=[]
liste_soyad=[]

for adsoyad in ogrenci_bil:
    ad,soyad=adsoyad.split()
    liste_ad.append((ad,))
    liste_soyad.append((soyad,))
    

print("Isimler listesi:",liste_ad)
print("Soyisimler listesi:",liste_soyad)


#4-
sirali_isim=sorted(liste_ad)
print("sirali liste:",sirali_isim)

#5-
kume=set()

    
if deger['ortalama']<70:
       
       kume.add(ad_soyad)

       print("Ortalamasi 70'in altinda olanlar:",kume)





#SORU 2
import pickle

film_arsiv={}
def veri_kaydet(dosya_adi,veri):
    with open(dosya_adi,'wb') as dosya:
        pickle.dump(veri,dosya)

def veri_yukle(dosya_adi):
    try:
        with open(dosya_adi,'rb') as dosya:
            veri=pickle.load(dosya)
            return veri
    except FileNotFoundError:
        return{}

film_arsiv=veri_yukle('film_arsiv.pkl')

print("------------Film Arsivi------------")

while True:
    print("\nYapmak istediginiz islemi seciniz")
    print("\n1.Film Ekleme")
    print("\n2.Film Guncelleme")
    print("\n3.Film Silme")
    print("\n4.Arsivi Goruntuleme")
    print("\nq.Cikis Yapma")
    
    sec=input("\nIsleme ait numarayi giriniz:")
    if sec=="q":
        print("\nCikis yapiliyor..")
        break
    elif sec=="1":

        ad=input("\nfilm adi:")
        yonetmen=input(f"\n{ad} filmi-yonetmeni:")
        tur=input(f"\n{ad} filmi-turu:")
        yil=input(f"\n{ad} filmi-yayin yili:")
        film={'yonetmen':yonetmen,'tur':tur,'yayin yili':yil}
        film_arsiv[ad]=film
        
        print("\nEkleme basariyla yapildi..")

    elif sec=="2":
        ad=input("\nGuncellemek istediginiz film adi:")

        if ad in film_arsiv:
           print(f"\n {ad} filmi icin bilgiler:{film_arsiv[ad]}")
           kategori=input("\nGuncellemek istediginiz kategori:\nYonetmen-yayin yili-tur\n")
           yeni_bilgi=input(f"\n{kategori} icin yeni bilgi:")
           if kategori in film_arsiv[ad]:
                 film_arsiv[ad][kategori]=yeni_bilgi
                 print(f"{ad} filmi basariyla guncellendi")
           else:
                 print(f"Girdiginiz {kategori} mevcut degil. ")
        else:
            print("Girdiginiz film ismi mevcut degil..")


    
    elif sec=="3":
        yeni_ad=input("\nSilme islemi yapmak istediginiz film adi:")
        if yeni_ad in film_arsiv:
           print(f"\n {yeni_ad} filmi icin bilgiler:{film_arsiv[ad]}")
           kategori_sil=input("\nSilmek istediginiz kategori:\nAd-Yonetmen-yayin yili-tur\n")
          
           if kategori_sil in film_arsiv[ad]:
                 film_arsiv[ad].pop(kategori_sil)
                 print(f"{kategori_sil} basariyla silindi")
           

           elif kategori_sil:
                 del film_arsiv[ad]
                 print(f"{yeni_ad} filmi basariyla silindi")

           else:
                print(f"Girdiginiz {kategori_sil} mevcut degil. ")
        else:
            print("Girdiginiz film adi mevcut degil..")

    elif sec=="4":
        filtre = input("Filtrelemek istiyor musunuz? (evet/hayır): ")

        if filtre == 'evet':

            kriter = input("Filtrelemek istediğiniz kriter nedir? (Yonetmen, Tur, Yayın Yılı): ")

            deger = input(f"Filtrelemek istediğiniz {kriter}: ")

            for film, bilgiler in film_arsiv.items():

              if bilgiler.get(kriter) == deger: 
                  print(f"Film: {film}, Yonetmen: {bilgiler['yonetmen']}, Yayın Yılı: {bilgiler['yayin yili']}, Tur: {bilgiler['tur']}")

        elif filtre == 'hayir':

            for film, bilgiler in film_arsiv.items():

               print(f"Film: {film}, Yönetmen: {bilgiler['yonetmen']}, Yayın Yılı: {bilgiler['yayin yili']}, Tur: {bilgiler['tur']}")
        else: 
            print("Geçersiz seçim.")


#SORU 3

musteri_sozluk={}
musteri_id=20
print("---------Musteri Yonetim Sistemi---------")
while True:
    
    
    print("1.Yeni Musteri Ekle")
    print("2.Musteri Bilgilerini Guncelle")
    print("3.Musteri Sil")
    print("4.Tum Musterileri Goruntule")
    print("5.Cikis Yap")

    secim=input("Yapmak istediginiz islemi secin(1-5):")
    
    if secim=="1":
        ad=input("Musteri Adi:")
        soyad=input("Musteri Soyadi:")
        email=input("E-posta:")
        tel=input("Telefon Numarasi::")

        musteri_sozluk[musteri_id]={"Ad":ad,"Soyad":soyad,"E-posta":email,"Telefon":tel}
        print(f"Musteri eklendi..\nMusteri ID'si:{musteri_id}")
        musteri_id += 1

    elif secim=="2":
        id_guncelle=int(input("Guncellenecek Musteri ID'si:"))
        if id_guncelle in musteri_sozluk:
            print(f"Mevcut bilgiler:{musteri_sozluk[id_guncelle]}")
            print("Guncellemek istediginiz bilgiyi seciniz:")
            print("1.Tum Bilgiler")
            print("2.Ad")
            print("3.Soyad")
            print("4.E-mail")
            print("5.Telefon")
            guncel_secim=input("bir secim yapin(1-4):")

            if guncel_secim=="1":
                guncel_ad=input("Yeni Ad:")
                guncel_soyad=input("Yeni Soyad:")
                guncel_email=input("Yeni E-mail:")
                guncel_tel=input("Yeni Telefon No:")

                musteri_sozluk[id_guncelle]["Ad"]=guncel_ad
                musteri_sozluk[id_guncelle]["Soyad"]=guncel_soyad
                musteri_sozluk[id_guncelle]["E-posta"]=guncel_email
                musteri_sozluk[id_guncelle]["Telefon"]=guncel_tel

                print("Bilgiler basariyla guncellendi...")

            elif guncel_secim=="2":
                 guncel_ad=input("Yeni Ad:")
                 musteri_sozluk[id_guncelle]["Ad"]=guncel_ad
                 print("Ad guncellendi...")

            elif guncel_secim=="3":
                 guncel_soyad=input("Yeni Soyad:")
                 musteri_sozluk[id_guncelle]["Soyad"]=guncel_soyad
                 print("Soyad guncellendi...")
            
            elif guncel_secim=="4":
                 guncel_email=input("Yeni E-mail:")
                 musteri_sozluk[id_guncelle]["E-posta"]=guncel_email
                 print("E-mail guncellendi...")
             
            elif guncel_secim=="5":
                 guncel_tel=input("Yeni Telefon No:")
                 musteri_sozluk[id_guncelle].update({"Telefon":guncel_tel})
                 print("Telefon guncellendi...")

            else:
                print("Gecersiz secim..")

        else:
            print("Gecersiz ID..!!")

    elif secim=="3":
         musteri_sil=int(input("Silinecek musteri ID'si:"))

         if musteri_sil in musteri_sozluk:
            del musteri_sozluk[musteri_sil]
            print("Musteri silindi...")

         else:
             print("Gecersiz ID..!!")

    elif secim=="4":
         if musteri_sozluk:
            for id,bilgiler in musteri_sozluk.items():
                print(f"ID:{id},Bilgiler:{bilgiler}")

         else:
             print("Hic musteri yok!!")
    
    elif secim=="5":

         print("Sistemden cikiliyor..")
         break

    else:
         print("Gecersiz secim..Lutfen tekrar deneyin.")


