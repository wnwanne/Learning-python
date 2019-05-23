class Player:
    def __init__(self, name, jersey_num):
        self.name = name
        self.jersey_num = jersey_num
        self.skills = {
            'shooting': True,
            'dribbling': True,
            'dunking': True}
        self.total_rest_time = 0

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

    def rest(self, duration):
        #rests player for duration of time (minutes)
        print('{} is resting for {} minutes'.format(self.name, duration))
        self.total_rest_time += duration
        print('{} is has now rested for {} minutes'.format(self.name,
                                                        self.total_rest_time))


name = input("Enter player name: ")
num = input("Enter player number: ")

player1 = Player(name, num)

#TODO: Winston, integrate this with player and use the new features in your RPG.
minutes = input('Enter a rest period (minutes): ')


player1.get_player()
