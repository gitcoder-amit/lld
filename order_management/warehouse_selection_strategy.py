from abc import ABC, abstractmethod
from typing import List
from .warehourse import *

class WarehouseSelectionStrategy(ABC):

    @abstractmethod
    def selectWarehouse(self, warehouse_list: List[Warehouse]):
        pass
