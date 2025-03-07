class OgrenciBilgiSistemi:

    def __init__(self,ogrenci_ad="Ahmet", ogrenci_soyad="Taş", ogrenci_no=1231,tc_no="11111111",telefon_no='+90000000'):
        self._ogrenci_ad = ogrenci_ad
        self._ogrenci_soyad = ogrenci_soyad
        self._ogrenci_no = ogrenci_no
        self.__tc_no = tc_no
        self.__telefon_no = telefon_no
    
    def gizli_bilgi(self):
        return f''' Öğrenci ad: {self._ogrenci_ad},
        Öğrenci Soyad: {self._ogrenci_soyad},
        Öğrenci No: {self._ogrenci_no}
        Telefon No: {self.__tc_no}
        Öğrenci TC: {self.__telefon_no}
    '''
    def genel_bilgi(self):
        return f''' Öğrenci ad: {self._ogrenci_ad},
        Öğrenci Soyad: {self._ogrenci_soyad},
    '''

class MudurBilgi():
    def __init__(self,mudur_ad,mudur_soyad,sifre):
        self.mudur_ad = mudur_ad
        self.mudur_soyad = mudur_soyad
        self.mudur_sifre = sifre

class OgretmenBilgi():
    def __init__(self,ad,soyad,sifre):
        self.ad = ad
        self.soyad = soyad
        self.sifre = sifre
Mudur = MudurBilgi("mehmet","kasım",1234)
Ogretmen = OgretmenBilgi("tunc","kaya",1234)
Ogrenci = OgrenciBilgiSistemi()
Ogretmen.sifre      

##sisteme giriş

def sisteme_giris():
    print("Lütfen öğretmen ya da mudur oldugunuzu dogrulayınız ögretmen için 1'e  mudur için 2'ye basın")
    d = int(input())

    if d == 1:
        print("Tunc Kaya lütfen sifrenizi giriniz")
        passw = int(input("şifreyi giriniz"))
        if (passw == Ogretmen.sifre):
            print("sisteme basarıyla giriş yaptınız...")
            print("öğrenci bilgisine erişmek için lütfen bire basın")
            d = int(input())
            if d == 1:
                print(Ogrenci.genel_bilgi())
            else:
                print("yanlıs giriş yaptınız")
    elif d==2:
        print("mehmet kasım lutfen sifrenizi giriniz")

        passw = int(input("şifrenizi giriniz "))

        if passw == Mudur.mudur_sifre:
            print("sisteme basarı ile giriş yaptınız")

            print("Öğrenci Genel Bilgilerine erişmek için 1'e tüm bilgilere erişmek için 2'ye basınız")
            d = int(input("tercihinizi giriniz"))
            if d == 1:
                print(Ogrenci.genel_bilgi())
            elif d==2:
                print(Ogrenci.gizli_bilgi())
            else:
                print("yanlıs giriş yaptınız")

        else:
            print("şifreniz yanlış")
    else:
        print("yanlış giriş yaptınız")




sisteme_giris()


