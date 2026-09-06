class Customer:
    def __init__(self, customer_id, name, email, phone):
        self.__customer_id = customer_id
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


if __name__ == "__main__":
    manager = CustomerManager()
    c1 = Customer("CUST-001", "Abi Sala", "abisala@example.com", "09173676789")
    manager.register_customer(c1)
    c1.display_customer_info()