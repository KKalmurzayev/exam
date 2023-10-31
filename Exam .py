
# import random

# while True:
#     user = input(" Здравствуйте, выберите один вариант камень, ножницу или бумагу: ")
#     variant = ["камень", "ножницы" , "бумага"]
#     computer = random.choice(variant)
   

#     print(f"Пользователь выбирает {user}, компьютер {computer}")
#     if user==computer:
#         print( "Ничья! Неплохо выбраны одинаковые варианты")
#     elif user=="камень":
#         if computer == "ножницы":
#             print("Камень бьет ножницы, Поздравляю, ВЫ ВЫЙГРАЛИ!")
#         else:
#             print("Бумага оборачивает камень, К сожелению, ВЫ ПРОИГРАЛИ!")
#     elif user=="ножницы":
#         if computer == "бумага":
#             print("Ножница режет бумагу, Поздравляю, ВЫ ВЫЙГРАЛИ!")
#         else:
#             print("Камень бьет ножницы, К сожелению, ВЫ ПРОИГРАЛИ1")
#     elif user=="бумага":
#         if computer == "камень":
#             print("Бумага оборачивает камень, Поздравляю, ВЫ ВЫЙГРАЛИ!")
#         else:
#             print("Бумага оборачивает камень, К сожелению, ВЫ ПРОИГРАЛИ!")
#         break
#     play_again = " "
#     play_again = input('д/н:')
#     if play_again.lower() != "д"
#         break
        



class Pizza:
    def __init__(self, contain, soys, sweet):
        self.contain = contain
        self.soys = soys
        self.sweet = sweet
  
    def ready(self):
        print("Подготовка теста")

    def collect(self):
        print("Собрать ингредиенты")
    
    def bake(self):
        print("Испечь пиццу")

    def сut(self):
        print("Прорезать пиццу")   

    def packed(self):
        print("Упоковать пиццу")   
  
    def info(self):  
        print("Тесто: " + str(self.contain))
        print("Соус: " + str(self.soys))
        print("Начинка: " + str(self.sweet))


class Peperony(Pizza):
    def __init__(self, contain, soys, sweet, pepper):
        super().__init__(contain, soys, sweet,)
        self.pepper = pepper
    def set_info(self, tomato):
        self.tomato = tomato

    def get_info(self):
        print('Дополнительный ингредиент'  + {self.tomato})
        

class Barbequ(Pizza):
    def __init__(self, contain, soys, sweet, mashroom):
        super().__init__(contain, soys, sweet,)
        self.mashroom = mashroom
        
    def set_info(self, cucumber):
        self.cucumber = cucumber

    def get_info(self):
        print('Дополнительный ингредиент'  + {self.cucumber})


class Gifts(Pizza):
    def __init__(self, contain, soys, sweet, oliva ):
        super().__init__(contain, soys, sweet,)
        self.oliva = oliva
        
        
    def set_info(self, nut):
        self.nut = nut

    def get_info(self):
        print('Дополнительный ингредиент'  + {self.nut})


    
