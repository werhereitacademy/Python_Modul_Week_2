#1- https://www.hackerrank.com/challenges/list-comprehensions/problem
# Giriş: dört tam sayı
x = int(input("x değeri: "))
y = int(input("y değeri: "))
z = int(input("z değeri: "))
n = int(input("n değeri: "))

# Tüm permütasyonları oluşturuyoruz
permutasyonlar = [[i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1)]

# Toplamı n'ye eşit olmayanları filtreliyoruz
sonuc = [perm for perm in permutasyonlar if sum(perm) != n]

# Sonucu yazdırıyoruz
print(sonuc)

#2- https://www.hackerrank.com/challenges/python-tuples/problem
# Girdi olarak alınan sayılar
n = int(input())  # Tuple içindeki eleman sayısı
elemanlar = tuple(map(int, input().split()))  # Tuple'a dönüştürülen sayılar

# Hash fonksiyonunu kullanarak tuple'ın hash değerini hesapla
print(hash(elemanlar))

#3- 