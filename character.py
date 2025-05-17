class Character:
    def __init__(self, name, char_class):
        self.name = name
        self.char_class = char_class
        self.level = 1
        self.exp = 0
        self.stats = {
            "hp": 100,
            "max_hp": 100,
            "mp": 50,
            "max_mp": 50,
            "attack": 10,
            "defense": 5,
            "magic": 8,
            "speed": 7
        }
        self.skills = []
        self.equipment = {
            "weapon": None,
            "armor": None,
            "accessory": None
        }
        self.inventory = []
        
    def add_exp(self, amount):
        self.exp += amount
        needed = self.get_exp_needed()
        if self.exp >= needed:
            self.level_up()
            
    def get_exp_needed(self):
        return 100 * (1.5 ** (self.level - 1))
        
    def level_up(self):
        self.level += 1
        self.exp = 0
        self.stats["max_hp"] += 20
        self.stats["max_mp"] += 10
        self.stats["attack"] += 5
        self.stats["defense"] += 3
        self.stats["magic"] += 4
        self.stats["speed"] += 2
        self.stats["hp"] = self.stats["max_hp"]
        self.stats["mp"] = self.stats["max_mp"]
        
        # Ajout de compétences selon la classe
        self.learn_skills()
        
    def learn_skills(self):
        class_skills = {
            "Sabreur": ["Coup critique", "Tourbillon"],
            "Mage": ["Boule de feu", "Soin"],
            "Archer": ["Flèche multiple", "Tir précis"]
        }
        
        if self.level in [2, 5, 10, 15]:
            new_skill = class_skills[self.char_class][len(self.skills)]
            self.skills.append(new_skill)