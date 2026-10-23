class Player:
    def __init__(self, name, energy=100):
        self.name = name
        self.energy = energy

    def use_energy(self, amount) -> None:
        self.energy -= amount
        if self.energy < 0:
            self.energy = 0
        else:
            self.energy = 100

    def show_status(self) -> None:
        print(f"Oyinchi: {self.name} energiya: {self.energy}")

player = Player('Hero')
player.use_energy()
player.show_status()