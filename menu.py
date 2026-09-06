class MenuItem:
    def __init__(self, item_id, name, price, description):
        self.item_id = item_id
        self.name = name
        self.__price = price
        self.description = description

    def get_price(self):
        return self.__price

    def set_price(self, new_price):
        if new_price > 0:
            self.__price = new_price
        else:
            print("Invalid price update.")

    def display_info(self):
        print(f"[{self.item_id}] {self.name} - ₱{self.__price:.2f}: {self.description}")

class Menu:
    def __init__(self):
        self.items = []

    def add_item(self, menu_item):
        self.items.append(menu_item)
        print(f"Successfully added {menu_item.name} to the menu!")

    def remove_item(self, item_id):
        for item in self.items:
            if item.item_id == item_id:
                self.items.remove(item)
                print(f"Removed item with ID: {item_id}")
                return
        print("Item ID not found.")

    def display_menu(self):
        if not self.items:
            print("\n--- The menu is currently empty. ---")
        else:
            print("\n=== Current Menu ===")
            for item in self.items:
                item.display_info()
            print("--------------------")

if __name__ == "__main__":
    startup_menu = Menu()

def run_menu_system(startup_menu):
    while True:
        print("\n=== Menu Management System ===")
        print("1. View Menu")
        print("2. Add Menu Item")
        print("3. Remove Menu Item")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            startup_menu.display_menu()
                
        elif choice == '2':
            print("\n--- Add New Item ---")
            item_id = input("Enter Item ID (e.g., D1): ").strip().upper()
            name = input("Enter Item Name: ")
            
            try:
                price = float(input("Enter Price in Pesos (e.g., 185.00): "))
                desc = input("Enter Description: ")
                new_item = MenuItem(item_id, name, price, desc)
                startup_menu.add_item(new_item)
            except ValueError:
                print("Error: Please enter a valid number for the price.")
                
        elif choice == '3':
            item_id = input("Enter the ID of the item to remove (e.g., D1): ").strip().upper()
            startup_menu.remove_item(item_id)
            
        elif choice == '4':
            print("Exiting Menu Management System...")
            break
            
        else:
            print("Invalid choice. Please select a number from 1 to 4.")