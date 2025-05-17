class CombatSystem:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy
        self.turn = 0  # 0 = joueur, 1 = ennemi
        self.result = None  # None, "win", "lose"
        
    def update(self):
        if self.turn == 0:
            # Tour du joueur (géré via interface)
            pass
        else:
            # Tour de l'ennemi
            self.enemy_turn()
            
    def enemy_turn(self):
        # IA simple de l'ennemi
        if random.random() < 0.7:
            damage = max(1, self.enemy.attack - self.player.stats["defense"] // 2)
            self.player.stats["hp"] -= damage
        else:
            # Utilisation de compétence spéciale
            pass
            
        self.turn = 0
        
    def player_attack(self):
        damage = max(1, self.player.stats["attack"] - self.enemy.defense // 2)
        self.enemy.hp -= damage
        self.turn = 1
        
    def player_use_skill(self, skill_index):
        skill = self.player.skills[skill_index]
        # Logique des compétences spéciales
        self.turn = 1
        
    def check_victory(self):
        if self.enemy.hp <= 0:
            self.result = "win"
            exp_gain = self.enemy.exp_reward
            gold_gain = random.randint(self.enemy.gold_min, self.enemy.gold_max)
            return exp_gain, gold_gain
        elif self.player.stats["hp"] <= 0:
            self.result = "lose"
            return 0, 0
        return None