from .warehouse_selection_strategy import WarehouseSelectionStrategy

class NearestWarehouseSelectionStrategy(WarehouseSelectionStrategy):
    def select_warehouse(self, warehouse_list):
        # Algorithm to pick the nearest warehouse
        # For now, I'm just picking the first warehouse for demo purposes
        return warehouse_list[0]
