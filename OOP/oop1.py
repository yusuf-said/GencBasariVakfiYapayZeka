#class ve __initin nasıl çalıstgını anlamak için oluşturdugum örnekler 


class Kitaplar():
    def __init__(self,yazar,kitap_adi,turu,isbn,basim_yili):
        self.yazar = yazar
        self.kitap_adi = kitap_adi
        self.tur = turu
        self.isbn = isbn
        self.basim_yili = basim_yili

    def show(self):
        return f'''Kitap Yazarı: {self.yazar},
        Kitap adı: {self.kitap_adi},
        Kitap Türü: {self.tur}
        Kitap Basım Yılı: {self.basim_yili},
        Kitap ISBN: {self.isbn}
        '''
    def tanitim_yazisi_ekle(self,bilgi)->str:
        self.bilgi = bilgi
        #print(self.bilgi)

    def show_tanitim(self):
        return self.bilgi




###kitap kayıt kısmı input alarak kullanıcıdan kitap hakkında bilgi isteyeceğiz

kitap_yazar = input("yazar adı: ")
kitap_adi = input("kitap adı: ")
kitap_turu = input("kitap turu: ")
kitap_isbn = input("kitap isbn: ")
kitap_basim = int(input("basım yılı: "))

#kitap_tanitim_yazisi = input("kitap tanıtım yazısı") # cok uzun yazılarda sıkıntı oldugu için değişkenle ile alacagım

kitap_tanitim_yazisi = ''''''
#classı instance olarak alacağız

new_kitap = Kitaplar(kitap_yazar,kitap_adi,kitap_turu,kitap_isbn,kitap_basim)

new_kitap.tanitim_yazisi_ekle(kitap_tanitim_yazisi)

print(new_kitap.show()) #return ettiğmiz için print kullanmamız gerekiyor
print(new_kitap.show_tanitim)




