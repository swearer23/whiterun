import json
from simulation.SaleDept import SaleDept
from simulation.SkuList import SKUList

def gen_SO(saleDept: SaleDept, skuList: SKUList):
  for salesPerson in saleDept.sales_people:
    sku = skuList.get_random_sku()
    salesPerson.sell(sku)

def main():
  saleDept = SaleDept()
  saleDept.init_sale_people()
  skuList = SKUList()
  skuList.init()
  gen_SO(saleDept, skuList)

if __name__ == '__main__':
  main()