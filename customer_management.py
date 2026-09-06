class Customer:
    def __init__(self, customer_id, name, email, phone):
        self.__customer_id = customer_id
        self.__name = name  # <-- Crucial so it doesn't stay empty!
        self.__email = email
        self.__phone = phone
        self.__order_history = []
    
    def get_customer_id(self):  
        return self.__customer_id

    def get_name(self):
        return self.__name

    def get_email(self):
        return self.__email

    def get_phone(self):
        return self.__phone

    def update_contact_info(self, email, phone):
        self.__email = email
        self.__phone = phone
        print(f"Updated contact information for {self.__name}.")

    def add_order_to_history(self, order):
        self.__order_history.append(order)

    def display_customer_info(self):
        print(f"Customer ID: {self.__customer_id}")
        print(f"Name: {self.__name}")
        print(f"Email: {self.__email}")
        print(f"Phone: {self.__phone}")
        print(f"Total Orders: {len(self.__order_history)}")


class CustomerManager:
    def __init__(self):
        self.customers = {}

    def register_customer(self, customer):
        if customer.get_customer_id() in self.customers:
            print("Customer already exists!")
        else:
            self.customers[customer.get_customer_id()] = customer
            print(f"Customer {customer.get_name()} successfully registered.")

    def find_customer(self, customer_id):
        return self.customers.get(customer_id, None)

def run_customer_system(manager):
    while True:
        print("\n=== Customer Management System ===")
        print("1. Register Customer")
        print("2. View Customer Info")
        print("3. Update Contact Info")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            cid = input("Customer ID: ")
            name = input("Name: ")
            email = input("Email: ")
            phone = input("Phone: ")
            new_customer = Customer(cid, name, email, phone)
            manager.register_customer(new_customer)

        elif choice == '2':
            cid = input("Enter Customer ID to search: ")
            customer = manager.find_customer(cid)
            if customer:
                customer.display_customer_info()
            else:
                print("Customer ID not found.")

        elif choice == '3':
            cid = input("Enter Customer ID to update: ")
            customer = manager.find_customer(cid)
            if customer:
                new_email = input("New Email: ")
                new_phone = input("New Phone: ")
                customer.update_contact_info(new_email, new_phone)
            else:
                print("Customer ID not found.")

        elif choice == '4':
            print("Returning to Main Menu...")
            break

        else:
            print("Invalid choice. Please select a number from 1 to 4.")

if __name__ == "__main__":
    manager = CustomerManager()
    run_customer_system(manager)