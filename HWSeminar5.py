# Task 1
# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
# Создайте программу для игры с конфетами человек против человека.

# Решение////////////////////////////////////////////////////////////////

# print(' '.join(filter(lambda x: not 'абв' in x,'Мы неабв очень любим Питон иабв Джавуабв'.split())))

# Решение 2 ////////////////////////////////////////////////////////////////

# my_str = 'Мы неабв очень любим Питон иабв Джавуабв !'.split()

# print(' '.join([word for word in my_str if 'абв' not in word]))

# ///////////////////////////////////////////////////////////////////////

# Task 2
# Условие задачи: 
# На столе лежит 2021 конфета. 
# Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, 
# чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота

# b) Подумайте как наделить бота ""интеллектом""

# Решение////////////////////////////////////////////////////////////////

# count_of_candy = int(input('Введите количество конфет для игры: '))
# gamer_1, gamer_2 = input('Введите имя 1 игрока: '), input('Введите имя 2 игрока: ')
# current_gamer = gamer_1
# while count_of_candy > 0:
#     print('Количество оставшихся конфет: {}'.format(count_of_candy))
#     while True:
#         number_to_delete = int(input('Ход игрока {} (1 - 28): '.format(current_gamer)))
#         if number_to_delete >= 1 and number_to_delete <= 28:
#             break
#     count_of_candy-= number_to_delete
#     current_gamer = gamer_2 if current_gamer == gamer_1 else gamer_1

# print('Победил {}'.format(current_gamer))

# ///////////////////////////////////////////////////////////////////////

# Task 3
# Создайте программу для игры в ""Крестики-нолики"".
# Решение////////////////////////////////////////////////////////////////
# import pygame as pg 
# pg.init()

# def win_check(mas, sing):
#     zeroes = 0
#     for row in mas:
#         zeroes += row.count(0)
#         if row.count(sing) == 3:
#             return sing
#             print(1)
#     for col in range(3):
#         if mas[0][col] == sing and mas[1][col] == sing and mas[2][col] == sing:
#             return sing
#     if mas[0][0] == sing and mas[1][1] == sing and mas[2][2] == sing:
#         return sing
#     if mas[0][2] == sing and mas[1][1] == sing and mas[2][0] == sing:
#         return sing
#     if zeroes == 0:
#         return 'No win, No defeat'
#     return False


# sizeblock = 100
# margine = 15

# WIDTH = HEIGTH = sizeblock * 3 + margine * 4 
# RES = WIDTH, HEIGTH

# sc = pg.display.set_mode(RES)
# pg.display.set_caption('Крестики нолики!')

# clock = pg.time.Clock()

# FPS = 30

# BLACK = (0, 0, 0)
# WHITE = (255, 255, 255)
# ROZOVI = (189, 30, 128)
# FIOLETOVI = (125, 81, 196)
# NASROZOVI = (255,20,147)
# ORHID = (138,43,226)

# mas = [[0] * 3 for i in range(3)]
# query = 0

# while True:
#     sc.fill(BLACK)
#     for event in pg.event.get():
#         if event.type == pg.QUIT:
#             pg.quit()
#             quit()
#         elif event.type == pg.MOUSEBUTTONDOWN:
#             x_mouse, y_mouse = pg.mouse.get_pos()
#             col = x_mouse // (sizeblock + margine)
#             row = y_mouse // (sizeblock + margine)
#             if mas[col][row] == 0:
#                 if query % 2 == 0:
#                     mas[col][row] = 'x'
#                 else: 
#                     mas[col][row] = 'o'
#                 query += 1

#     for row in range(3):
#         for col in range(3):
#             if mas[col][row] == 'x':
#                 color = FIOLETOVI
#             elif mas[col][row] == 'o':
#                 color = ROZOVI
#             else:
#                 color = WHITE
#             x = col * sizeblock + (col + 1) * margine
#             y = row * sizeblock + (row + 1) * margine
#             pg.draw.rect(sc, color, (x, y, sizeblock, sizeblock))
#             if color == FIOLETOVI:
#                 pg.draw.line(sc, NASROZOVI, (x + 10, y + 10), (x + sizeblock - 10, y + sizeblock - 10), 5)
#                 pg.draw.line(sc, NASROZOVI, (x + sizeblock - 10, y + 10), (x + 10, y + sizeblock - 10), 5)
#             elif color == ROZOVI:
#                 pg.draw.circle(sc, ORHID, (x + sizeblock // 2, y + sizeblock // 2), sizeblock // 2 - 5, 5)
        
#         if (query - 1) % 2 == 0:
#             game_over = win_check(mas, 'x')
#         else:
#             game_over = win_check(mas, 'o')

#         if game_over:
#             sc.fill(BLACK)
#             font = pg.font.SysFont('Calibri', 45)
#             text1 = font.render(game_over, True, WHITE, 5)
#             text_rect = text1.get_rect()
#             text_x = sc.get_width() / 2 - text_rect.width / 2
#             text_y = sc.get_height() / 2 - text_rect.height / 2
#             sc.blit(text1, [text_x, text_y])

#     pg.display.update()
#     clock.tick(FPS)
# ///////////////////////////////////////////////////////////////////////

# Task 4
# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

# Решение////////////////////////////////////////////////////////////////
# def coding(txt):
#     count = 1
#     res = ''
#     for i in range(len(txt)-1):
#         if txt[i] == txt[i+1]:
#             count += 1
#         else:
#             res = res + str(count) + txt[i]
#             count = 1
#     if count > 1 or (txt[len(txt)-2] != txt[-1]):
#         res = res + str(count) + txt[-1]
#     return res

# def decoding(txt):
#     number = ''
#     res = ''
#     for i in range(len(txt)):
#         if not txt[i].isalpha():
#             number += txt[i]
#         else:
#             res = res + txt[i] * int(number)
#             number = ''
#     return res


# s = input("Введите текст для кодировки: ")
# print(f"Текст после кодировки: {coding(s)}")
# print(f"Текст после дешифровки: {decoding(coding(s))}")
# ///////////////////////////////////////////////////////////////////////