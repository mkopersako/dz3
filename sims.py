# class Human:
#     def __init__(self, name):
#         self.name = name
#
# class Auto:
#     def __init__(self, brand):
#         self.brand = brand
#         self.passengers = []
#
#     def add_passengers(self, human):
#         self.passengers.append(human)
#
#     def print_passengers(self):
#         if self.passengers != []:
#             print(f'Names of {self.brand} passengers:')
#             for passenger in self.passengers:
#                 print(passenger)
#
# nick = Human('Nick')
# anna = Human('Anna')
# car = Auto('BMW')
# car.add_passengers(nick)
# car.add_passengers(anna)
# car.print_passengers()

import random
class Human:
    def __init__(self, name='Human', job=None, home=None, car=None):
        self.name = name
        self.job = job
        self.home = home
        self.car = car
        self.money = 100
        self.gladness = 50
        self.satiety = 50
    def get_job(self):
        if self.car.drive():
            pass
        else:
            self.to_repair()
            return
        self.job = Job(job_list)
    def get_car(self):
        self.car = Auto(brands_of_car)
    def get_home(self):
        self.home = House()

    def eat(self):
        if self.home.food <= 0:
            self.shopping('food')
        else:
            if self.satiety >= 100:
                self.satiety = 100
                return
            self.satiety += 5
            self.home.food -= 5
    def work(self):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 10:
                self.shopping('fuel')
                return
            else:
                self.to_repair()
                return
        self.money += self.job.salary
        self.gladness -= self.job.gladness
        self.satiety -= 5
    def shopping(self, manage):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 10:
                manage = 'fuel'
            else:
                self.to_repair()
                return
        if manage == 'fuel':
            print('I bought fuel')
            self.money -= 50
            self.car.fuel += 100
        elif manage == 'food':
            print('Bought food')
            self.money -= 20
            self.satiety += 5
            self.gladness += 2
    def chill(self):
        self.gladness += 10
        self.home.mess += 5
    def clean_home(self):
        self.gladness -= 5
        self.home.mess = 0
    def to_repair(self):
        self.car.strength += 100
        self.money -= 100

    def days_indexes(self):
        days = f"Today the {day} of {self.name}'s life"
        print(f'{day:=^50}')
        human_indexes = self.name + "'s indexes"
        print(f'{human_indexes:+^50}')
        print(f'Money = {self.money}')
        print(f'Satiety = {self.satiety}')
        print(f'Gladness = {self.gladness}')

        home_indexes = 'Home indexes'
        print(f'{home_indexes:^50}')
        print(f'Food = {self.home.food}')
        print(f'Mess = {self.home.mess}')

        car_indexes = f"{self.car.brand} car indexes"
        print(f'{car_indexes:^50}')
        print(f'Fuel = {self.car.fuel}')
        print(f'Strength = {self.car.strength}')

    def is_alive(self):
        if self.gladness < 0:
            print('Depression...')
            return False
        if self.satiety < 0:
            print('Dead...')
            return False
        if self.money < -500:
            print('Bankrupt...')
            return False
    def live(self, day):
        if self.is_alive() == False:
            return False
        if self.home is None:
            print('Settled in te home')
            self.get_home()
        if self.car is None:
            self.get_car()
            print(f"I bought a car {self.car.brand}")
        if self.job is None:
            self.get_job()
            print(f"")

class Auto:
    def __init__(self, brand_list):
        self.brand = random.choice(list(brand_list))
        self.fuel = brand_list[self.brand]['fuel']
        self.strength = brand_list[self.brand]['strength']
        self.consumption = brand_list[self.brand]['consumption']

    def drive(self):
        if self.strength > 0 and self.fuel >= self.consumption:
            self.fuel -= 10
            self.strength -= 1
            return True
        else:
            print('The car cannot move')
            return False



class House:
    def __init__(self):
        self.food = 0
        self.mess = 0

class Job:
    def __init__(self, job_list):
        self.job = random.choice(list(job_list))
        self.salary = job_list[self.job]['salary']
        self.gladness = job_list[self.job['job_gladness']]


job_list = {'C++': {'salary': 90, 'job_gladness': 3},
            'Python': {'salary': 50, 'job_gladness': 10},
            'Java': {'salary': 70, 'job_gladness': 7},
            'PHP': {'salary': 40, 'job_gladness': 5}}

brands_of_car = {"BMW": {'fuel': 100, 'strength': 100, 'consumption': 6},
                 "Lada": {'fuel': 50, 'strength': 30, 'consumption': 9},
                 "Ford": {'fuel': 80, 'strength': 150, 'consumption': 8},
                 "Audi": {'fuel': 70, 'strength': 120, 'consumption': 7}}
