import os
import colorama
import sys

# -*- coding: utf-8 -*-

if os.name == "nt":
        os.system("cls")
else:
        os.system("clear")

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
    print(colorama.Fore.YELLOW + "* Welcome, please readme first read readme.txt" + colorama.Fore.RESET)
    print(colorama.Fore.YELLOW + "* If you want to add some more special things, you can edit pws.txt file." + colorama.Fore.RESET)
    print(colorama.Fore.YELLOW + "* Enter tags of at least 3 characters." + colorama.Fore.RESET)
    print(colorama.Fore.YELLOW + "* Press the [y] key to continue, if you do not want to continue, type [n]." + colorama.Fore.RESET)
    devam = input()
    if devam == "y":

        girdiler = []
        while True:
            girdi = input(colorama.Fore.RED + "Enter Tag: " + colorama.Fore.RESET)
            girdiler.append(girdi)
            print(colorama.Fore.RED + "Entered Tags:", colorama.Fore.GREEN + ", ".join(girdiler) + colorama.Fore.RESET)
            devam = input(colorama.Fore.YELLOW + "Press the [y] key to continue, if you do not want to continue, type [n]. " + colorama.Fore.RESET)
            if devam == "n":
                print(colorama.Fore.YELLOW + "Your files is created." + colorama.Fore.RESET)
                print(colorama.Fore.YELLOW + "Good Luck." + colorama.Fore.RESET)
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
                        
        dosya_yolu = os.path.join(os.getcwd(), "passwords.txt")
        print(os.path.dirname(dosya_yolu))               
    else:
        print(colorama.Fore.RED + "## Exit ##" + colorama.Fore.RESET)
        devam == False
        return
    os.system("python controller.py")
    print("Your file is created.")
    print(colorama.Fore.GREEN + "### Exit ###" + colorama.Fore.RESET)
    print(colorama.Fore.YELLOW + "Good Luck." + colorama.Fore.RESET)
if __name__ == "__main__":
     main()