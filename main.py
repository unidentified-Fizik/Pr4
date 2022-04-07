# #------------№1\
# import sys
# import random
# import re
#
# dict_sample = {1:[random.randint(1,5),random.randint(1,5),random.randint(1,5)],
#                2:[random.randint(3,8),random.randint(1,8),random.randint(1,9)]}
#
#
#
# print(dict_sample)
# x = dict_sample
# # print("Введите 1 или 2")
# # dict_sample[input()] = [random.randint(1,3)]
# # print(dict_sample)
# # print(len(dict_sample))
#
# def Add(x):
#     dict_sample[input()]=[random.randint(3,5)]
#     print(x)
#     return dict_sample
#
#
# Add(x)
#
#
# print(re.findall(r':',dict_sample))


# Номер 1 хороший вид
# class Hash:
#     table = []
#
#     def __init__(self, key=None, value=None):
#         if key is None and value is None:
#             self.table = []
#         else:
#             self.key = key
#             self.value = value
#
#     def get_key(self):
#         return self.key
#
#     def set_key(self, new_key):
#         self.key = new_key
#
#     def get_value(self):
#         return self.value
#
#     def get_by_index(self, item):
#         return self.table.__getitem__(item)
#
#     def get_size(self):
#         return len(self.table)
#
#     def get_obj(self, index):
#         return self.table.__getitem__(index)
#
#     def set_value(self, new_value):
#         self.value = new_value
#
#     def add_item(self, element):
#         self.table.append(element)
#
#     def output(self):
#         for e in self.table:
#             print("Key - " + str(e.get_key()) + "; Value - " + str(e.get_value()))
#
#     def find_by_key(self, key):
#         for e in self.table:
#             if e.get_key() == key:
#                 print("Key - " + str(e.get_key()) + "; Value - "
#                       + str(e.get_value()))
#
#     def find_by_value(self, value):
#         for e in self.table:
#             if e.get_value() == value:
#                 print("Key - " + str(e.get_key()) + "; Value - "
#                       + str(e.get_value()))
#
#     def change_key(self, element, new_key):
#         for e in self.table:
#             if element.get_value() == e.get_value():
#                 e.set_key(new_key)
#
#     def change_value(self, element, new_value):
#         for e in self.table:
#             if element.get_key() == e.get_key():
#                 e.set_value(new_value)
#
#     def remove_item(self, index):
#         self.table.remove(index)
#
#
# table = Hash()
# table.add_item(Hash(12, 3))
# table.add_item(Hash(14, 2))
# table.add_item(Hash(15, 1))
# table.add_item(Hash('df', "sdf5"))
# table.output()
# table.remove_item(table.get_obj(0))
# print("")
# table.output()
# print("")
# for i in range(0, table.get_size()):
#     print(table.get_by_index(i).get_value())
# print("")
#
# table.find_by_key(12)
# table.find_by_value("sdf5")




# #-------------2
#
# class MyClass():
#     x=2
#     y=3
#
#     def summ(self, x, y):
#         self.x = x
#         self.y = y
#         self.sum=x+y
#
#     def Peremen(self):
#         print(self.__dict__)
#
# pt = MyClass()
# pt.x = 6
# pt.y = 5
# pt.Peremen()
# pt.summ(4,5)
# print(pt.__dict__)
# print(dir(pt))

# ----------------3
#
# class A:
#     pass
#
#
# class B(A):
#     pass
#
# class C(B,A): # Ошибка в том , что класс B  уже включает класс А и его не нужно повторно ключать .
# pass






 # # Номер 5
# class HTML:
#     resultCode = []
#     tab = ''
#
#     def __init__(self):
#         HTML.resultCode = []
#
#     class body:
#
#         def __enter__(self):
#             HTML.resultCode.append("<body>")
#             HTML.tab += '    '
#
#         def __exit__(self, *args, **kwargs):
#             HTML.resultCode.append("</body>")
#
#     class div:
#         count = 0
#
#         def __enter__(self):
#             HTML.resultCode.append(HTML.tab + "<div>")
#             HTML.tab += '    '
#
#         def __exit__(self, *args, **kwargs):
#             self.count += 1
#             for i in range(0, self.count):
#                 HTML.tab = HTML.tab[:-4]
#             HTML.resultCode.append(HTML.tab + "</div>")
#
#     def p(self, value):
#         tag = HTML.tab + "<p>" + value + "</p>"
#         HTML.resultCode.append(tag)
#
#     def get_code(self):
#         result = ''
#         for item in HTML.resultCode:
#             result += item
#             result += '\n'
#
#         return result
#
#
# html = HTML()
# with html.body():
#     with html.div():
#         with html.div():
#             html.p('Первая строка.')
#             html.p('Вторая строка.')
#         with html.div():
#             html.p('Третья строка.')
#             with html.div():
#                 html.p('opop')
#     with html.div():
#         html.p('sdfjfsjsjfjnf')
#
# print(html.get_code())





# #-------------8
# from tkinter import Tk, Canvas, Frame, BOTH
#
#
# class Example(Frame):
#
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#
#     def initUI(self):
#         self.master.title("Castl")
#         self.pack(fill=BOTH, expand=1)
#
#         canvas = Canvas(self)
#
#
#
#
#         # Рисуем прямоугольник.
#         canvas.create_rectangle(
#             100, 110, 120, 120,
#             outline="#f11", width=2
#         )
#
#         #Рисуем Линии
#         canvas.create_line(120,120,140,120)
#
#         # Рисуем прямоугольник.
#         canvas.create_rectangle(
#             140, 110, 160, 120,
#             outline="#f11", width=2
#         )
#         # Рисуем Линии
#         canvas.create_line(160, 120, 180, 120)
#
#         # Рисуем прямоугольник.
#         canvas.create_rectangle(
#             180, 110, 200, 120,
#             outline="#f11", width=2
#         )
#         # Рисуем Линии
#         canvas.create_line(200, 120, 220, 120)
#
#         # Рисуем прямоугольник.
#         canvas.create_rectangle(
#             220, 110, 240, 120,
#             outline="#f11", width=2
#         )
#         # Рисуем Линии башню сделаю линиями , позже нужно запизнуть в цикл
#         canvas.create_line(240, 110, 240, 100)
#         canvas.create_line(240, 100, 270, 100)
#         canvas.create_line(270, 100, 270, 110)
#         canvas.create_line(270, 110, 290, 110)
#         canvas.create_line(290, 110, 290, 100)
#         canvas.create_line(290, 100, 310, 100)
#         canvas.create_line(310, 100, 310, 300)
#         canvas.create_line(310, 300, 100, 300)
#         canvas.create_line(100, 300, 100, 120)
#
#         #Рисую линии и ккирпичную кладку через них
#         x0=100
#         x1=130
#         x2=130
#         x3=160
#         canvas.create_line(100, 180, 130, 180)
#         for i in range(0,3):
#             x1+=60
#             x0+=60
#             canvas.create_line(x0, 180, x1, 180)
#             canvas.create_line(130, 180, 130, 150)
#             for i in range(0,2):
#                 canvas.create_line(x1, 180,x1, 150)
#                 canvas.create_line(x0,180,x0,150)
#         for i in range(0,3):
#             canvas.create_line(x2, 150, x3, 150)
#             x2+=60
#             x3+=60
#
#
# #второй слой кирпичной кладки
#         x0 = 100
#         x1 = 130
#         x2 = 130
#         x3 = 160
#         canvas.create_line(100, 230, 130, 230)
#         for i in range(0, 3):
#             x1 += 60
#             x0 += 60
#             canvas.create_line(x0, 230, x1, 230)
#             canvas.create_line(130, 220, 130, 200)
#             for i in range(0, 2):
#                 canvas.create_line(x1, 230, x1, 200)
#                 canvas.create_line(x0, 230, x0, 200)
#         for i in range(0, 3):
#             canvas.create_line(x2, 200, x3, 200)
#             x2 += 60
#             x3 += 60
#
#
# # тритий слой кладки
#         canvas.create_line(100, 270, 130, 270)
#         canvas.create_line(160, 270, 190, 270)
#         canvas.create_line(220, 270, 250, 270)
#         canvas.create_line(280, 270, 310, 270)
#         canvas.create_line(130, 270, 130, 240)
#         canvas.create_line(160, 270, 160, 240)
#         canvas.create_line(190, 270, 190, 240)
#         canvas.create_line(250, 270, 250, 240)
#         canvas.create_line(220, 270, 220, 240)
#         canvas.create_line(280, 270, 280, 240)
#         canvas.create_line(130, 240, 160, 240)
#         canvas.create_line(190, 240, 220, 240)
#         canvas.create_line(250, 240, 280, 240)
#         canvas.create_line(240, 120, 240, 300)
#
#
# # МОСТ
# #         canvas.create_arc(
# #             330, 280, 400, 350, start=0,
# #             extent=210, width=2
# #         )
#         canvas.create_arc(330, 280, 390, 350,
#                      start=0, extent=180,
#                     outline='darkblue',
#                      width=5)
#         canvas.create_line(330,300,350,320)
#         canvas.create_line(350, 280, 350, 320)
#         canvas.create_line(390, 320, 350, 280)
#
#         canvas.create_line(120, 380, 330, 350)
#         canvas.create_line(120, 320, 335, 300)
#
#         canvas.create_line(120, 320, 120, 380)
#         canvas.create_line(335, 320, 120, 380)
#         canvas.create_line(335, 340, 335, 300)
#
#
#
#         # Wood - это точки для создания многоугольника, тут можно сделать треуголник и из нескольких ёлку,
            # там по 3 одинаковые координаты 2-раза и две одинаковые для получения треугольника
#
#
#
#         points = [
#             350, 250, 380,
#             380, 350, 350, 250, 380
#         ]
#
#         # Рисуем многоугольник.
#
#         canvas.create_polygon(points, outline='#f11',
#                               fill='#1f1', width=2)
#
#
#         canvas.pack(fill=BOTH, expand=1)
#
#
# def main():
#     root = Tk()
#     ex = Example()
#     root.geometry("500x300+300+300")
#     root.mainloop()
#
#
# if __name__ == '__main__':
#     main()