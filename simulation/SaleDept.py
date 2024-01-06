import json
from simulation.SalesPerson import SalesPerson

class SaleDept:
  def __init__(self):
    self.sales_people: list[SalesPerson] = []

  def init_sale_people(self):
    for person in self.sales_person_from_file():
      self.sales_people.append(SalesPerson(**person))

  def sales_person_from_file(self):
    filepath = './maindata/sales_person.json'
    return json.load((open(filepath, 'r')))