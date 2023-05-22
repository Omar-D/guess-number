from random import randint
num=0
while(True):
    value = randint(0, 100)
    print("Oyundan çıkmak istiyorsanız 'exit' yazınız")
    num=input("Lütfen 0 ile 100 arası tamin ettiğiniz sayıyı giriniz: ")
    try:
        if(num=="exit"):
            exit()
        elif(int(num)==value):
            print("Çok şanslısınız girdiğiniz sayı ile rastgele üretilen sayıyla aynıdır :)")
        elif(int(num)!=value):
            print("Maalesef tahmin edemediniz :(")
    except:
        print("1) Lütfen sayı giriniz")
        print("2) Girdiğiniz sayı TAM SAYI olacak")
