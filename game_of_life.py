from random import randint

WIDTH = 10
HEIGHT = 15
COUNT_A = 10
COUNT_F = 10

class Matrix:
    def __init__(self, count_x, count_y):#создаем матрицу
        self.x = count_x
        self.y = count_y
        self.matrix = [[None]*self.y for y in range(self.x)]
        name = 0
        self.names = []
        for i in range(self.x*self.y):
            self.names.append(name)
            name+=1
        print(self.names)

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
        if x == None or y == None:
            x = randint(0, WIDTH-1)
            y = randint(0, HEIGHT-1)
            if self.get_element(x,y):
                return False
            else:
            self.matrix[x][y] = obj
                return True
        else:
            self.matrix[x][y] = obj
    def belonging_class(self,x,y, cls):
        result = self.matrix[x][y].__class__ == cls
        return result

    def refresh(self,x = 0, y = 0, massive = [[None]*self.y for y in range(self.x)]):
        ''' проверяет имеющиеся объекты, запускает действия для каждого '''
##        if x == None and y == None:
##            for x in range(self.x):
##                for y in range(self.y):
##                    if belonging_class(x,y,Animal):
##                        for xk in [-1, 0, 1]:
##                            for yk in [-1, 0, 1]:
##                                x = x + xk if x + xk >= 0 else None
##                                y = 
##                        ref_1 = belonging_class(x,y-1,Animal)
##                        ref_2 = belonging_class(x+1,y-1,Animal)
##                        ref_3 = belonging_class(x+1,y,Animal)
##                        ref_4 = belonging_class(x+1,y+1,Animal)
##                        ref_5 = belonging_class(x,y+1,Animal)
##                        ref_6 = belonging_class(x-1,y+1,Animal)
##                        ref_7 = belonging_class(x-1,y,Animal)
##                        ref_8 = belonging_class(x-1,y-1,Animal)
##        else:
##            if belonging_class(x,y,Animal):
##                        ref_1 = belonging_class(x,y-1,Animal)
##                        ref_2 = belonging_class(x+1,y-1,Animal)
##                        ref_3 = belonging_class(x+1,y,Animal)
##                        ref_4 = belonging_class(x+1,y+1,Animal)
##                        ref_5 = belonging_class(x,y+1,Animal)
##                        ref_6 = belonging_class(x-1,y+1,Animal)
##                        ref_7 = belonging_class(x-1,y,Animal)
##                        ref_8 = belonging_class(x-1,y-1,Animal)
##        return ref_1, ref_2,  ref_3,  ref_4,  ref_5,  ref_6,  ref_7,  ref_8
        if belonging_class(x,y,Animal):
            for xk in [-1, 0, 1]:
                for yk in [-1, 0, 1]:
                    if not xk and not yk:
                        x1 = xk+x if xk+x >= 0 else None
                        y1 = yk+y if yk+y >= 0 else None
                        if x1 != None and y1 != None and massive[x1][y1] == None:
                            massive[x1][y1] = belonging_class(self,x1,y1, Animal) if belonging_class(self,x1,y1, Animal) else  
            if massive[x-1][y-1] and massive[x][y-1] == None:
                animal = Animal(matrix.get_name())
                put.elements(animal,x,y-1)
        while True:
            x = randint(WIDTH)
            y = randint(HEIGHT)
            if massive[x][y] == None:
                break
        refresh(x,y,massive)
        
            
            
                
                
            
    def __str__(self):
        st=''
        for y in range(self.y):
            line=[]
            for x in range(self.x):
                line.append(str(self.matrix[x][y]))
            st += (', '.join(line)+'\n')
        return st

                
class Agent:
    def __str__(self):
        return str(self.name)
        
      
class Animal(Agent):               
    def __init__(self, name):
        self.name = name
        


class Food(Agent):
    def __init__(self,name):
        self.name = name       
        
      
#pep8

matrix = Matrix(WIDTH, HEIGHT)
i,l=0,0
while i != COUNT_A:
    animal = Animal(matrix.get_name())
    try:
        matrix.put_elements(animal)
    except Exception as e:
        print('Элемент занят', e)
        i-=1
    i+=1

while l != COUNT_F:
    food = Food(matrix.get_name())
    try:
        matrix.put_elements(food)
    except Exception as e:
        print('Элемент занят', e)
        l-=1
    l+=1
animal = Animal(matrix.get_name())
matrix.put_elements(animal,0,0)
print(matrix.belonging_class(0,0, Food))
print(matrix.belonging_class(0,0, Animal))
print(matrix)
x, y = int(input('Введите координаты>> '))
matrix.put_elements(animal,x,y)
print(refresh(x,y))


##animal = Animal(WIDTH, HEIGHT)
##food = Food(WIDTH, HEIGHT, animal.animal)
##print(food.food)
##agent = Agent()
##matrix.put_elements(animal.animal,food.food)
##matrix.printer()
'''print(str(agent))'''
#matrix.put_element(1,1,a)
#matrix.put_element(5,5,f)
#print(matrix)
