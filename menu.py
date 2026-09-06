# Abstract Base Class for Object-Oriented Design
class MenuItem:
    def __init__(self, name, price):
        self._name = name
        self._price = price
        
    def get_name(self):
        return self._name
        
    def get_price(self):
        return self._price
        
    def display_item(self):
        pass

# Inheritance: Food Item
class Food(MenuItem):
    def __init__(self, name, price, is_vegan=False):
        super().__init__(name, price)
        self._is_vegan = is_vegan
        
    def display_item(self):
        vegan_str = " (Vegan)" if self._is_vegan else ""
        print(f"[Food] {self._name} - P{self._price:.2f}{vegan_str}")

# Inheritance: Beverage Item
class Beverage(MenuItem):
    def __init__(self, name, price, size="Large"):
        super().__init__(name, price)
        self._size = size
        
    def display_item(self):
        print(f"[Drink] {self._name} ({self._size}) - P{self._price:.2f}")

class MenuManagement:
    def __init__(self):
        self._menu = []
        
    def add_menu_item(self, item):
        self._menu.append(item)
        
    def show_menu(self):
        print("\n--- System Menu ---")
        for item in self._menu:
            item.display_item()

if __name__ == "__main__":
    menu_module = MenuManagement()
    
    menu_module.add_menu_item(Food("Burger", 150.00, False))
    menu_module.add_menu_item(Food("Pizza (Slice)", 110.00, False))
    menu_module.add_menu_item(Food("Fries", 50.00, True))
    menu_module.add_menu_item(Beverage("Iced Tea", 65.00, "Large"))
    menu_module.add_menu_item(Beverage("Soda", 57.00, "Large"))
    
    menu_module.show_menu()