print("""
Kullanıcı girişi
""")
giriş_adı = "erdemkral"
şifre = "erdem"
giriş_hakkı = 3

while True:
    giriş_sor = input("Kullanıcı adı:")
    şifre_sor = input("Kullanıcı şifresi:")
    if giriş_sor != giriş_adı and şifre != şifre_sor:
        giriş_hakkı -= 1
        print("Hatalı giriş...")
    elif giriş_sor == giriş_adı and şifre != şifre_sor:
        giriş_hakkı -= 1
        print("Hatalı giriş...")
    elif giriş_sor != giriş_adı and şifre == şifre_sor:
        giriş_hakkı -= 1
        print("Hatalı giriş...")
    else :
        print("Başarılı giriş...")
        break
    if giriş_hakkı == 0:
        print("Giriş hakkınız bitti...")
        break




















