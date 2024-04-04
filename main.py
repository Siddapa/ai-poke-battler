class Battle:
    def __init__(self):
        self.turns = []
        self.team1 = []
        self.team2 = []


class Pokemon:
    def __init__(self, name):
        # Fetch these individually using PokeAPI
        self.hp = 0
        self.atk = 0
        self.def = 0
        self.spatk = 0
        self.spdef = 0
        self.speed = 0
        self.item = ''
