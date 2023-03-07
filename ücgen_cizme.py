sayi= int(input("Sayı giriniz ="))
for i in range (sayi):
    if i==(sayi-1):
        print(" "*(sayi-i)+"/"+("_"*2*i)+"\\")
    else:
        print(" "*(sayi-i)+"/"+(" "*2*i)+"\\")