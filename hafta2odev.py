import requests

api_adresi = "https://reqres.in/api/users"

def kullanicilari_api_den_al():
    cevap = requests.get(api_adresi)
    return cevap.json()["data"]

def kullanicilari_goster(kullanicilar):
    print("\nGüncellenmiş Kullanıcı Listesi:")
    for kullanici in kullanicilar:
        print(f'ID: {kullanici["id"]} - Ad: {kullanici["first_name"]} {kullanici["last_name"]}')

def yeni_kullanici_ekle(kullanicilar, ad, meslek):
    yeni_id = max([k["id"] for k in kullanicilar]) + 1 if kullanicilar else 1
    yeni_kullanici = {"id": yeni_id, "first_name": ad, "last_name": "", "job": meslek}
    kullanicilar.append(yeni_kullanici)
    print(f"\nYeni kullanıcı eklendi: {yeni_kullanici}")
    return kullanicilar

def kullanici_guncelle(kullanicilar, kullanici_id, yeni_ad, yeni_meslek):
    for kullanici in kullanicilar:
        if kullanici["id"] == kullanici_id:
            kullanici["first_name"] = yeni_ad
            kullanici["job"] = yeni_meslek
            print(f"\nKullanıcı güncellendi: {kullanici}")
            return kullanicilar
    print("\nKullanıcı bulunamadı!")
    return kullanicilar

def kullanici_sil(kullanicilar, kullanici_id):
    yeni_liste = [k for k in kullanicilar if k["id"] != kullanici_id]
    if len(yeni_liste) != len(kullanicilar):
        print(f"\nKullanıcı {kullanici_id} silindi.")
        return yeni_liste
    print("\nKullanıcı bulunamadı!")
    return kullanicilar

kullanicilar = kullanicilari_api_den_al()
print("İlk Kullanıcı Listesi:")
kullanicilari_goster(kullanicilar)

kullanicilar = yeni_kullanici_ekle(kullanicilar, "Ali", "Öğrenci")
kullanicilar = kullanici_guncelle(kullanicilar, 2, "Mehmet", "Mühendis")
kullanicilar = kullanici_sil(kullanicilar, 2)

kullanicilari_goster(kullanicilar)
