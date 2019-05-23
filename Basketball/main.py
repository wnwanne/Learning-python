class Player:
    def __init__(self, name, jersey_num):
        self.name = name
        self.jersey_num = jersey_num
        self.skills = {
            'shooting': True,
            'dribbling': True,
            'dunking': True}

    def set_skill(self, skill):
        self.skills[skill] = True

    def get_player(self):
        msg = 'name: {}\nnumber: {}\nskills: {}'
        print(msg.format(self.name, self.jersey_num, self.skills))

    def change_jers_num(self, jers):
        self.jersey_num = jers


    def injured(self):
        #resets all player skills to false
        for skill in self.skills:
            self.skills[skill] = False


class Team:
    def __init__(self, name, members):
        self.name = name
        self.members = members
        self.build_team()

    def get_players(self, name, jersey_num):
        self.name = name
        self.jersey_num = jersey_num
        return name, jersey_num

    def build_team(self):
        # create list of player names
        self.member_names = []
        for member in self.members:
            self.member_names.append(member.name)

    def get_team(self):
        msg = 'name: {}\nmember: {}'
        print(msg.format(self.name, self.member_names))




# have user define number of players
team_members = []
number_of_players = int(input('Enter number of players: '))
for n in range(number_of_players):
    player_num = n+1
    print('Creating Player{}'.format(player_num))
    name = input("Enter player name: ")
    num = input("Enter player number: ")
    player = Player(name, num)
    team_members.append(player)

team1 = Team("cavs", team_members)

team1.get_team()
'''

practiceDictionary = {
    "winston": 22,
    'chris': 24,
    'sage': 16
}

if 'Winston' in practiceDictionary:
    print(practiceDictionary)
else:
    print("its not in there")'''