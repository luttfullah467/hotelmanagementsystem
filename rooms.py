from abc import ABC, abstractmethod
class Room(ABC):
    def __init__(self, room_number, price):
        self.__room_number = room_number
        self.__price = price
        self.__available = True

    def get_room_number(self):
        return self.__room_number

    def get_price(self):
        return self.__price

    def is_available(self):
        return self.__available

    def book_room(self):
        self.__available = False

    def checkout_room(self):
        self.__available = True

    @abstractmethod
    def room_type(self):
        pass

class EconomyRoom(Room):
    def room_type(self):
        return "Economy Room"

class BussinessRoom(Room):
    def room_type(self):
        return "Bussiness Room"

class FamilyRoom(Room):
    def room_type(self):
        return "Family Room"