import json
from simulation.SaleDept import SaleDept
from simulation.SkuList import SKUList

orders = {}

def gen_SO(saleDept: SaleDept, skuList: SKUList):
  for salesPerson in saleDept.sales_people:
    sku = skuList.get_random_sku()
    if salesPerson.sell(sku) is not None:
      if salesPerson.name not in orders:
        orders[salesPerson.name] = 0
      orders[salesPerson.name] += 1

def main():
  saleDept = SaleDept()
  saleDept.init_sale_people()
  skuList = SKUList()
  skuList.init()
  day = 0
  while day < 100:
    gen_SO(saleDept, skuList)
    day += 1
  print(orders)

if __name__ == '__main__':
  main()