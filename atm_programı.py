print("******************"
      "ATM"
      "İşlem seçiniz..."
      "Bakiye sorgulamak için 1'i"
      "Para çekmek için 2'yi"
      "Para yatırmak için 3'e tıklayınız..."
      "Çıkmak için q'ya tıklayınız"
      "******************")
bakiye = 1000
while True:
    işlem = input("Lütfen işlem seçiniz:")
    if (işlem == "q"):
        break
    elif (işlem == "1"):
        print("Bakiyeniz:",bakiye)
    elif (işlem == "2"):
        tutar = int(input("Çekmek istediğiniz tutarı giriniz:"))
        if (tutar <= bakiye):
            bakiye -= tutar
            print("Kalan bakiye miktarı:",bakiye)
            continue
        print("Yetersiz bakiye")
    elif (işlem == "3"):
        para_yatır = int(input("Yatırmak istediğiniz tutarı giriniz:"))
        bakiye += para_yatır
        print("Kalan bakiye miktarı:", bakiye)
    else:
        print("Geçersiz işlem...")


































