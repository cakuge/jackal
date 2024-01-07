import os
import colorama
import sys

# -*- coding: utf-8 -*-



def main():
    def sekilli_yazi(metin):
     print(colorama.Fore.BLUE + metin + colorama.Fore.RESET)

    sekilli_yazi("""
__________________________________________
/_____/_____/_____/_____/_____/_____/_____/
     __               __           .__     
    |__|____    ____ |  | _______  |  |    
    |  \__  \ _/ ___\|  |/ /\__  \ |  |    
    |  |/ __ \  \___|    <  / __ \|  |__  
/\__|  (____  /\___  >__|_ \(____  /____/  
\______|    \/     \/     \/     \/        
                                                    
 __________________________________________
/_____/_____/_____/_____/_____/_____/_____/
""")
    print(colorama.Fore.YELLOW + "Hoşgeldiniz, aktive etmeden önce lütfen readme.txt yi okuyunuz." + colorama.Fore.RESET)
    print(colorama.Fore.YELLOW + "Devam etmek için [y] tuşuna basın ya da [n] yazın." + colorama.Fore.RESET)
    devam = input()
    if devam == "y":

        girdiler = []
        while True:
            girdi = input(colorama.Fore.RED + "Etiket Giriniz: " + colorama.Fore.RESET)
            girdiler.append(girdi)
            print(colorama.Fore.RED + "Girilen etiketler:", colorama.Fore.GREEN + ", ".join(girdiler) + colorama.Fore.RESET)
            devam = input("Devam etmek için (y) durdurmak için (n) giriniz: ")
            if devam == "n":
                print(colorama.Fore.YELLOW + "Dosyanız oluşturuldu." + colorama.Fore.RESET)
                break

        with open("pws.txt", "r") as f:
            pws = f.read()

        with open("passwords.txt", "w") as f:
            for girdi in girdiler:
                f.write(girdi + "\n")
                f.write(girdi + "." +"\n")
                f.write("."+girdi +"\n")
                f.write(girdi.upper() + "\n")
                f.write(girdi.capitalize())
                for satir in pws.splitlines():
                        f.write(girdi + "\n")
                        f.write(satir + girdi + "\n")
                        f.write(satir + girdi + "." +"\n")
                        f.write(satir + girdi.capitalize() + "\n")
                        f.write(girdi + satir + "\n")
                        f.write(girdi + satir + "." + "\n")
                        f.write(girdi.capitalize() + "" + satir + "\n")
                        f.write(girdi.upper() + satir + "\n")
                        f.write(girdi[0:1] + girdi[1].upper() + girdi[2].upper() + girdi[3:] + "\n")
                        f.write(girdi[0:1] + girdi[1].upper() + girdi[2].upper() + girdi[3:] +satir +"\n")
                        f.write(satir + girdi[0:1] + girdi[1].upper() + girdi[2].upper() + girdi[3:] + "\n")
                        f.write(girdi[0:1] + girdi[1].upper() + girdi[2:] + "\n")
                        f.write(girdi[0:1] + girdi[1].upper() + girdi[2:] + "." +"\n")
                        f.write(girdi[0:1] + girdi[1].upper() + girdi[2:] + satir + "\n")
                        f.write(girdi[0:1] + girdi[1].upper() + girdi[2:] + satir + "." +"\n")
                        f.write(satir + girdi[0:1] + girdi[1].upper() + girdi[2:] + "\n")
                        f.write(satir + girdi[0:1] + girdi[1].upper() + girdi[2:] + "." +"\n")
                        break
        dosya_yolu = os.path.join(os.getcwd(), "passwords.txt")
        print(os.path.dirname(dosya_yolu))               
    else:
        print(colorama.Fore.RED + "Çıkış Yapılıyor." + colorama.Fore.RESET)
        return
    os.system("python controller.py")
if __name__ == "__main__":
    main()
    print(colorama.Fore.GREEN + "Çıkış Yapıldı." + colorama.Fore.RESET)