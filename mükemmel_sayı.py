print("Mükemmel sayı")

a = int(input("Bir sayı giriniz:"))

i = 1
toplam = 0

while (i < a):
    if (a % i == 0):
        toplam += i
    i += 1

if (toplam == a):
    print("{} bir mükemmel sayıdır.".format(a))
else:
    print("{} bir mükemmel sayı değildir".format(a))

































