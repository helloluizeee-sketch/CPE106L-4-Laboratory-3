#include <iostream>
#include <string>
#include <vector>
#include <memory>

class MenuItem {
protected:
    std::string name;
    double price;
public:
    MenuItem(std::string n, double p) : name(n), price(p) {}
    virtual ~MenuItem() = default;
    
    virtual void displayItem() const = 0; 
    
    std::string getName() const { return name; }
    double getPrice() const { return price; }
};

// Inheritance: Food Item
class Food : public MenuItem {
private:
    bool isVegan;
public:
    Food(std::string n, double p, bool vegan) : MenuItem(n, p), isVegan(vegan) {}
    void displayItem() const override {
        std::cout << "[Food] " << name << " - P" << price << (isVegan ? " (Vegan)" : "") << "\n";
    }
};

class Beverage : public MenuItem {
private:
    std::string size;
public:
    Beverage(std::string n, double p, std::string s) : MenuItem(n, p), size(s) {}
    void displayItem() const override {
        std::cout << "[Drink] " << name << " (" << size << ") - P" << price << "\n";
    }
};

// Integration Module
class MenuManagement {
private:
    std::vector<std::shared_ptr<MenuItem>> menu;
public:
    void addMenuItem(std::shared_ptr<MenuItem> item) {
        menu.push_back(item);
    }

    void showMenu() const {
        std::cout << "\n--- System Menu ---\n";
        for (const auto& item : menu) {
            item->displayItem();
        }
    }
};

int main() {
    MenuManagement menuModule;
    
    menuModule.addMenuItem(std::make_shared<Food>("Burger", 150.00, false));
    menuModule.addMenuItem(std::make_shared<Food>("Pizza (Slice)", 110.00, false));
    menuModule.addMenuItem(std::make_shared<Food>("Fries", 50.00, true));
    
    menuModule.addMenuItem(std::make_shared<Beverage>("Iced Tea", 65.00, "Large"));
    menuModule.addMenuItem(std::make_shared<Beverage>("Soda", 57.00, "Large"));
    
    menuModule.showMenu();
    return 0;
}