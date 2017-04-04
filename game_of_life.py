from random import randint, choice


WIDTH = 10
HEIGHT = 15
COUNT_A = 10
COUNT_F = 10
COUNT_P = 10


class Matrix:
    def __init__(self, count_x, count_y):
        ''' создаем матрицу '''
        self.x = count_x
        self.y = count_y
        self.matrix = [[None]*count_y for x in range(count_x)]

    def __str__(self):
        st = ''
        for y in range(self.y):
            line = []
            for x in range(self.x):
                line.append(str(self.matrix[x][y]))
            st += ', '.join(line)+'\n'
        return st

    def get_element(self, x, y):
        if WIDTH > x >= 0 and HEIGHT > y >= 0 :
            return self.matrix[x][y]
        else:
            return 'Empty'

    def put_elements(self, obj, x1=None, y1=None):
        ''' вставляет объект по координатам '''
        if not x1 or not y1:
            x1 = randint(0, WIDTH - 1)
            y1 = randint(0, HEIGHT - 1)
            if self.get_element(x1, y1):
                print('Клетка занята')
                return None, None
            else:
                self.matrix[x1][y1] = obj
                x_obj = x1
                y_obj = y1
                return x_obj, y_obj
        else:
            self.matrix[x1][y1] = obj
            x_obj = x1
            y_obj = y1
            return x_obj, y_obj

    def refresh(self, list_of_obj):
        self.matrix = [[None]*self.x for x in range(self.y)]
        for obj in [list_of_obj]:
            self.put_elements(obj, obj.cor_x, obj.cor_y)

    def get_list_of_objects(self):
        self.list_of_objects = []
        for x in range(WIDTH):
            for y in range(HEIGHT):
                if self.get_element(x, y):
                    self.list_of_objects.append(self.get_element(x, y))


class Agent:
    def __init__(self,count_energy, count_life):
        self.life = count_life
        self.energy = count_energy
        self.is_worked = False
        self.cor_x = 0
        self.cor_y = 0

    def get_name(self):
        return self.name

    def belong_class(self, obj, cls):
        return isinstance(obj, cls)

    def give_life(self,count=10):
        self.life += count

    def give_energy(self,count=10):
        self.energy += count

    def take_life(self,count=10):
        self.life -= count

    def take_energy(self,count=10):
        self.energy -= count

    def travel(self,x2, y2):
        self.cor_x = x2
        self.cor_y = y2
        self.take_energy()


class Controller:
    def delete_element(self, obj):
        self.list_of_objects.remove(obj)

    def attack_1(self, obj_1, obj_2):
        obj_2.take_life(obj_1.energy - obj_2.energy)
        obj_1.take_energy(obj_1.energy)
        obj_2.take_energy(obj_2.energy)
        if obj_2.life <= 0:
            self.delete_element(obj_2)

    def attack_2(self, obj_1, obj_2):
        if obj_1.energy >= obj_2.energy:
            obj_1.give_life(obj_2.life)
            obj_1.take_energy(obj_1.energy)
            obj_2.take_energy(obj_2.energy)
            self.delete_element(obj_2)
        else:
            obj_1.take_energy(obj_1.energy)
            obj_2.take_energy(obj_1.energy)

    def find_place(self, obj_1, obj_2=None):
        x1, y1 = obj_1.cor_x, obj_1.cor_y
        if obj_2:
            x2, y2 = obj_2.cor_x, obj_2.cor_y
            x_free = 2 * x1 - x2
            y_free = 2 * y1 - y2
            t = self.matrix.get_element(x_free, y_free)
        else:
            t = True
            x_free = 0
            y_free = 0
        free_places = [[0] * 2] * 8
        if self.matrix.get_element(x_free, y_free) == 'Empty' or t:
            free_places[0][0], free_places[0][1] = x1, y1 + 1
            free_places[1][0], free_places[1][1] = x1 + 1, y1 + 1
            free_places[2][0], free_places[2][1] = x1 + 1, y1
            free_places[3][0], free_places[3][1] = x1 + 1, y1 - 1
            free_places[4][0], free_places[4][1] = x1, y1 - 1
            free_places[5][0], free_places[5][1] = x1 - 1, y1 - 1
            free_places[6][0], free_places[6][1] = x1 - 1, y1
            free_places[7][0], free_places[7][1] = x1 - 1, y1 + 1
            for k in range(7):
                x = free_places[k][0]
                y = free_places[k][1]
                if self.matrix.get_element(x, y) == 'Empty' or self.matrix.get_element(x, y) >= 0:
                    free_places.remove([x, y])
                if len(free_places) != 0:
                    line = choice(free_places)
                    x_free = line[0]
                    y_free = line[1]
                else:
                    x_free, y_free = None, None
        return x_free, y_free

    def get_list_of_neighbour(self, obj):
        list_of_neighbour = []
        x = obj.cor_x
        y = obj.cor_y
        for x1 in [-1, 0, 1]:
            for y1 in [-1, 0, 1]:
                if x1 != 0 and y1 != 0:
                    if self.matrix.get_element(x + x1, y + y1) != 'Empty' and \
                            self.matrix.get_element(x + x1, y + y1):
                        list_of_neighbour.append(self.matrix.get_element(x + x1, y + y1))
        if len(list_of_neighbour):
            return None
        else:
            return choice(list_of_neighbour)

    def create_obj(self, cls, count):
        i = 0
        while i != count:
            obj = cls()
            x_cor, y_cor = self.matrix.put_elements(obj)
            if x_cor and y_cor:
                obj.cor_x = x_cor
                obj.cor_y = y_cor
                i += 1

    def start_game(self, matrix):
        self.matrix = matrix
        self.create_obj(Animal, COUNT_A)
        self.create_obj(Predator, COUNT_P)
        self.create_obj(Food, COUNT_F)
        self.list_of_objects = self.matrix.list_of_objects()
        for obj in [self.list_of_objects]:
            neighbour = self.get_list_of_neighbour(obj)
            if not obj.is_worked:
                if not neighbour:
                    if obj.belong_class(obj, Animal):
                        x_free, y_free = self.find_place(obj)
                        if x_free and y_free:
                            child = Animal()
                            child.cor_x, child.cor_y = self.matrix.put_elements(child, x_free, y_free)
                            obj.take_energy(obj.energy)
                            child.life = obj.life/2
                            obj.take_life(obj.life/2)
                        else:
                            obj.give_energy(20)
                            obj.take_life()
                    if obj.belong_class(obj, Predator):
                        x_free, y_free = self.find_place(obj)
                        if x_free and y_free:
                            child = Predator()
                            child.cor_x, child.cor_y = self.matrix.put_elements(child, x_free, y_free)
                            obj.take_energy(obj.energy)
                            child.life = obj.life/2
                            obj.take_life(obj.life/2)
                        else:
                            obj.give_energy(20)
                            obj.take_life()
                    if obj.belong_class(obj, Food):
                        x_free, y_free = self.find_place(obj)
                        if x_free and y_free:
                            child = Food()
                            child.cor_x, child.cor_y = self.matrix.put_elements(child, x_free, y_free)
                            child.life = obj.life / 2
                            obj.take_life(obj.life / 2)
                        else:
                            obj.take_life(50)
                else:
                    if obj.belong_class(obj, Animal):
                        if neighbour.belong_class(neighbour, Animal):
                            if obj.energy > neighbour.energy:
                                self.attack_1(obj, neighbour)
                                obj.is_worked = True
                            else:
                                x_end, y_end = self.find_place(obj, neighbour)
                                if x_end and y_end:
                                    obj.travel(x_end, y_end)
                                    obj.is_worked = True
                                else:
                                    obj.give_energy(20)
                                    obj.take_life(10)
                                    if obj.life <= 0:
                                        self.delete_element(obj)
                        if neighbour.belong_class(neighbour, Food):
                            if obj.energy > 0:
                                if neighbour.life <= obj.energy:
                                    self.delete_element(neighbour)
                                    obj.take_energy(neighbour.life)
                                    obj.give_life(neighbour.life)
                                    obj.is_worked = True
                                else:
                                    neighbour.take_life(obj.energy)
                                    obj.give_life(obj.energy)
                                    obj.take_energy(obj.energy)
                                    obj.is_worked = True
                            else:
                                obj.give_energy(20)
                                obj.take_life()
                        if neighbour.belong_class(neighbour, Predator):
                            if obj.energy >= 10:
                                x_end, y_end = self.find_place(obj, neighbour)
                                if x_end and y_end:
                                    obj.travel(x_end, y_end)
                            else:
                                obj.give_energy(20)
                                obj.take_life(10)
                    if obj.belong_class(obj, Predator):
                        if neighbour.belong_class(neighbour, Animal):
                            if obj.energy > 0:
                                self.attack_2(obj, neighbour)
                                obj.is_worked = True
                            else:
                                obj.give_energy(20)
                                obj.take_life(10)
                                if obj.life <= 0:
                                    self.delete_element(obj)
                        if neighbour.belong_class(neighbour, Predator):
                            if obj.energy > neighbour.energy:
                                self.attack_1(obj, neighbour)
                                obj.is_worked = True
                            else:
                                x_end, y_end = self.find_place(obj, neighbour)
                                if x_end and y_end:
                                    obj.travel(x_end, y_end)
                                    obj.is_worked = True
                                else:
                                    obj.give_energy(20)
                                    obj.take_life(10)
                                    if obj.life <= 0:
                                        self.delete_element(obj)
                    if obj.belong_class(obj, Food):
                        obj.give_life(30)
        self.matrix.refresh(self.list_of_objects)
        print(self.matrix)


class Animal(Agent):               
    def __init__(self):
        super().__init__(100,100)
        self.name = randint(0, 10000000000)


class Predator(Agent):
    def __init__(self):
        super().__init__(100, 100)
        self.name = randint(0, 10000000000)


class Food(Agent):
    def __init__(self):
        super().__init__(0,100)
        self.name = randint(0, 10000000000)


field = Matrix(WIDTH, HEIGHT)
game_controller = Controller()
game_controller.start_game(field)

