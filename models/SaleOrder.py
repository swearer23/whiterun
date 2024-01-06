class SaleOrder:
    def __init__(self, sku, qty, delivery_day):
        self.id = id
        self.sku = sku
        self.qty = qty
        self.delivery_day = delivery_day

    def __str__(self):
        return f"SaleOrder({self.id}, {self.customer}, {self.items}, {self.total}, {self.date})"

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        return self.id == other.id

    def __hash__(self):
        return hash(self.id)