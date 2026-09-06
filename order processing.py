class Order:
    def __init__(self, order_id, customer_name):
        self.order_id = order_id
        self.customer_name = customer_name
        self.items = {}
        self.__status = "Pending"

    def add_item(self, menu_item, quantity):
        self.items[menu_item] = self.items.get(menu_item, 0) + quantity
        print(f"Added {menu_item.name} (x{quantity}) to order {self.order_id}.")

    def remove_item(self, item_id):
        for menu_item in list(self.items):
            if menu_item.item_id == item_id:
                del self.items[menu_item]
                print(f"Removed item with ID: {item_id} from order {self.order_id}.")
                return
        print("Item ID not found in this order.")

    def get_total_price(self):
        return sum(item.get_price() * qty for item, qty in self.items.items())

    def get_status(self):
        return self.__status

    def advance_status(self):
        flow = ["Pending", "Confirmed", "Preparing", "Out for Delivery", "Completed"]
        if self.__status == "Completed":
            print(f"Order {self.order_id} is already Completed.")
        else:
            self.__status = flow[flow.index(self.__status) + 1]
            print(f"Order {self.order_id} status updated to: {self.__status}")

    def cancel(self):
        if self.__status == "Completed":
            print(f"Order {self.order_id} is already completed and cannot be cancelled.")
        else:
            self.__status = "Cancelled"
            print(f"Order {self.order_id} has been cancelled.")

    def display_info(self):
        print(f"\n[{self.order_id}] Customer: {self.customer_name} | Status: {self.__status}")
        if not self.items:
            print("  (No items yet)")
        for item, qty in self.items.items():
            print(f"  {item.name} x{qty} - ₱{item.get_price() * qty:.2f}")
        print(f"  TOTAL: ₱{self.get_total_price():.2f}")


class OrderProcessor:
    def __init__(self):
        self.orders = []

    def create_order(self, order_id, customer_name):
        order = Order(order_id, customer_name)
        self.orders.append(order)
        print(f"Successfully created order {order_id} for {customer_name}!")
        return order

    def find_order(self, order_id):
        for order in self.orders:
            if order.order_id == order_id:
                return order
        print("Order ID not found.")
        return None

    def display_all_orders(self):
        active = [o for o in self.orders if o.get_status() != "Completed"]
        print("\n--- No active orders. ---" if not active else "\n=== Active Orders ===")
        for order in active:
            order.display_info()

    def display_completed_transactions(self):
        done = [o for o in self.orders if o.get_status() == "Completed"]
        print("\n--- No completed transactions yet. ---" if not done else "\n=== Completed Transactions ===")
        for order in done:
            order.display_info()


if __name__ == "__main__":
    from menu_management_module import MenuItem

    sample_menu_items = [
        MenuItem("D1", "Chicken Adobo", 185.00, "Classic Filipino braised chicken"),
        MenuItem("D2", "Sinigang na Baboy", 220.00, "Sour pork stew with vegetables"),
        MenuItem("D3", "Iced Tea", 45.00, "House-blend iced tea"),
    ]
    processor = OrderProcessor()

    while True:
        print("\n=== Order Processing System ===")
        print("1. Create Order  2. Add Item  3. Remove Item  4. View Active Orders")
        print("5. Advance Status  6. Cancel Order  7. View Completed  8. Exit")
        choice = input("Enter your choice (1-8): ")

        if choice == '1':
            oid = input("Order ID: ")
            name = input("Customer Name: ")
            processor.create_order(oid, name)

        elif choice == '2':
            order = processor.find_order(input("Order ID: "))
            if order:
                for item in sample_menu_items:
                    item.display_info()
                item_id = input("Item ID to add: ")
                match = next((i for i in sample_menu_items if i.item_id == item_id), None)
                if match:
                    try:
                        order.add_item(match, int(input("Quantity: ")))
                    except ValueError:
                        print("Error: enter a valid whole number.")
                else:
                    print("Item ID not found in menu.")

        elif choice == '3':
            order = processor.find_order(input("Order ID: "))
            if order:
                order.remove_item(input("Item ID to remove: "))

        elif choice == '4':
            processor.display_all_orders()

        elif choice == '5':
            order = processor.find_order(input("Order ID: "))
            if order:
                order.advance_status()

        elif choice == '6':
            order = processor.find_order(input("Order ID: "))
            if order:
                order.cancel()

        elif choice == '7':
            processor.display_completed_transactions()

        elif choice == '8':
            print("Exiting Order Processing System...")
            break

        else:
            print("Invalid choice. Please select a number from 1 to 8.")
