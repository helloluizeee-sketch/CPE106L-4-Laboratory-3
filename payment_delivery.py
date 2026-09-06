from abc import ABC, abstractmethod
from datetime import datetime


class Payment(ABC):
    def __init__(self, amount: float):
        self._amount = amount
        self._timestamp = datetime.now()
        self._status = "Pending"

    @property
    def amount(self) -> float:
        return self._amount

    @property
    def status(self) -> str:
        return self._status

    @abstractmethod
    def process_payment(self) -> bool:
        pass


class CashPayment(Payment):
    def __init__(self, amount: float, cash_tendered: float):
        super().__init__(amount)
        self._cash_tendered = cash_tendered
        self._change = 0.0

    @property
    def change(self) -> float:
        return self._change

    def process_payment(self) -> bool:
        if self._cash_tendered >= self._amount:
            self._change = self._cash_tendered - self._amount
            self._status = "Completed"
            print(f"[Cash] Payment accepted. Total: PHP {self._amount:.2f} | Tendered: PHP {self._cash_tendered:.2f} | Change: PHP {self._change:.2f}")
            return True
        else:
            self._status = "Failed"
            print(f"[Cash] Insufficient cash. Total: PHP {self._amount:.2f} | Tendered: PHP {self._cash_tendered:.2f}")
            return False


class CardPayment(Payment):
    def __init__(self, amount: float, card_number: str, card_holder: str):
        super().__init__(amount)
        self.__card_number = card_number[-4:]
        self._card_holder = card_holder

    def process_payment(self) -> bool:
        if len(self.__card_number) == 4:
            self._status = "Completed"
            print(f"[Card] Payment of PHP {self._amount:.2f} approved for {self._card_holder} (Ending in **{self.__card_number}).")
            return True
        self._status = "Failed"
        return False


class EWalletPayment(Payment):
    def __init__(self, amount: float, account_number: str, provider: str = "GCash"):
        super().__init__(amount)
        self._account_number = account_number
        self._provider = provider

    def process_payment(self) -> bool:
        if len(self._account_number) >= 10:
            self._status = "Completed"
            print(f"[{self._provider}] Payment of PHP {self._amount:.2f} successful for account {self._account_number}.")
            return True
        self._status = "Failed"
        return False


class Delivery:
    VALID_STATUSES = ["Pending", "Preparing", "Out for Delivery", "Delivered", "Cancelled"]

    def __init__(self, delivery_id: str, address: str, rider_name: str = "Unassigned"):
        self.delivery_id = delivery_id
        self.address = address
        self.rider_name = rider_name
        self._status = "Pending"
        self._created_at = datetime.now()

    @property
    def status(self) -> str:
        return self._status

    def assign_rider(self, rider_name: str):
        self.rider_name = rider_name
        if self._status == "Pending":
            self._status = "Preparing"
        print(f"[Delivery] Rider '{self.rider_name}' assigned to delivery #{self.delivery_id}.")

    def update_status(self, new_status: str):
        if new_status in self.VALID_STATUSES:
            self._status = new_status
            print(f"[Delivery #{self.delivery_id}] Status updated to: {self._status}")
        else:
            print(f"[Delivery] Invalid status '{new_status}'. Allowed: {self.VALID_STATUSES}")


class Transaction:
    def __init__(self, transaction_id: str, order_id: str, payment: Payment, delivery: Delivery):
        self.transaction_id = transaction_id
        self.order_id = order_id
        self.payment = payment
        self.delivery = delivery
        self.timestamp = datetime.now()

    def get_details(self) -> str:
        return (
            f"--- Transaction Receipt [{self.transaction_id}] ---\n"
            f"Timestamp: {self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}\n"
            f"Order ID: {self.order_id}\n"
            f"Amount Paid: PHP {self.payment.amount:.2f}\n"
            f"Payment Method: {self.payment.__class__.__name__} ({self.payment.status})\n"
            f"Delivery Address: {self.delivery.address}\n"
            f"Delivery Status: {self.delivery.status} (Rider: {self.delivery.rider_name})\n"
            f"------------------------------------------------"
        )


class PaymentDeliveryManager:
    def __init__(self):
        self._transactions = []

    def checkout(self, order_id: str, payment: Payment, delivery: Delivery) -> bool:
        print(f"\nProcessing checkout for Order #{order_id}...")
        is_successful = payment.process_payment()

        if is_successful:
            delivery.update_status("Preparing")
            tx_id = f"TXN-{len(self._transactions) + 1:04d}"
            transaction = Transaction(tx_id, order_id, payment, delivery)
            self._transactions.append(transaction)
            print(f"Checkout successful. Transaction registered: {tx_id}")
            return True
        else:
            print("Payment rejected. Transaction aborted.")
            return False

    def view_completed_transactions(self):
        print("\n================ COMPLETED TRANSACTIONS ================")
        if not self._transactions:
            print("No completed transactions recorded.")
        for tx in self._transactions:
            print(tx.get_details())
        print("========================================================\n")


if __name__ == "__main__":
    manager = PaymentDeliveryManager()

    delivery1 = Delivery(delivery_id="DEL-101", address="123 Ayala Ave, Makati")
    delivery1.assign_rider("Carlos")
    cash_pay = CashPayment(amount=450.00, cash_tendered=500.00)
    manager.checkout(order_id="ORD-001", payment=cash_pay, delivery=delivery1)

    delivery2 = Delivery(delivery_id="DEL-102", address="456 BGC High Street, Taguig")
    delivery2.assign_rider("Marco")
    ewallet_pay = EWalletPayment(amount=820.50, account_number="09171234567")
    manager.checkout(order_id="ORD-002", payment=ewallet_pay, delivery=delivery2)

    delivery1.update_status("Delivered")

    manager.view_completed_transactions()