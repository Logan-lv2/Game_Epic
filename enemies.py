class Enemy:
    def __init__(self, name, stats, exp_reward):
        self.name = name
        self.stats = stats
        self.exp_reward = exp_reward
        self.gold_min = exp_reward // 2
        self.gold_max = exp_reward * 2
        
def generate_enemy(floor):
    enemy_types = [
        {"name": "Gobelin", "stats": {"hp": 50, "attack": 8, "defense": 3}},
        {"name": "Loup géant", "stats": {"hp": 70, "attack": 12, "defense": 5}},
        {"name": "Mage noir", "stats": {"hp": 40, "attack": 15, "defense": 2}}
    ]
    
    enemy_data = random.choice(enemy_types)
    # Scaling avec l'étage
    multiplier = 1 + (floor // 10) * 0.5
    stats = {k: int(v * multiplier) for k, v in enemy_data["stats"].items()}
    exp = int(30 * multiplier)
    
    return Enemy(enemy_data["name"], stats, exp)