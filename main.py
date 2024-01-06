import json
from simulation.SaleDept import SaleDept
from simulation.SkuList import SKUList
from simulation.Logger import Logger

logger = Logger()

def gen_SO(saleDept: SaleDept, skuList: SKUList):
  order_list = []
  for salesPerson in saleDept.sales_people:
    sku = skuList.get_random_sku()
    order = salesPerson.sell(sku)
    if order is not None:
      order_list.append(order)
  return order_list

def main():
  saleDept = SaleDept()
  saleDept.init_sale_people()
  skuList = SKUList()
  skuList.init()
  day = 0
  while day < 100:
    logger.new_day(day)
    order_list = gen_SO(saleDept, skuList)
    logger.new_order(order_list)
    day += 1

if __name__ == '__main__':
  main()