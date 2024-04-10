import requests
import json


'''
Represents all relevant characteristics of Pokemon with the game's battle mechanics
Each characteristic is converted into a custom JSON for use in the damage-calc API
'''
class Pokemon:
    def __init__(self):
        self.name = ''
        self.level = 0
        self.cur_hp = 0
        self.item = ''
        self.ability = ''
        self.ivs = {'hp': 31, 'atk': 31, 'def': 31, 'spa': 31, 'spd': 31, 'spe': 31}
        self.evs = {'hp': 0, 'atk': 0, 'def': 0, 'spa': 0, 'spd': 0, 'spe': 0}
        self.nature = ''
        self.moves = []
        self.status = ''
        self.boosts = {'atk': 0, 'def': 0, 'spa': 0, 'spd': 0, 'spe': 0}
        self.toxic_counter = 10
        self.turns_on_field = 0

    def get_name(self):
        return self.data['name']

    def get_fields(self):
        return self.data['fields']

    def cvt_to_json(self):
        return {
            'name': self.name,
            'fields': {
                'level': self.level,
                'originalCurHp': self.cur_hp,
                'item': self.item,
                'ability': self.ability,
                'ivs': self.ivs,
                'evs': self.evs,
                'nature': self.nature,
                'moves': self.moves,
                'status': self.status,
                'boosts': self.boosts,
                'toxicCounter': self.toxic_counter
            }
        }



class Team:
    def __init__(self, pkm):
        self.pkm = pkm
        self.lead = pkm[0]


class Turn:
    def __init__(self, trainer_team, opponent_team, field={}, gen=8):
        self.trainer_team = trainer_team
        self.opponent_team = opponent_team
        self.field = field
        self.gen = gen

    def simulate(self):
        speed_order = self.fetch_faster()

        # Stay in and attack
        if len(speed_order) != 0:
            for move1 in speed_order[0]['fields']['moveset']:
                for move2 in speed_order[1]['fields']['moveset']:
                    # Checklist: Ability, Terrain, Item, Move (Primary/Secondary)
                    Turn.fetch_turn_changes({
                        'gen': self.gen,
                        'pkm1': {
                            'name': self.trainer_team.lead['name'],
                            'fields': self.trainer_team.lead['fields']
                        },
                        'pkm2': {
                            'name': self.opponent_team.lead['name'],
                            'fields': self.opponent_team.lead['fields']
                        },
                        'move': move1,
                        'field': self.field
                    })

        # Switch to a better match up

        # Sack

        
    def fetch_turn_changes(data: dict):
        url = 'http://localhost:3000'
        r = requests.post(url + '/calc-damage', json=data)
        if r.status_code == 200:
            return r.json()
        else:
            return None

    def fetch_faster(self):
        calc = Turn.fetch_turn_changes({
            'gen': 8,
            'pkm1': self.trainer_team.lead.cvt_to_json(),
            'pkm2': self.opponent_team.lead.cvt_to_json(),
            'move': 'Tackle',
            'field': self.field
        })
        pkm1_speed = calc['attacker']['stats']['spe']
        pkm2_speed = calc['defender']['stats']['spe']
        if pkm1_speed > pkm2_speed:
            return [self.trainer_team.lead, self.opponent_team.lead]
        elif pkm1_speed < pkm2_speed:
            return [self.opponent_team.lead, self.trainer_team.lead]
        else:
            return []
