print("*********************** -- V A K I F B A N K -- ***********************")

deftc ="xxx"
defsifre = "123"
bakiye = int("0")

while(True):
    tc = input("TCNİZİ GİRİN:")
    sifre = input("ŞİFRENİZİ GİRİN:")

    if (deftc == tc) and (defsifre == sifre):
        print("Hoşgeldiniz.")
        print("Güncel bakiyeniz", bakiye, "TL")

        break
    elif (deftc == tc) and (defsifre != sifre):
        print("Yanlış Şifre! Şifrenizi değiştirmek ister misiniz ? E/H")
        cevap = input()
        if cevap == "e":
            yenisifre = input("Yeni şifrenizi giriniz:")
            defsifre = yenisifre
    else:
        print("Tekrar deneyiniz")

while(True):
    print("PARA YATIR (Y) - PARA ÇEK (Ç) - İŞLEMİ SONLANDIR (S)")
    paraislemlericevap = input()
    if paraislemlericevap == "y":
        yenipara = int(input("Yatırmak istediğiniz miktarı giriniz:"))
        if (yenipara > 0):
            bakiye = bakiye + yenipara
            print("Güncel bakiyeniz",bakiye,"TL")
        else:
            print("Pozitif veya 0'dan büyük bir sayı giriniz.")
    elif paraislemlericevap == "ç":
        yenipara = int(input("Çekmek istediğiniz miktarı giriniz:"))
        if (yenipara > 0):
            bakiye = bakiye - yenipara
            if (bakiye < 0):
                print("Hesabınızda yeterli miktarda para yok.")
                bakiye = bakiye + yenipara
                print("Güncel bakiyeniz", bakiye, "TL")
            else:
                print("Güncel bakiyeniz",bakiye,"TL")

        else:
            print("Pozitif veya 0'dan büyük bir sayı giriniz.")

    elif paraislemlericevap == "s":
        print("Bizi tercih ettiğiniz için teşekkürler!")
        print("*********************** -- V A K I F B A N K -- ***********************")
        break

    else:
        print("Lütfen 'Y' , 'Ç' veya 'S' harflerinden birini tuşlayınız.")











