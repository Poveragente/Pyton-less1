def is_year_leap(number):
   return True if number % 4 == 0 else False

numb = int(input("Введите год " ))
leap = is_year_leap(numb)
    
print(f"год {numb}: {leap}")
