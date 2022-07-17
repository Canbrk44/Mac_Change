import subprocess
import time


print("******Mac Değiştirici***********")

def Degistir():
    interface = input("İnterface Giriniz: ")
    mac_ad = input("Yeni Mac Adresini Giriniz : ")

    try:
        subprocess.call(["ifconfig",interface,"down"])
        subprocess.call(["ifconfig",interface,"hw","ether",mac_ad])
        subprocess.call(["ifconfig",interface,"up"])
        print(f"Mac Adresiniz {mac_ad} Olarak Değiştirilmiştir")
    except Exception as Hata:
        print("Mac Adresi Değiştirilmesi Sırasında Hata.. !")


Degistir()