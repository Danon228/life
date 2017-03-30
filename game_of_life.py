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
        self.matrix = [[None]*self.y for y in range(self.x)]
        # self.massive = [[0] * self.y for y in range(self.x)]
        name = 1
        self.names = []
        for _ in range(self.x * self.y+1):
            self.names.append(name)
            name += 1
        print(self.names)

    def __str__(self):
        st = ''
        for y in range(self.y):
            line = []
            for x in range(self.x):
                line.append(str(self.matrix[x][y]))
            st += ', '.join(line)+'\n'
        return st

    '''def create_options(self):
        for x in range(WIDTH):
            for y in range(HEIGHT):
                if self.belonging_class(x,y,Animal) or self.belonging_class(x,y,Predator):
                    self.options[matrix[x][y]]['life'] = 100
                    self.options[matrix[x][y]]['energy'] = 100'''

    def get_count(self):
        for x in range(WIDTH):
            for y in range(HEIGHT):
                if not(self.matrix[x][y]):
                    self.count+=1
        return self.count

    def get_name(self):
        return self.names.pop()

    def get_element(self, x, y):
        if x>=0 and y>=0:
            return self.matrix[x][y]
        else:
            return 'Empty'
        
    def put_elements(self, obj, x=None, y=None):
        ''' вставляет объект по координатам '''
        if not x or not y:
            x = randint(0, WIDTH-1)
            y = randint(0, HEIGHT-1)
            if self.get_element(x,y):
                return False
            else:
                self.matrix[x][y] = obj
                return True
        else:
            self.matrix[x][y] = obj

    def belonging_class(self, x, y, cls):
        return self.matrix[x][y].__class__ == cls

    def delete_element(self,x,y):
        self.names.append(self.matrix[x][y])
        self.matrix[x][y] = None

    def give_life(self, x, y, count = 10):
        self.matrix[x][y].life += count

    def give_energy(self,x, y, count = 10):
        self.matrix[x][y].energy += count

    def take_life(self, x, y,count = 10):
        self.matrix[x][y].life -= count

    def take_energy(self, x, y,count = 10):
        self.matrix[x][y].energy -= count

    def travel(self,x1, y1, x2, y2):
        if
        self.matrix[x2][y2] = self.matrix[x1][y1]
        self.matrix[x1][y1] = None
        self.take_energy(x2,y2)

    def attack(self,x1,y1,x2,y2):
        self.take_energy(x1,y1,self.matrix[x1][y1].energy)
        self.take_energy(x2,y2,self.matrix[x2][y2].energy)
        self.take_life(x2,y2,self.matrix[x1][y1].energy - self.matrix[x1][y1].energy)

   def find_place(self,x1,y1,x2,y2):
       x_free = 2*x1-x2
       y_free = 2*y1-y2
       free_places = [[0]*2]*8
       if self.get_element(x_free, y_free) == 'Empty' or self.get_element(x_free,y_free)>=0:
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
               if self.get_element(x,y) == 'Empty' or self.get_element(x,y) >= 0:
                   free_places.remove([x,y])
                if len(free_places) != 0:
                line = choice.free_places
                x_free = line[0]


    def refresh(self):
        ''' проверяет имеющиеся объекты, запускает действия для каждого '''
        for x in range(WIDTH):
            for y in range(HEIGHT):
                if self.belonging_class(x, y, Animal):
                    for xk in [-1, 0, 1]:
                        for yk in [-1, 0, 1]:
                            if not xk and not yk: # если клетка не 0,0
                                x1 = xk+x if xk+x >= 0 else None
                                y1 = yk+y if yk+y >= 0 else None
                                if x1 and y1:# если клетка существует
                                    if self.belonging_class(x1,y1,Food):
                                        self.give_life(x,y)
                                        self.take_energy(x,y)
                                        if self.matrix[x][y].energy < 0 :
                                            count = -self.matrix[x][y].energy
                                            self.take_lifes(x,y,count)
                                    if self.belonging_class(x1,y1,Animal):
                                        if self.matrix[x][y].energy > self.matrix[x1][y1].energy:
                                            self.attack(x,y,x1,y1)
                                        elif
                                            ...
                                    if self.belonging_class(x1,y1,Predator):
                                        ...
                if self.belongig_class(x,y,Predator):
                    for xk in [-1, 0, 1]:
                        for yk in [-1, 0, 1]:
                            if not xk and not yk: # если клетка не 0,0
                                x1 = xk+x if xk+x >= 0 else None
                                y1 = yk+y if yk+y >= 0 else None
                                if x1 and y1:# если клетка существует
                                    if self.belonging_class(x1,y1,Animal) and self.matrix[x][y].energy>= 30:
                                        self.give_life(x,y,30)
                                        self.take_energy(x,y,30)
                                        self.delete_element(x1,y1)
                                        if self.matrix[x][y].energy < 30 :
                                            self.take_energy(x,y,30)
                                            if self.matrix[x1][y1].energy>=30:
                                                self.take_energy(x1,y1,30)
                                            else:
                                                self.take_energy(x1,y1,self.matrix[x1][y1].energy)
                                                self.take_life(x1,y1,30 - self.matrix[x1][y1].energy)
                                                self.give_life(x,y,30 - self.matrix[x1][y1].energy)


                                            pass
                                    if self.belonging_class(x1,y1,Predator):








# massive[x1][y1] = self.belonging_class(self,x1,y1, Animal) if belonging_class(self,x1,y1, Animal) else
#             if massive[x-1][y-1] and massive[x][y-1] == None:
#                 animal = Animal(matrix.get_name())
#                 put.elements(animal,x,y-1)
#         while True:
#             x = randint(WIDTH)
#             y = randint(HEIGHT)
#             if massive[x][y] == None:
#                 break
#         refresh(x,y,massive)
            



class Agent:
    def __init__(self):
        self.life = 100
        self.energy = 100
        self.is_worked = False

    def __str__(self):
        return str(self.name)

    def
        
      
class Animal(Agent):               
    def __init__(self, name):
        super().__init__()
        self.name = name


class Predator(Agent):
    def __init__(self, name):
        super().__init__()
        self.name = name
        

class Food:
    def __init__(self,name):
        self.name = name
      

matrix = Matrix(WIDTH, HEIGHT)
i, l = 0, 0
while i != COUNT_A:
    animal = Animal(matrix.get_name())
    try:
        matrix.put_elements(animal)
    except Exception as e:
        print('Элемент занят', e)
        i -= 1
    i += 1

while l != COUNT_F:
    food = Food(matrix.get_name())
    try:
        matrix.put_elements(food)
    except Exception as e:
        print('Элемент занят', e)
        l -= 1
    l += 1

while k != COUNT_P:
    predator = Predator(matrix.get_name())
    try:
        matrix.put_elements(predator)
    except Exception as e:
        print('Элемент занят', e)
        k -= 1
    l += 1



animal = Animal(matrix.get_name())
matrix.put_elements(animal, 0, 0)
print(matrix.belonging_class(0, 0, Food))
print(matrix.belonging_class(0, 0, Animal))
print(matrix)
x, y = int(input('Введите координаты >> '))
matrix.put_elements(animal, x, y)
