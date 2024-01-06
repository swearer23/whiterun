from enum import Enum
from models.SKU import SKU

class SaleOrderStatus(Enum):
    PENDING = 'pending'
    IN_PROGRESS = 'in_progress'
    COMPLETED = 'completed'
    CANCELLED = 'cancelled'

class SaleOrder:
    def __init__(self, sku: SKU, qty, delivery_day, **kwargs):
        self.sku = sku
        self.qty = qty
        self.delivery_day = delivery_day
        self.status = SaleOrderStatus.PENDING
        self.sales_person_name = kwargs['sales_person_name']

    def __dict__(self):
        return {
            'sku': self.sku.name,
            'qty': self.qty,
            'delivery_day': self.delivery_day,
            'status': self.status.value,
            'sales_person_name': self.sales_person_name
        }
