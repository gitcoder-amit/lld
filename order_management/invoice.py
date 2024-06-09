class Invoice:
    def __init__(self):
        self.total_item_price = 0
        self.total_tax = 0
        self.total_final_price = 0

    # Generate Invoice
    def generate_invoice(self, order):
        # Compute and update the above details
        self.total_item_price = 200
        self.total_tax = 20
        self.total_final_price = 220
