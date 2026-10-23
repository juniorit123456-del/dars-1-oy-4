class Athlete:
    def __init__(self, name, sport, age):
        self.name = name
        self.sport = sport
        self.age = age

    def show_info(self):
        print(f"Ism: {self.name} \nSport turi: {self.sport} \nYosh: {self.age}")

sport = Athlete('Ali', 'Futbol', 20)
sport.show_info()