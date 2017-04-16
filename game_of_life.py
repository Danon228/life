from random import randint, choice
from tkinter import *


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
        if self.x > x >= 0 and self.y > y >= 0 :
            return self.matrix[x][y]
        else:
            return 'Empty'

    def put_elements(self, obj, x1=None, y1=None):
        ''' вставляет объект по координатам '''
        if not x1 or not y1:
            x1 = randint(0, self.x - 1)
            y1 = randint(0, self.y - 1)
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

    def refresh(self, list):
        self.list_of_objects = list
        self.matrix = self.matrix = [[None]*self.y for x in range(self.x)]
        for obj in (self.list_of_objects):
            self.matrix[obj.cor_x][obj.cor_y] = obj

    def get_list_of_objects(self):
        self.list_of_objects = []
        for x in range(self.x):
            for y in range(self.y):
                if self.get_element(x, y):
                    self.list_of_objects.append(self.get_element(x, y))
        return self.list_of_objects


class Agent:
    def __init__(self,count_energy, count_life):
        self.life = count_life
        self.energy = count_energy
        self.is_worked = False
        self.cor_x = 0
        self.cor_y = 0
        self.IPP = 35

    def get_name(self):
        return self.name

    def belong_class( self, obj, cls):
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

    def __init__(self, x, y):
        self.matrix = Matrix(x,y)

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

    def find_place(self, obj_1, obj_2 = None):
        if obj_2:
            x1, y1 = obj_1.cor_x, obj_1.cor_y
            x2, y2 = obj_2.cor_x, obj_2.cor_y
            x_free = 2 * x1 - x2
            y_free = 2 * y1 - y2
            t = False
        else:
            x_free = 0
            y_free = 0
            t = True
        if self.matrix.get_element(x_free, y_free) == 'Empty' or t or self.matrix.get_element(x_free, y_free):
            free_places = []
            x = obj_1.cor_x
            y = obj_1.cor_y
            for x1 in [-1, 0, 1]:
                for y1 in [-1, 0, 1]:
                    if x1 != 0 and y1 != 0:
                        if not self.matrix.get_element(x + x1, y + y1) != 'Empty' and \
                                not self.matrix.get_element(x + x1, y + y1):
                            free_places.append([x + x1, y + y1])
            if len(free_places):
                line = choice(free_places)
                x_free = line[0]
                y_free = line[1]
            else:
                x_free = None
                y_free = None
        return x_free, y_free

    def get_list_of_neighbour(self, obj):
        list_of_neighbour = []
        x = obj.cor_x
        y = obj.cor_y
        for x1 in [-1, 0, 1]:
            for y1 in [-1, 0, 1]:
                if x1 != 0 and y1 != 0:
                    if self.matrix.get_element(x+x1, y+y1) and self.matrix.get_element(x+x1, y+y1) != 'Empty':
                        list_of_neighbour.append(self.matrix.get_element(x+x1, y+y1))
        if len(list_of_neighbour):
            return choice(list_of_neighbour)
        else:
            return None

    def create_objects(self, count, cls, IPP):
        i = 0
        while i != count:
            obj = cls()
            x_cor, y_cor = self.matrix.put_elements(obj)
            if x_cor or y_cor:
                obj.cor_x = x_cor
                obj.cor_y = y_cor
                if IPP:
                    obj.IPP = IPP
                i += 1

    def start_game(self, work):
        if work:
            self.list_of_objects = self.matrix.get_list_of_objects()
            for obj in (self.list_of_objects):
                neighbour = self.get_list_of_neighbour(obj)
                if not obj.is_worked:
                    if not neighbour:
                        x_free, y_free = self.find_place(obj)
                        if x_free and y_free:
                            if obj.belong_class(obj, Animal):
                                child = Animal()
                                child.cor_x, child.cor_y = self.matrix.put_elements(child, x_free, y_free)
                                self.list_of_objects.append(child)
                                child.energy = obj.energy/2
                                child.life = obj.life/2
                                obj.take_life(obj.life/2)
                                obj.take.energy(obj.energy)
                            if obj.belong_class(obj, Predator):
                                child = Predator()
                                child.cor_x, child.cor_y = self.matrix.put_elements(child, x_free, y_free)
                                self.list_of_objects.append(child)
                                child.energy = obj.energy
                                child.life = obj.life/2
                                obj.take_life(obj.life/2)
                                obj.take.energy(obj.energy)
                            if obj.belong_class(obj, Food):
                                child = Food()
                                child.cor_x, child.cor_y = self.matrix.put_elements(child, x_free, y_free)
                                self.list_of_objects.append(child)
                                child.life = obj.life / 2
                                obj.take_life(obj.life / 2)
                        else:
                            if obj.belong_class(obj, Food):
                                obj.give_life(50)
                            else:
                                obj.give_energy(30)
                                obj.take_life(5)
                                if obj.life <= 0:
                                    self.delete_element(obj)
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



class Animal(Agent):               
    def __init__(self):
        super().__init__(100,100)
        self.name = randint(0, 10000000000)
        self.color = 'blue'


class Predator(Agent):
    def __init__(self):
        super().__init__(100, 100)
        self.name = randint(0, 10000000000)
        self.color = 'red'


class Food(Agent):
    def __init__(self):
        super().__init__(0,100)
        self.name = randint(0, 10000000000)
        self.color = 'yellow'


class Interface(Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.pack(side='left', expand=True, fill='both')
        self.create_widgets()
        self.matrix = []

    def create_widgets(self):
        self.frame_parent = Frame(self)
        self.frame_parent.pack(side='left', expand=True, fill='both')
        self.frame_child = Frame(self.frame_parent)
        self.frame_child.pack(side='left', expand=True, fill='both')
        self.frame_widgets = Frame(self.frame_parent)
        self.frame_widgets.pack(side='top', expand=False, fill='x')
        Label(self.frame_widgets, text='Give parameters:',
              font='Arial 14').pack(side='top', expand=False)
        frame_create_matr_1 = Frame(self.frame_widgets, bg='gray')
        frame_create_matr_1.pack(side='top', expand=True, fill='x')
        Label(frame_create_matr_1, text='Give Width ',
              font='Arial 10', bg='gray').pack(side='left')
        self.ent_x = Entry(frame_create_matr_1)
        self.ent_x.pack(side='left')
        Label(frame_create_matr_1, text='Give Height',
              font='Arial 10', bg='gray').pack(side='left')
        self.ent_y = Entry(frame_create_matr_1)
        self.ent_y.pack(side='left')
        self.but = Button(frame_create_matr_1)
        self.but.config(text='Create Matrix', bg='red', height=2, width=23, command=self.create_matrix)
        self.but.pack(side='top', expand=False)
        Label(self.frame_widgets,
              text='Create Objects:',
              font='Arial 14').pack(side='top', expand=False)
        self.frame_create_obj_1 = Frame(self.frame_parent, bg='gray')
        self.frame_create_obj_1.pack(side='top', expand=False, fill='x')
        Label(self.frame_create_obj_1,
              text='Class',
              bg='gray',
              font='Arial 10').pack(side='left')
        self.ent_class = Entry(self.frame_create_obj_1)
        self.ent_class.pack(side='left')
        Label(self.frame_create_obj_1, text='Count',
              bg='gray',
              font='Arial 10').pack(side='left')
        self.ent_count = Entry(self.frame_create_obj_1)
        self.ent_count.pack(side='left')
        Label(self.frame_create_obj_1,
              text='IPP',
              bg='gray',
              font='Arial 10').pack(side='left')
        self.ent_IPP = Entry(self.frame_create_obj_1)
        self.ent_IPP.pack(side='left')
        self.but_create_obj = Button(self.frame_create_obj_1)
        self.but_create_obj.config(text='Create Objects', bg='red', height=2, command=self.create_objects)
        self.but_create_obj.pack(side='left')
        self.frameSSSD = Frame(self.frame_parent, bg='gray')
        self.frameSSSD.pack(side='top', expand=False, fill='x')
        Label(self.frameSSSD, text='Start, Stop, Save, Download:', font='Arial 14').pack(side='top', expand=False,
                                                                                         fill='x')
        self.but_start = Button(self.frameSSSD)
        self.but_start.config(text='Start', bg='red', width=10, command=self.start)
        self.but_start.pack(side='left')
        self.frame_1 = Frame(self.frameSSSD, width=6, bg='gray')
        self.frame_1.pack(side='left')
        self.but_stop = Button(self.frameSSSD)
        self.but_stop.config(text='Stop', bg='red', width=10, command=self.stop)
        self.but_stop.pack(side='left')
        self.frame_2 = Frame(self.frameSSSD, width=6, bg='gray')
        self.frame_2.pack(side='left')
        self.but_save = Button(self.frameSSSD)
        self.but_save.config(text='Save', bg='red', width=10, command=self.save)
        self.but_save.pack(side='left')
        self.frame_3 = Frame(self.frameSSSD, width=6, bg='gray')
        self.frame_3.pack(side='left')
        self.but_download = Button(self.frameSSSD)
        self.but_download.config(text='Download', bg='red', width=10, command=self.download)
        self.but_download.pack(side='left')
        self.frame_4 = Frame(self.frameSSSD, width=6, bg='gray')
        self.frame_4.pack(side='left')
        self.ent_file = Entry(self.frameSSSD, width=35)
        self.ent_file.pack(side='left')


    def create_matrix(self):
        self.x = int(self.ent_x.get())
        self.y = int(self.ent_y.get())
        self.game_controller = Controller(self.x, self.y)
        frame_mat = Frame(self.frame_child)
        frame_mat.pack(anchor=W)
        for y in range(self.y):
            frame_line = Frame(frame_mat)
            frame_line.pack(side='top')
            self.matrix.append([])
            for x in range(self.x):
                frame_elem = Frame(frame_line, bg='black', width=15, height=15)
                self.matrix[y].append(frame_elem)
                frame_elem.pack(side='left')

    def create_objects(self):
        if self.ent_IPP.get():
            self.IPP = self.ent_IPP.get()
        else:
            self.IPP = None
        if self.ent_count.get():
            self.count = int(self.ent_count.get())
        else:
            self.count = 0
        self.cls = self.ent_class.get()
        if self.ent_class.get():
            self.game_controller.create_objects(self.count, self.cls, self.IPP)
        self.refresh()

    def refresh(self):
        self.list_of_objects = self.game_controller.matrix.get_list_of_objects()
        for obj in (self.list_of_objects):
            x = obj.cor_x
            y = obj.cor_y
            self.change_color(x,y,obj.color)

    def change_color(self, x=0, y=0, color='black'):
        self.matrix[y][x].config(bg=color)

    def clean_matrix(self):
        for y in range(self.y):
            for x in range(self.x):
                self.change_color(x,y)

    def start(self):


    def stop(self):
        pass

    def save(self):
        pass

    def download(self):
        pass



root = Tk()
root.title('Matrix')

interface = Interface(root)
root.mainloop()



