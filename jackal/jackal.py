import os
# encoding:utf-8
def main():
    print("Hoşgeldiniz. Programı çalıştırmadan önce lütfen readme.txt yi okuyunuz. programdan çıkmak için exit yazmanız yeterlidir. ")
    print("Devam etmek için y tuşuna basın.")
    devam = input()
    if devam == "y":

        girdiler = []
        while True:
            girdi = input("Etiket Giriniz: ")
            girdiler.append(girdi)
            print("Girilen girdiler:", girdiler)
            devam = input("Devam etmek için (y) durdurmak için (n) giriniz: ")
            if devam == "n":
               print("Dosya şu dizinde oluşturuldu:", os.path.dirname("yeni_pws.txt"))
            break

        with open("pws.txt", "r") as f:
            pws = f.read()

        with open("passwords.txt", "w") as f:
            for girdi in girdiler:
                f.write(girdi + "\n")
                f.write(girdi + "." +"\n")
                f.write("."+girdi +"\n")
                f.write(girdi.upper() + "\n")
                for satir in pws.splitlines():
                    if len(girdi) > 2:
                        f.write(girdi[0:1] + girdi[1].upper() + girdi[2].upper() + girdi[3:] + "\n")
                        f.write(girdi[0:1] + girdi[1].upper() + girdi[2].upper() + girdi[3:] +satir +"\n")
                        f.write(satir + girdi[0:1] + girdi[1].upper() + girdi[2].upper() + girdi[3:] + "\n")
                    else:
                        f.write(girdi + "\n")
                        f.write(satir + girdi + "\n")
                        f.write(satir + girdi + "." +"\n")
                        f.write(satir + girdi.capitalize() + "\n")
                        f.write(girdi + satir + "\n")
                        f.write(girdi + satir + "." + "\n")
                        f.write(girdi.capitalize() + "" + satir + "\n")
                        f.write(girdi.upper() + satir + "\n")
                    if len(girdi) > 1:
                        f.write(girdi[0:1] + girdi[1].upper() + girdi[2:] + "\n")
                        f.write(girdi[0:1] + girdi[1].upper() + girdi[2:] + "." +"\n")
                        f.write(girdi[0:1] + girdi[1].upper() + girdi[2:] + satir + "\n")
                        f.write(girdi[0:1] + girdi[1].upper() + girdi[2:] + satir + "." +"\n")
                        f.write(satir + girdi[0:1] + girdi[1].upper() + girdi[2:] + "\n")
                        f.write(satir + girdi[0:1] + girdi[1].upper() + girdi[2:] + "." +"\n")
                    else:
                        f.write(girdi + "\n")
                        f.write(satir + girdi + "\n")
                        f.write(satir + girdi + "." +"\n")
                        f.write(satir + girdi.capitalize() + "\n")
                        f.write(girdi + satir + "\n")
                        f.write(girdi + satir + "." + "\n")
                        f.write(girdi.capitalize() + "" + satir + "\n")
                        f.write(girdi.upper() + satir + "\n")
                        
    else:
        return

if __name__ == "__main__":
    main()