# kullanıcı ismi ve parola kontrolü programı
defkullanici = "username"
defparola = "123456"
kullanici = input("Kullanıcı adı: ")
parola = input("Parola: ")
if(defkullanici == kullanici) and (defparola == parola):
    print("siteye hosgeldiniz")
elif(defkullanici != kullanici) and (defparola == parola):
    print("kullanici adi yanlis")
elif(defkullanici == kullanici) and (defparola != parola):
    print("parola yanlis")
else:
    print("bilgiler hatali")
