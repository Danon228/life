from random import randint

WIDTH = 10
HEIGHT = 15
COUNT_A = 10
COUNT_F = 10

class Matrix:
    def __init__(self, count_x, count_y):
        ''' создаем матрицу '''
        self.x = count_x
        self.y = count_y
        self.matrix = [[None]*self.y for y in range(self.x)]
        self.massive = [[0] * self.y for y in range(self.x)]
        name = 0
        self.names = []
        for _ in range(self.x * self.y):
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

    def get_count(self):
        for x in range(self.matrix):
            for y in range(self.matrix):
                if self.matrix[x][y] != None:
                    count+=1
        return count

    def get_name(self):
        return self.names.pop()

    def get_element(self, x, y):
        return self.matrix[x][y]
        
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
        result = self.matrix[x][y].__class__ == cls
        return result

    def refresh(self,x = 0, y = 0, m):
        ''' проверяет имеющиеся объекты, запускает действия для каждого '''
        for l in range(self.y):
            line = []
            for t in range(self.x):
                line.append(str(self.massive[t][l]))
            st += ', '.join(line)
        if st.find('0')>=0:
            if self.belonging_class(x, y, Animal):
                for xk in [-1, 0, 1]:
                    for yk in [-1, 0, 1]:
                        if not xk and not yk: # если клетка не 0,0
                            x1 = xk+x if xk+x >= 0 else None
                            y1 = yk+y if yk+y >= 0 else None
                            if x1 and y1:# если клетка существует
                                self.massive[x1][y1] = belonging_class(x1,y1,Animal) if belonging_class(x1,y1,Animal) else None
                                refresh(x1,y1,self.massive)



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
    def __str__(self):
        return str(self.name)
        
      
class Animal(Agent):               
    def __init__(self, name):
        self.name = name
        

class Food(Agent):
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
animal = Animal(matrix.get_name())
matrix.put_elements(animal, 0, 0)
print(matrix.belonging_class(0, 0, Food))
print(matrix.belonging_class(0, 0, Animal))
print(matrix)
x, y = int(input('Введите координаты >> '))
matrix.put_elements(animal, x, y)
print(matrix.refresh(x, y))