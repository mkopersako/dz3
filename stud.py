import random


class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.money = 100
        self.alive = True
        self.satiety = 50

    def to_study(self):
        print('Time to study...')
        self.progress += 0.2
        self.gladness -= 2
        self.satiety -= 1

    def to_sleep(self):
        print('Time to sleep')
        self.gladness += 3

    def to_chill(self):
        print('Time to chill...')
        self.gladness += 5
        self.progress -= 0.3
        self.satiety -= 1
        self.money -= 20

    def to_work(self):
        print('Time to work...')
        self.money += 100
        self.gladness += 10
        self.satiety -= 15

    def is_alive(self):
        if self.progress <= -0.5:
            print('Cast out...')
            self.alive = False
        elif self.gladness == 0:
            print('Depression..')
            self.to_chill()
        elif self.progress > 5:
            print('Externally...')
            self.alive = False
        elif self.satiety == 0:
            print('Dead...')
            self.alive = False
        if self.money < 20:
            self.to_work()
        if self.progress < 0.5:
            self.to_study()

    def end_of_day(self):
        print(f'Gladness = {self.gladness}')
        print(f'Progress = {round(self.progress, 2}')
        print(f'Money - {self.money}')
        print(f'Satiety - {self.satiety}')

    def live(self, day):
        day = "Day " + str(day) + ' of ' + self.name + "life"
        print(f'{day:=^50}')
        live_cube = random.randint(1, 4)
        if live_cube == 1:
            self.to_study()
        elif live_cube == 2:
            self.to_sleep()
        elif live_cube == 3:
            self.to_chill()
        elif live_cube == 4:
            self.to_work()
        self.end_of_day()
        self.is_alive()


nick = Student('Igor')
for day in range(365):
    if nick.alive == False:
        break
    nick.live(day)