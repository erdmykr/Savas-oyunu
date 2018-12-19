#Author: Erdem1
import random
import time
from msvcrt import getch
from colorama import init, Fore
sleep = time.sleep
init(autoreset=False)


__import__('os').system("title Savaş oyunu")
class oyuncu:
    def __init__(self, isim):
        self.can = 60
        self.enerji = 50
        self.isim = isim
        self.sıhhiyeci_hakkı = 2
        self.sehitler = 0
        self.bombeleme = 1
        self.geri_çekilme = 1
    def saldır(self):
        if self.enerji != 0:
            print(Fore.RED)
            print("Saldırı sürüyor. Bekleyin.")
            for i in ".....................":
                time.sleep(0.1)
                print(i, flush=True, end="")
            print()
            secenekler = [1, 1, 2]
            secenek = random.choice(secenekler)
            print(Fore.RESET)

        else:
            print(Fore.RED)
            print("Enerjiniz bitti, geri çekilin!")
            print(Fore.RESET)
            return None
        self.enerji -= 5
        if secenek == 1:
            return True
        elif secenek == 2:
            return False
    def dinlenmek_için_geri_çekil(self, sure):
        if self.geri_çekilme:
            print(Fore.GREEN)
            print(f"Dinlenmek için {sure} dakika geri çekildiniz. (1 dakika: 1 saniye)")
            for i in sure*".":
                print(i, end="", flush=True)
                time.sleep(1)
            print()
            print("Savaş devam ediyor!")
            print(Fore.RESET)
            self.enerji += sure/2
            self.sıhhiyeci_hakkı +=1
        else:
            print("Çok fazla geri çekildiniz, artık yeter")
    def sıhhiyeci_gönder(self):
        print(Fore.MAGENTA)
        if self.sıhhiyeci_hakkı:
            self.sehitler -= 10
            print("Savaş bölgesine sıhhiyeci gönderildi")
            self.sıhhiyeci_hakkı -= 1
        else:
            print("Sıhhiyeciniz yok")
        print(Fore.RESET)

    
    def darbelen(self):
        b = random.randint(1, 15)
        self.sehitler += b
        self.can -= b
        if not self.can:
            return False
        return True
    
    def bombele(self):
            if self.bombeleme:
                b = random.randint(10, 20)
                self.sehitler += b
                self.can -= b
                self.bombeleme = 0
                return True
            return False

print(Fore.BLUE)
print(30*" "+"SAVAŞ OYUNU\n\n")
for i in range(1, 100):
    sleep(0.1)
    print("\r{}%".format(" "*36)+str(i), end="")
sleep(3)
print("\r{}%100".format(" "*36))



print(Fore.GREEN)
print("OYUN BAŞLIYOR!")
print(Fore.MAGENTA)
ism1 = input("1. oyuncu adı: ")
print(Fore.RESET)
print(Fore.BLUE)
ism2 = input("2. oyuncu adı: ")
print(Fore.RESET)
oyuncu1 = oyuncu(ism1)
oyuncu2 = oyuncu(ism2)
sira = 0
print(Fore.GREEN+"""
SEÇENEKLER:
[1] SALDIR
[2] SIHHİYECİ GÖNDER
[3] DİNLENMEK İÇİN GERİ ÇEKİL
[4] BOMBALA


""")
print(Fore.RESET)
while True:
    print(Fore.GREEN)
    print(50*"*")
    print(Fore.RESET)
    try:
        sira += 1
        if sira % 2 == 0:
            print(Fore.MAGENTA)
            print(f"Sıra: {oyuncu1.isim}")
            print(f"ASKER: {oyuncu1.can}, ENERJİ: {oyuncu1.enerji}, SIHHİYECİ: {oyuncu1.sıhhiyeci_hakkı}, ŞEHİTLER: {oyuncu1.sehitler}")
            print(Fore.RESET)
            wsira = "1"
        else:
            print(Fore.BLUE)
            print(f"Sıra: {oyuncu2.isim}")
            print(f"ASKER: {oyuncu2.can}, ENERJİ: {oyuncu2.enerji}, SIHHİYECİ: {oyuncu2.sıhhiyeci_hakkı}, ŞEHİTLER: {oyuncu2.sehitler}")
            print(Fore.RESET)
            wsira = "2"
        istek = getch()

        if istek == b"1":
            if wsira == "1":
                print(Fore.MAGENTA)
                a = oyuncu1.saldır()
                if a is True:
                    b = oyuncu2.darbelen()
                    if b is True:
                        print("Rakip darbelendi!")
                        print("ÖLDÜRÜLENLER TOPLAM: {}".format(oyuncu2.sehitler))
                    if b is False:
                        print(Fore.GREEN)
                        print("KAZANDINIZ, düşman ordusu dağıldı!")
                        print(Fore.RESET)
                        getch()
                        break
                if a is False:
                    print(Fore.RED)
                    print("Rakip kendini savundu!")
                    print(Fore.RESET)

                        
            else:
                print(Fore.BLUE)
                a = oyuncu2.saldır()
                if a == True:
                    b = oyuncu1.darbelen()
                    if b:
                        print("Rakip darbelendi!")
                        print("ÖLDÜRÜLENLER TOPLAM: {}".format(oyuncu1.sehitler))

                
                    else:
                        print(Fore.RED)
                        print("Rakibin ordusu dağıldı, savaşı kazandınız!")
                        getch()
                        break
                elif a == False:
                    print("Rakip kendini savundu!")
        

        elif istek == b"2":
            if wsira == "1":
                oyuncu1.sıhhiyeci_gönder()
            else:
                oyuncu2.sıhhiyeci_gönder()
        
        elif istek == b"3":
            if wsira == "1":
                print(Fore.MAGENTA)
                suree = input("Kaç dakika(saniye) geri çekileceksiniz?\n")
                try:
                    oyuncu1.dinlenmek_için_geri_çekil(int(suree))
                except:
                    print("Hatalı giriş yapıldı, sıranızı kaybettiniz :(")
                
            else:
                print(Fore.BLUE)
                suree = input("Kaç dakika(saniye) geri çekileceksiniz?\n")
                try:
                    oyuncu2.dinlenmek_için_geri_çekil(int(suree))
                except:
                    print("Hatalı giriş yapıldı, sıranızı kaybettiniz :(")
            print(Fore.RESET)

        elif istek == b"4":
            if wsira == "1":
                print(Fore.MAGENTA)
                bcd = oyuncu2.bombele()
                oyuncu1.enerji -= 10
                if bcd:
                    print("Düşamnlar bombalandı!")
                    print(f"ÖLDÜRÜLEN TOPLAM: {oyuncu2.sehitler}")
                else:
                    print("Bombanız yok!")
            else:
                print(Fore.BLUE)
                oyuncu2.enerji -= 10
                bcdf = oyuncu1.bombele()
                if bcdf:
                    print("Düşmanlar bombalandı!")
                    print(f"ÖLDÜRÜLEN TOPLAM: {oyuncu1.sehitler}")
                else:
                    print("Bombanız yok!")
            print(Fore.RESET)
    except Exception as e:
        print(Fore.RED)
        print("Bir hata oluştu")
    input()
    __import__("os").system("cls")
    print(Fore.RESET)