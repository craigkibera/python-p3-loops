#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    pass
    countdown = 10  # Start counting down from 10
    while countdown >= 1:  # Continue looping while countdown is greater than or equal to 1
        print(countdown)  # Print the current countdown number
        countdown -= 1  # Decrement the countdown by 1
    print("Happy New Year!")  # Print "Happy New Year!" after the loop finishes

happy_new_year()

    

def square_integers(int_list):
    # code goes here!
    pass
    return [num ** 2 for num in int_list]

def fizzbuzz():
    # code goes here!
    pass
    for num in range(1, 101):  
        if num % 3 == 0 and num % 5 == 0:  
            print("FizzBuzz")
        elif num % 3 == 0:  
            print("Fizz")
        elif num % 5 == 0:  
            print("Buzz")
        else:  
            print(num)


fizzbuzz()
