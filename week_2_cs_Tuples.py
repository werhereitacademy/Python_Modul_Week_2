nummers = []
n = int(input("n nummer:...  "))
giris = input("Sayıları boşluk bırakarak girin: ")

nummer = list(map(int, giris.split()))
nummers.append(nummer)
nummerstuple = tuple(nummers)
hashnummer = hash(nummerstuple)
print(hashnummer)