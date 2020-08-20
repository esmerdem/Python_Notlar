"""
Kullanıcıdan aldığınız bir sayının "Armstrong" sayısı olup olmadığını bulmaya çalışın.

Örnek olarak, Bir sayı eğer 4 basamaklı ise ve oluşturan rakamlardan herbirinin 4. kuvvetinin toplamı( 3 basamaklı sayılar için
3.kuvveti ) o sayıya eşitse bu sayıya "Armstrong" sayısı denir.

Örnek olarak : 1634 = 1^4 + 6^4 + 3^4 + 4^4
"""
sayı = input("Sayı:")
sayı1 = int(sayı)
liste = [i for i in sayı]
boy = len(liste)
boy2 = len(liste)
toplam = 0
while boy >0:
    sayı = int(sayı)
    kalan = sayı % 10
    toplam += kalan ** boy2
    sayı = sayı / 10
    boy -= 1
if toplam == sayı1:
    print("Armstrong sayısı")
else:
    print("Değil")
















