class Bill:
    def __init__(self, room, nights,price):
        self.room = room
        self.nights = nights
        self.__price = price

    def calculate_bill(self):
        total = self.room.get_price() * self.nights
        return total
    
    def get_price(self):
        return self.__price

    def display_bill(self):
        total = self.calculate_bill()
        print("\n===== BILL =====")
        print("Room:", self.room.get_room_number())
        print("Room Type:", self.room.room_type())
        print("Price per Night:", self.room.get_price())
        print("Nights:", self.nights)
        print("Total Bill:", total)