class Customer:

    def __init__(self, name, cnic, phone):
        self.name = name
        self.cnic = cnic
        self.phone = phone

    def display_customer(self):
        print("Name:", self.name)
        print("CNIC:", self.cnic)
        print("Phone:", self.phone)