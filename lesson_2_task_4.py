def fizz_buzz(num):
    for i in range(1, num + 1):
        if i % 3 == 0 & i % 5 == 0:
            print(f"{i} - FizzBuzz")
        if i % 3 == 0:
            print(f"{i} - Fizz")
        if i % 5 == 0:  
            print(f"{i} - Buzz")
        else: print({i})

number = int(input("Введите число "))
print(fizz_buzz(number))

