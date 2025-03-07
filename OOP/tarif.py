class Recipe():
    def __init__(self, dish_name, ingredient, instructions):
        self.dish_name = dish_name
        self.ingredient = ingredient
        self.instructions = instructions
        
    def icerik(self):
        return {
            "dishname": self.dish_name,
            "ingredient": self.ingredient,
            "instructions": self.instructions
        }

class Recipe_book():
    def __init__(self):
        self.all_dish = []  # Tüm tariflerin saklandığı liste
    
    def icerige_ekle(self, recipe):
        self.all_dish.append(recipe.icerik())
    
    def liste_yazdir(self):
        return self.all_dish

    def arama_yap(self, keyword):
        results = []  # Her arama için yeni bir sonuç listesi oluştur
        for recipe in self.all_dish:
            if keyword.lower() in recipe["dishname"].lower():
                results.append(recipe)  # Eşleşen tarifleri results listesine ekle

        if results:
            # Arama sonucunda bulunan tüm tariflerin detaylarını yazdır
            for result in results:
                print(f"Dish Name: {result['dishname']}")
                print(f"Ingredients: {', '.join(result['ingredient'])}")
                print(f"Instructions: {result['instructions']}\n")
        else:
            print("Not found")  # Eğer tarif bulunmadıysa kullanıcıya mesaj yazdır

# Örnek kullanım
Recipebook = Recipe_book()
recipe1 = Recipe("Pasta", ["Noodles", "Tomato Sauce"], "Boil and mix.")
recipe2 = Recipe("Pasta2", ["Noodles", "Tomato Sauce"], "Boil and mix.")
recipe3 = Recipe("Pasta3", ["Noodles", "Tomato Sauce"], "Boil and mix.")

Recipebook.icerige_ekle(recipe1)
Recipebook.icerige_ekle(recipe2)
Recipebook.icerige_ekle(recipe3)

Recipebook.arama_yap("Pasta")  # "Pasta" ile eşleşen tüm tarifleri gösterir
Recipebook.arama_yap("Pasta2")  # "Pasta2" ile eşleşen tüm tarifleri gösterir
Recipebook.arama_yap("Pizza")    # Tarif bulunmadıysa "Not found" yazdırır