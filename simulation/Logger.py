from enum import Enum
import pandas as pd
from models.SaleOrder import SaleOrder

class LoggerType(Enum):
  NEW_ORDER = 'new_order'

class Logger:
  def new_day(self, day: int):
    print(f'==============Day {day}==============')

  def new_order(self, order_list: list[SaleOrder]):
    self.__unified_log([{
        'type': LoggerType.NEW_ORDER.value,
        **order.__dict__()
      } for order in order_list
    ])

  def __unified_log(self, obj: dict):
    print(pd.DataFrame(obj))