class Reservation:
    def __init__(self, customer, room, nights):
        self.customer = customer
        self.room = room
        self.nights = nights
        self.__available = True
    def is_available(self):
        return self.__available
    
    def book_room(self):
        self.__available = False
    
    def checkout_room(self):
        self.__available = True

    def book(self):
        if self.room.is_available():
            self.room.book_room()
            print("\nRoom booked successfully!")
            print("Customer:", self.customer.name)
            print("Room:", self.room.get_room_number())
            print("Nights:", self.nights)
        else:
            print("\nRoom is already occupied.")

    def checkout(self):
        self.room.checkout_room()
        print("\nCheck-out successful!")
        print("Customer:", self.customer.name)