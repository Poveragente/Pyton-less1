num = input("Введите номер: ")
num = "88005553535" 
#Делаем из строчки массив 
def get_part(index: int) -> str:
    if 0 <= index < len(num):
        return num[index]
    return ""
# Вызовы: каждый выводит свою часть (один символ)
for i in range(11):
    print(get_part(i))
