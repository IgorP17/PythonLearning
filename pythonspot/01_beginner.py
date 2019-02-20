# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 21:40:41 2019

@author: Igor
"""

# Strings
print("=== Strings")
## Чего нить напечатем
s = "Just say hello world"
print(s)

## Ввод с клавиатуры
print("Здесь ввод с клавиатуры, закомменчен")
# keyboard_input = input("Enter smth: ")
# print("Input was = " + keyboard_input)

## Сравнение строк а может тернарный оператор???
s1 = "eq"
s2 = "eq"
if (s1 == s2): print("Compare s1 == s2 - true")
s2 = "hh"
if (s1 != s2): print("Compare s1 == s2 - false")

## Обращение к элементам строки
s = "Мамба хуамба"
print("== Обращение к элементам строки")
print("Строка = " + s)
print("Первый символ строки: " + s[0])
print("Второй символ строки: " + s[1])
print("Где то символы строки: " + s[1:7])
print("Откуда то и до конца символы строки: " + s[6:])
