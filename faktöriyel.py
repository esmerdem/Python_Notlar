print("Bir sayının faktörüyelini bulma..."
      "Çıkmak için q'ya basınız")
while True:
    girdi = input("Bir sayı girin(Çıkmak için q'ya basın):")

    if girdi == "q":
        break
    else:
        girdi = int(girdi)
        sabit = 1
        for i in range(2,girdi + 1):
            sabit *= i
        print(sabit)


































