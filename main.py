from rooms import EconomyRoom, BussinessRoom, FamilyRoom
from customer import Customer
from reservation import Reservation
from billing import Bill
rooms=[
    EconomyRoom(1,3000),
    EconomyRoom(2,3000),
    BussinessRoom(3,10000),
    FamilyRoom(4,5000)
]
customers = []
reservations = []
while True:
    print("\n===== HOTEL MANAGEMENT SYSTEM =====")
    print("1. View Rooms")
    print("2. Add Customer")
    print("3. Book Room")
    print("4. Check-out")
    print("5. Generate Bill")
    print("6. Exit")

    choice = input("Enter your choice: ")
    if choice == "1":
        print("\n===== ROOMS =====")
        for room in rooms:
            print(
                room.get_room_number(),
                "-",
                room.room_type(),
                "-",
                room.get_price(),
                "-",
                "Available" if room.is_available() else "Occupied"
            )
    elif choice == "2":
        name = input("Enter customer name: ")
        cnic = input("Enter CNIC: ")
        phone = input("Enter phone number: ")
        customer = Customer(name, cnic, phone)
        customers.append(customer)
        print("Customer added successfully!")

    elif choice == "3":
        if len(customers) == 0:
            print("Please add a customer first.")
        else:
            print("\nCustomers:")
            for i in range(len(customers)):
                print(i + 1, customers[i].name)
            customer_choice = int(input("Select customer: "))
            customer = customers[customer_choice - 1]
            room_number = int(input("Enter room number: "))
            nights = int(input("Enter number of nights: "))
            selected_room = None

            for room in rooms:
                if room.get_room_number() == room_number:
                    selected_room = room
            if selected_room is None:
                print("Room not found.")

            else:
                reservation = Reservation(
                    customer,
                    selected_room,
                    nights
                )
                reservation.book()
                reservations.append(reservation)
    elif choice == "4":
        if len(reservations) == 0:
            print("No reservations found.")

        else:
            for i in range(len(reservations)):
                print(
                    i + 1,
                    reservations[i].customer.name,
                    "- Room",
                    reservations[i].room.get_room_number()
                )
            reservation_choice = int(
                input("Select reservation: ")
            )
            reservation = reservations[reservation_choice - 1]
            reservation.checkout()

    elif choice == "5":
        if len(reservations) == 0:
            print("No reservations found.")
        else:
            for i in range(len(reservations)):
                print(
                    i + 1,
                    reservations[i].customer.name,
                    "- Room",
                    reservations[i].room.get_room_number()
                )
            reservation_choice = int(
                input("Select reservation: ")
            )
            reservation = reservations[reservation_choice - 1]
            bill = Bill(
                reservation.room,
                reservation.nights
            )
            bill.display_bill()
    elif choice == "6":
        print("Thank you for using Hotel Management System!")
        break
    else:

        print("Invalid choice!")
