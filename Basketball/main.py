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




name = input("Enter player name: ")
num = input("Enter player number: ")

player1 = Player(name, num)

player1.get_player()
