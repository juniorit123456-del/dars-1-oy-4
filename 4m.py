class Ticket:
    def __init__(self, movie, price, count):
        self.movie = movie
        self.price = price
        self.count = count

    def jami(self):
        return self.price * self.count

    def show_info(self):
        print(f"Film: {self.movie}, Umumiy xarajat: {self.jami()}")

ticket = Ticket('Avatar', 40000, 3)
print(ticket.jami())