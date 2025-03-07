#Bu Python dosyasında Inheritance konusu üzerine çalışma yaptım
# *Parent Class *Child Class


class calisan_genel_bilgi():
    guncel_yil = 2025
    sirket_domain = "mail.example.com"
    def __init__(self, ad, soyad, dogum_yili, is_baslama_tarihi):
        self.ad = ad
        self.soyad = soyad
        self.dogum_yili = dogum_yili
        self.ise_baslama_tarihi = is_baslama_tarihi
    
    def calisma_suresi(self):
        print(self.ise_baslama_tarihi)
        return self.guncel_yil - self.ise_baslama_tarihi

    
    def calisan_mail(self):
        return f'{self.ad}.{self.soyad}@{self.sirket_domain}'

class Muhendis(calisan_genel_bilgi):
    taban_maas = 35000 #muhendis taban maas
    def __init__(self,ad,soyad,dogum_yili,is_baslama_tarihi,calisma_alani):
        super().__init__(ad,soyad,dogum_yili,is_baslama_tarihi)
        self.calisma_alani = calisma_alani
    
    def calisan_bilgi(self):
        print(f'Adı: {self.ad}, Soyad: {self.soyad}, Calısma Alanı: {self.calisma_alani},meslek türü: mühendislik , mail adresi: {self.calisan_mail()}')

    def maas_hesaplama(self):
        return self.taban_maas + self.calisma_suresi() * (8.5)

class isci(calisan_genel_bilgi):
    taban_maas = 20000 #isci taban maas
    def __init__(self,ad,soyad,dogum_yili,is_baslama_tarihi,calisma_alani):
        super().__init__(ad,soyad,dogum_yili,is_baslama_tarihi)
        self.calisma_alani = calisma_alani
    
    def calisan_bilgi(self):
        print(f'Adı: {self.ad}, Soyad: {self.soyad}, Calısma Alanı: {self.calisma_alani},meslek türü: isci , mail adresi: {self.calisan_mail()}')

    def maas_hesaplama(self):
        return self.taban_maas + self.calisma_suresi() * (6.5)

class ogretmen(calisan_genel_bilgi):
    taban_maas = 30000 #öğretmenlik taban maas
    def __init__(self,ad,soyad,dogum_yili,is_baslama_tarihi,branch):
        super().__init__(ad,soyad,dogum_yili,is_baslama_tarihi)
        self.branch = branch
    
    def calisan_bilgi(self):
        print(f'Adı: {self.ad}, Soyad: {self.soyad}, Branş: {self.branch},meslek türü: öğretmenlik , mail adresi: {self.calisan_mail()}')

    def maas_hesaplama(self):
        return self.taban_maas + self.calisma_suresi() * (7)



muhendis1 = Muhendis("Ahmet", "Yağcı", 1978, 2019, "yapay zeka")


muhendis1.calisan_bilgi()

print(muhendis1.maas_hesaplama())
