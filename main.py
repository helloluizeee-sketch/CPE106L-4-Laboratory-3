from menu import Menu, MenuItem, run_menu_system
from order_processing import OrderProcessor, run_order_system
from customer_management import CustomerManager, run_customer_system
from payment_delivery import PaymentDeliveryManager, run_payment_delivery_system

def main():
    print("Initializing Food Delivery Management System...\n")
    
    system_menu = Menu()
    processor = OrderProcessor()
    customer_manager = CustomerManager()
    payment_delivery_manager = PaymentDeliveryManager()

    while True:
        print("\n=== Food Delivery Management System ===")
        print("1. Manage Menu")
        print("2. Manage Customers")
        print("3. Process Orders")
        print("4. Payment & Delivery Checkout")
        print("5. Exit")
        
        choice = input("Select an option (1-5): ")
        
        if choice == '1':
            run_menu_system(system_menu)
            
        elif choice == '2':
            run_customer_system(customer_manager)
            
        elif choice == '3':
            run_order_system(processor, system_menu.items, customer_manager)
            
        elif choice == '4':
            run_payment_delivery_system(payment_delivery_manager)
            
        elif choice == '5':
            print("Shutting down system. Goodbye!")
            break
            
        else:
            print("Invalid selection.")

if __name__ == "__main__":
    main()