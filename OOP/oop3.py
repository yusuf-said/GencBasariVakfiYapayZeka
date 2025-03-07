##multiple inheritancew, moethod overriding

class Insan:
    def __init__(self, isim, yas):
        self.isim = isim
        self.yas = yas

    def bilgileri_goster(self):
        return f"İsim: {self.isim}, Yaş: {self.yas}"

class Calisan:
    def __init__(self, sirket, maas):
        self.sirket = sirket
        self.maas = maas

    def calisan_bilgileri(self):
        return f"Şirket: {self.sirket}, Maaş: {self.maas} TL"

class Yazilimci(Insan, Calisan):
    def __init__(self, isim, yas, sirket, maas, programlama_dili):
        Insan.__init__(self, isim,yas)
        self.yas = yas
        Calisan.__init__(self, sirket, maas)
        self.programlama_dili = programlama_dili

    def calisan_bilgileri(self):
        return f"{self.bilgileri_goster()}, Çalıştığı Şirket: {self.sirket}, Maaş: {self.maas} TL, Programlama Dili: {self.programlama_dili}"

yazilimci = Yazilimci("Ahmet", 28, "TechCorp", 30000, "Python")
print(yazilimci.calisan_bilgileri())
