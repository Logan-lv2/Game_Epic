class Item:
    def __init__(self, name, item_type, stats, value):
        self.name = name
        self.type = item_type  # weapon, armor, consumable
        self.stats = stats  # {"attack": 5, "defense": 3}
        self.value = value
        
class Inventory:
    def __init__(self):
        self.items = []
        self.max_size = 20
        
    def add_item(self, item):
        if len(self.items) < self.max_size:
            self.items.append(item)
            return True
        return False
        
    def remove_item(self, index):
        if 0 <= index < len(self.items):
            return self.items.pop(index)
        return None
        
    def use_item(self, index, character):
        item = self.items[index]
        if item.type == "consumable":
            for stat, value in item.stats.items():
                if stat in character.stats:
                    character.stats[stat] = min(
                        character.stats[stat] + value,
                        character.stats[f"max_{stat}"] if f"max_{stat}" in character.stats else float('inf')
                    )
            self.remove_item(index)
            return True
        return False