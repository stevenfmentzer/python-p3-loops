#!/usr/bin/env python3

def happy_new_year():
    countdown = 10
    while countdown >= 0:
        print(countdown)
        countdown-=1 
    print("Happy New Year!")

def square_integers(int_list):
    squared = []
    for num in int_list:
        num_square = num * num
        squared.append(num_square)
    return squared

def fizzbuzz():
    count = 1
    while count < 101: 
        if count % 3 == 0 and count % 5 == 0: 
            print("FizzBuzz")
        elif count % 3 == 0: 
            print("Fizz")
        elif count % 5 == 0: 
            print("Buzz")
        else: 
            print(count)
        count -= 1
