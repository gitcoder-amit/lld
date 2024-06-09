from typing import List
from .warehourse import *
from .warehouse_selection_strategy import * 

class WarehouseController:
    def __init__(self, warehouse_list: List[Warehouse], warehouse_selection_strategy: WarehouseSelectionStrategy = None):
        self.warehouse_list = warehouse_list
        self.warehouse_selection_strategy = warehouse_selection_strategy

    # Add new warehouse
    def add_new_warehouse(self, warehouse: Warehouse):
        self.warehouse_list.append(warehouse)

    # Remove warehouse
    def remove_warehouse(self, warehouse: Warehouse):
        self.warehouse_list.remove(warehouse)

    def select_warehouse(self, selection_strategy: WarehouseSelectionStrategy) -> Warehouse:
        self.warehouse_selection_strategy = selection_strategy
        return self.warehouse_selection_strategy.selectWarehouse(self.warehouse_list)
