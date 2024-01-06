import json
from random import randint
from models.SKU import SKU

class SKUList(list[SKU]):
  def __init__(self, *args, **kwargs) -> None:
    super().__init__(*args, **kwargs)

  def init(self):
    for sku in self.from_file():
      self.append(SKU(**sku))

  def from_file(self):
    filepath = './maindata/sku.json'
    return json.load((open(filepath, 'r')))
  
  def get_random_sku(self):
    return self[randint(0, len(self) - 1)]