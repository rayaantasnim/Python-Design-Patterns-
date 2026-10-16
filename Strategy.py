from abc import ABC, abstractmethod

# ============================================================
# Step 1: Strategy Interface
# ============================================================
class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

# ============================================================
# Step 2: Concrete Strategies
# ============================================================
class BkashPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"✅ Paid {amount} BDT using Bkash.")

class NagadPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"✅ Paid {amount} BDT using Nagad.")

class CardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"✅ Paid {amount} BDT using Credit/Debit Card.")

class CashPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"✅ Paid {amount} BDT using Cash.")

# ============================================================
# Step 3: Context Class
# ============================================================
class PaymentContext:
    def __init__(self, strategy):
        self.strategy = strategy

    def set_strategy(self, strategy):
        """Change the payment method."""
        self.strategy = strategy

    def checkout(self, amount):
        print(f"\nProcessing payment of {amount} BDT...")
        # Delegates execution to the chosen payment strategy
        self.strategy.pay(amount)
        print("Payment Successful!")

# ============================================================
# Step 4: Main Program
# ============================================================
# Start with Bkash
payment = PaymentContext(BkashPayment())
payment.checkout(500)

# Change to Nagad
payment.set_strategy(NagadPayment())
payment.checkout(1000)

# Change to Card
payment.set_strategy(CardPayment())
payment.checkout(2000)

# Change to Cash
payment.set_strategy(CashPayment())
payment.checkout(3000)
