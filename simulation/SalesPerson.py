from models.SaleOrder import SaleOrder
from models.SKU import SKU
from utils import get_sample

class SalesPerson:
  def __init__(self, **kwargs) -> None:
    self.name = kwargs['name']
    self.monthly_order_qty = kwargs['monthly_order_qty']
    self.qty_per_order = kwargs['qty_per_order']
    self.delivery_duration = kwargs['delivery_duration']

  def sell(self, sku: SKU):
    if self.is_selling_today() == False:
      return None
    sample_order_qty = get_sample(self.qty_per_order, 0.2)
    sample_order_duration = get_sample(self.delivery_duration, 0.5)
    saleOrder = SaleOrder(
      sku,
      sample_order_qty,
      sample_order_duration,
      sales_person_name=self.name
    )
    return saleOrder

  def is_selling_today(self):
    prob = self.monthly_order_qty / 30
    sample_prob = get_sample(prob, 0.5)
    if sample_prob < 0.5:
      return False
    else:
      return True
