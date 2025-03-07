##absraction alakalı
from abc import ABC, abstractmethod

class Tiyatro_oyunu(ABC):
    def __init__(self):
        self.oyun_adi = "Küçük Burjuvalar"
        self.yazar = "Maksim Gorki"
        self.salon = "Harbiye"

    
    def oyun_bilgi(self):
        return f'''Oyun adı: {self.oyun_adi},
        Oyun Yazarı: {self.yazar},
        Salon: {self.salon}'''
    @abstractmethod
    def karakter_ozellik(self):
        pass


#karakter özellikleri
class KucukBurjuvalar(Tiyatro_oyunu):
    def __init__(self):
        super().__init__()
    def karakter_ozellik(self):
        return """Maksim Gorki'nin "Küçük Burjuvalar" adlı tiyatro oyunu, Çarlık Rusyası'nda farklı toplumsal sınıflardan gelen karakterlerin yaşamlarını ve aralarındaki çatışmaları konu alır."""
        

class Bessemyonov(Tiyatro_oyunu):
    def __init__(self):
        super().__init__()
    def karakter_ozellik(self):
        return "Bessemyonov, 58 yaşında, hali vakti yerinde bir küçük burjuva; bir boya atölyesinin şefi. Geleneklerine bağlı, otoriter bir baba figürüdür"
    
class Ivanovna(Tiyatro_oyunu):
    def __init__(self):
        super().__init__()
    def karakter_ozellik(self):
        return "Ivanovna, 52 yaşında, Bessemyonov'un eşi. Aile içindeki huzuru korumaya çalışan, uzlaştırıcı bir karakterdir. "
    
kucuk_burjuva = KucukBurjuvalar()   
print(kucuk_burjuva.oyun_bilgi())
bessemyonov = Bessemyonov()
print(bessemyonov.karakter_ozellik())
