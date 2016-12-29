import random
def menu_goruntule():
    print("1. Fal Bakma Oyunu")
    print("2. Blackjack (21) Oyunu")
    print("3. Çıkış")

def sayi_al(alt_sinir ,ust_sinir):
    sayi=int(input())
    while sayi<alt_sinir or sayi>ust_sinir:
        sayi=int(input("Hatalı veri girisi, lütfen tekrar giriniz:"))
    return sayi

def menu():
    cikis='h'
    while cikis=='H' or cikis=='h':
        menu_goruntule()
        print("Seciminizi giriniz [1-3]:",end='')
        secim=sayi_al(1,3)
        if secim==1:
            def deste_olustur():
                simgeler = ["Kupa", "Karo", "Maça", "Sinek"]
                sayılar = ["As", "İkili", "Üçlü", "Dörtlü", "Beşli", "Altılı", "Yedili", "Sekizli", "Dokuzlu", "Onlu",
                           "Vale","Kız", "Papaz"]
                deste = []
                for simge in simgeler:
                    for sayı in sayılar:
                        x = deste.append(simge + " " + sayı)
                return deste

            def islemler():
                ek_list = []
                ayrı_list = []
                sayac = 0

                deste = deste_olustur()
                for kart in deste:
                    if len(deste) >= 13:
                        uzunluk = 14
                    else:
                        uzunluk = len(deste)
                    for sayi in range(1, uzunluk):
                        kagit = random.choice(deste)
                        print(sayi, "-", end="")
                        print(kagit)
                        ek_list.append(kagit)
                        deste.remove(kagit)
                        sözlük = {'Kupa As': '1', 'Kupa İkili': '2', 'Kupa Üçlü': '3', 'Kupa Dörtlü': '4', 'Kupa Beşli': '5',
                                  'Kupa Altılı': '6',
                                  'Kupa Yedili': '7', 'Kupa Sekizli': '8', 'Kupa Dokuzlu': '9', 'Kupa Onlu': '10',
                                  'Kupa Vale': '11', 'Kupa Kız': '12', 'Kupa Papaz': '13',
                                  'Karo As': '1', 'Karo İkili': '2', 'Karo Üçlü': '3', 'Karo Dörtlü': '4', 'Karo Beşli': '5',
                                  'Karo Altılı': '6',
                                  'Karo Yedili': '7', 'Karo Sekizli': '8', 'Karo Dokuzlu': '9', 'Karo Onlu': '10',
                                  'Karo Vale': '11', 'Karo Kız': '12', 'Karo Papaz': '13',
                                  'Maça As': '1', 'Maça İkili': '2', 'Maça Üçlü': '3', 'Maça Dörtlü': '4', 'Maça Beşli': '5',
                                  'Maça Altılı': '6',
                                  'Maça Yedili': '7', 'Maça Sekizli': '8', 'Maça Dokuzlu': '9', 'Maça Onlu': '10',
                                  'Maça Vale': '11', 'Maça Kız': '12', 'Maça Papaz': '13',
                                  'Sinek As': '1', 'Sinek İkili': '2', 'Sinek Üçlü': '3', 'Sinek Dörtlü': '4', 'Sinek Beşli': '5',
                                  'Sinek Altılı': '6',
                                  'Sinek Yedili': '7', 'Sinek Sekizli': '8', 'Sinek Dokuzlu': '9', 'Sinek Onlu': '10',
                                  'Sinek Vale': '11', 'Sinek Kız': '12', 'Sinek Papaz': '13'}
                        if sayi == int(sözlük[kagit]):
                            print("Eşleşme bulundu.")
                            ayrı_list.append(kagit)
                            ek_list.remove(kagit)
                            deste.extend(ek_list)
                            ek_list.clear()
                            break
                        elif len(ek_list) == 13:
                            print("Eşleşme bulunamadı.")
                            ek_list.clear()
                            break
                        tuş = input()
                for i in range(0, len(ayrı_list)):
                    puan = int(sözlük[ayrı_list[i]])
                    if puan <= 10:
                        sayac += puan
                    else:
                        sayac += 10
                print("Bitti. Toplam puanınız:", sayac)
                print("Niyetiniz %", sayac, " ihtimalle gerçekleşecek.")
            devam = input("Niyetinizi tuttunuz mu(e/h)?")
            while (devam not in ['e', 'E', 'h', 'H']):
                print("Yanlış harf girdiniz.")
                devam = input("Niyetinizi tuttunuz mu?(e/h?")
                if devam == 'e' or devam == 'E':
                    break
                elif devam == 'h' or devam == 'H':
                    break
            while devam == 'h' or devam == 'H':
                devam = input("Bi zahmet tutuver! Tuttun mu?")
                while (devam not in ['e', 'E', 'h', 'H']):
                    print("Yanlış harf girdiniz.")
                    devam = input("Bi zahmet tutuver! Tuttun mu?")
            while devam == 'e' or devam == 'E':
                deste=deste_olustur()
                ek_list = []
                deger = 0
                puan = 0
                sayac = 0

                islemler()
                devam = input("Tekrar oynamak istiyor musunuz?(e/h)")
                while (devam not in ['e', 'E', 'h', 'H']):
                    print("Yanlış harf girdiniz.")
                    devam = input("Tekrar oynamak istiyor musunuz?(e/h)")
                    if devam in ['e', 'E', 'h', 'H']:
                        break
                if devam == 'e' or devam == 'E':
                    devam = input("Niyetinizi tuttunuz mu(e/h)?")
                    while (devam not in ['e', 'E', 'h', 'H']):
                        print("Yanlış harf girdiniz.")
                        devam = input("Niyetinizi tuttunuz mu?(e/h?")
                        if devam == 'e' or devam == 'E':
                            break
                        elif devam == 'h' or devam == 'H':
                            break
                    while devam == 'h' or devam == 'H':
                        devam = input("Bi zahmet tutuver! Tuttun mu?")
                        while (devam not in ['e', 'E', 'h', 'H']):
                            print("Yanlış harf girdiniz.")
                            devam = input("Bi zahmet tutuver! Tuttun mu?")
        elif secim==2:
            deste = ["Sinek As", "Sinek İkili", "Sinek Üçlü", "Sinek Dörtlü", "Sinek Beşli", "Sinek Altılı",
                     "Sinek Yedili",
                     "Sinek Sekizli", "Sinek Dokuzlu", "Sinek Onlu", "Sinek Vale", "Sinek Kız", "Sinek Papaz",
                     "Kupa As", "Kupa İkili",
                     "Kupa Üçlü", "Kupa Dörtlü", "Kupa Beşli", "Kupa Altılı", "Kupa Yedili", "Kupa Sekizli",
                     "Kupa Dokuzlu", "Kupa Onlu",
                     "Kupa Vale", "Kupa Kız", "Kupa Papaz", "Karo As", "Karo İkili", "Karo Üçlü", "Karo Dörtlü",
                     "Karo Beşli", "Karo Altılı",
                     "Karo Yedili", "Karo Sekizli", "Karo Dokuzlu", "Karo Onlu", "Karo Vale", "Karo Kız", "Karo Papaz",
                     "Maça As", "Maça İkili",
                     "Maça Üçlü", "Maça Dörtlü", "Maça Beşli", "Maça Altılı", "Maça Yedili", "Maça Sekizli",
                     "Maça Dokuzlu", "Maça Onlu", "Maça Vale",
                     "Maça Kız", "Maça Papaz"]

            dagitici = []  # dağıtıcı listesi
            oyuncu = []  # oyuncu listesi
            oyuncu_kart_top = 0
            dagitici_kart_top = 0

            def kart_dagit():
                for kart in range(1, 3):
                    kart = random.choice(deste)
                    deste.remove(kart)
                    dagitici.append(kart)
                for kart in range(1, 3):
                    kart = random.choice(deste)
                    deste.remove(kart)
                    oyuncu.append(kart)
            def puanHesap(liste):
                toplam = 0
                as_puan = 0
                degerler = {"Sinek As": "11", "Sinek İkili": "2", "Sinek Üçlü": "3", "Sinek Dörtlü": "4",
                            "Sinek Beşli": "5", "Sinek Altılı": "6", "Sinek Yedili": "7", "Sinek Sekizli": "8",
                            "Sinek Dokuzlu": "9", "Sinek Onlu": "10", "Sinek Vale": "10", "Sinek Kız": "10",
                            "Sinek Papaz": "10", "Kupa As": "11", "Kupa İkili": "2", "Kupa Üçlü": "3",
                            "Kupa Dörtlü": "4", "Kupa Beşli": "5", "Kupa Altılı": "6", "Kupa Yedili": "7",
                            "Kupa Sekizli": "8", "Kupa Dokuzlu": "9", "Kupa Onlu": "10", "Kupa Vale": "10",
                            "Kupa Kız": "10", "Kupa Papaz": "10", "Karo As": "11", "Karo İkili": "2",
                            "Karo Üçlü": "3", "Karo Dörtlü": "4", "Karo Beşli": "5", "Karo Altılı": "6",
                            "Karo Yedili": "7", "Karo Sekizli": "8", "Karo Dokuzlu": "9", "Karo Onlu": "10",
                            "Karo Vale": "10", "Karo Kız": "10", "Karo Papaz": "10", "Maça As": "11",
                            "Maça İkili": "2", "Maça Üçlü": "3", "Maça Dörtlü": "4", "Maça Beşli": "5",
                            "Maça Altılı": "6", "Maça Yedili": "7", "Maça Sekizli": "8", "Maça Dokuzlu": "9",
                            "Maça Onlu": "10", "Maça Vale": "10", "Maça Kız": "10", "Maça Papaz": "10"}
                for i in range(len(liste)):
                    toplam += int(degerler[liste[i]])
                    if liste[i] in ["Karo As", "Maça As", "Kupa As", "Sinek As"]:
                        as_puan += 1
                        toplam = toplam - 11
                        if toplam <= 10:
                            toplam += 11
                        else:
                            toplam += 1

                return toplam

            print("Blackjack simülasyonuna hoşgeldiniz.\nOyun Başlıyor!")
            devam = 'e'
            while devam == 'e' or devam == 'E':
                def deste_olustur():
                    simgeler = ["Kupa", "Karo", "Maça", "Sinek"]
                    sayılar = ["As", "İkili", "Üçlü", "Dörtlü", "Beşli", "Altılı", "Yedili", "Sekizli", "Dokuzlu",
                               "Onlu","Vale", "Kız", "Papaz"]
                    deste = []
                    for simge in simgeler:
                        for sayı in sayılar:
                            x = deste.append(simge + " " + sayı)
                    return deste
                deste_olustur()
                dagitici = []  # dağıtıcı listesi
                oyuncu = []  # oyuncu listesi
                oyuncu_kart_top = 0
                dagitici_kart_top = 0
                kart_dagit()
                oyuncu_kart_top = puanHesap(oyuncu)
                dagitici_kart_top = puanHesap(dagitici)
                print("Oyuncunun kartları:", oyuncu[0], ",", oyuncu[1], "(Oyuncunun puanı:", oyuncu_kart_top, ")")
                print("Dağıtıcının açık kartı:", dagitici[0])  # dağıtıcının diğer kartı kapalı

                while oyuncu_kart_top < 21 and dagitici_kart_top < 21:
                    devam = input("(K)ağıt mı, (P)as mı?:")
                    while devam not in ["k", "K", "P", "p"]:
                        print("Yanlış harf girdiniz.")
                        devam = input("(K)ağıt mı, (P)as mı?:")
                    while devam == "K" or devam == "k":
                        oyuncu.append(random.choice(deste))
                        oyuncu_kart_top = puanHesap(oyuncu)
                        print("Oyuncunun kartları:", oyuncu)
                        print("Oyuncunun puanı:", oyuncu_kart_top)
                        if oyuncu_kart_top >= 21:
                            break
                        devam = input("(K)ağıt mı, (P)as mı?:")
                    if devam == "p" or devam == "P":
                        print("Oyuncunun puanı:", oyuncu_kart_top, " Sıra dağıtıcıda.")
                        print("Dağıtıcının kartları:", dagitici)
                        print("Dağıtıcının puanı:", dagitici_kart_top)
                        while dagitici_kart_top < 17:
                            dagitici.append(random.choice(deste))
                            dagitici_kart_top = puanHesap(dagitici)
                            print("Dağıtıcının kartları:", dagitici)
                            print("Dağıtıcının puanı:", dagitici_kart_top)
                        break
                if dagitici_kart_top == 21 and oyuncu_kart_top != 21:
                    print("Dağıtıcının kağıtları:", dagitici)
                    print("BLACKJACK! Dağıtıcı kazandı.Oyuncu battı.")
                elif oyuncu_kart_top == 21 and dagitici_kart_top != 21:
                    print("BLACKJACK!Oyuncu kazandı.Dağıtıcı battı.")
                elif oyuncu_kart_top > 21:
                    print("Dağıtıcı Kazandı. Oyuncu battı.")
                elif dagitici_kart_top > 21:
                    print("Oyuncu kazandı. Dağıtıcı battı.")
                elif dagitici_kart_top > oyuncu_kart_top:
                    print("Dağıtıcı kazandı. Oyuncu battı.")
                elif oyuncu_kart_top > dagitici_kart_top:
                    print("Oyuncu kazandı. Dağıtıcı battı.")
                elif oyuncu_kart_top == dagitici_kart_top:
                    print("Oyun berabere!")

                devam = input("Tekrar oynamak istiyor musunuz? (e/h)")
                while (devam not in ['e', 'E', 'h', 'H']):
                    print("Yanlış harf girdiniz.")
                    devam = input("Tekrar oynamak istiyor musunuz?(e/h)")
                    if devam in ['e', 'E', 'h', 'H']:
                        break
                if devam == 'h' or devam == 'H':
                    break

        elif secim==3:
            cikis = input("Çıkmak istediğinizden emin misiniz(e/E/h/H)?:")
            if cikis=='e' or cikis=='E':
                print("Güle Güle!")
            while cikis not in ['e', 'E', 'h', 'H']:
                cikis = input("Hatalı veri girisi, lütfen tekrar giriniz:")

menu()