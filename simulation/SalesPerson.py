from models.SaleOrder import SaleOrder
from utils import get_sample

class SalesPerson:
  def __init__(self, **kwargs) -> None:
    self.name = kwargs['name']
    self.monthly_order_qty = kwargs['monthly_order_qty']
    self.qty_per_order = kwargs['qty_per_order']
    self.delivery_duration = kwargs['delivery_duration']

  def sell(self, sku):
    random_qty = get_sample(self.qty_per_order, 0.2)
    print(f"{self.name} sold {random_qty} of {sku.name}")
    saleOrder = SaleOrder(
      sku,
      self.qty_per_order,
      self.delivery_duration
    )
