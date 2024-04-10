import re
from battle import Turn, Team, Pokemon
from random import choice


def load_pkm(filename: str):
    with open (filename, 'a') as f:
        f.write('\n')

    all_pkm = []
    with open(filename, 'r') as f:
        new_pkm = Pokemon()
        for line in f:
            name_item = re.search('([\'\(\)\w\s-]+) @ ([\w\s-]+)', line)
            ability = re.search('Ability: ([\w\s-]+)', line)
            ivs = re.search('IVs: (.+)', line)
            evs = re.search('EVs: (.+)', line)
            nature = re.search('([\w\s-]+) Nature', line)
            move = re.search('- ([\w\s-]+)', line)

            if name_item:
                new_pkm.name = name_item[1]
                new_pkm.item = name_item[2].rstrip()
            elif ability:
                new_pkm.abilty = ability[1].rstrip()
            elif ivs:
                individual_ivs = re.findall('(\d+) (\w+)', ivs[1])
                for iv in individual_ivs:
                    new_pkm.ivs[iv[1].lower()] = int(iv[0])
            elif evs:
                individual_evs = re.findall('(\d+) (\w+)', evs[1])
                for ev in individual_evs:
                    new_pkm.evs[ev[1].lower()] = int(ev[0])
            elif nature:
                new_pkm.nature = nature[1]
            elif move:
                new_pkm.moves.append(move[1].rstrip())
            else:
                if new_pkm.name:
                    all_pkm.append(new_pkm)
                new_pkm = Pokemon()
    return all_pkm


if __name__ == '__main__':
    trainer_team = Team(load_pkm('example_team.txt'))
    opponent_team = Team(load_pkm('example_team.txt'))

    start = Turn(trainer_team, opponent_team)
    print(start.fetch_faster())
    
    # start = Turn(choice(trainer_team), choice(opponent_team))

