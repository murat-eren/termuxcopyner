import os

os.system("clear")
os.system("")
os.system("mkdir /sdcard/herecopy/")
print("PROGRAMINIZI CIHAZININ DOSYA YONETICISINDEN 'herecopy' KLASORUNE KOPYALAYIN")
ad = input("Herecopy Klosöründeki Dosyanızın Tam Adını Girin  : ")
ad2 = input("Hangi  Adla Kaydedileycek  :  ")
os.system("cp /sdcard/herecopy/" + (ad ) + " /data/data/com.termux/files/home/" + (ad2))
print("İşlem Tamamlandı")

