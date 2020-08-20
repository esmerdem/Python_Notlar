"""
Her bir while döngüsünde kullanıcıdan bir sayı alın ve kullanıcının girdiği sayıları "toplam" isimli bir değişkene
ekleyin. Kullanıcı "q" tuşuna bastığı zaman döngüyü sonlandırın ve ekrana "toplam değişkenini" bastırın.
"""
print("Sayıları toplama")

toplam = 0

while True:
    girdi = input("Sayı:(Çıkmak için q'ya basınız)")
    if (girdi == "q"):
        print(toplam)
        break
    else:
        girdi = int(girdi)
        toplam += girdi




























