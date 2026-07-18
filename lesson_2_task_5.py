months_groups = [
    [12, 1, 2],    # Зима
    [3, 4, 5],     # Весна
    [6, 7, 8],     # Лето
    [9, 10, 11]    # Осень
]
season_names = ["Зима", "Весна", "Лето", "Осень"]

month = int(input("Введите номер месяца (1–12): "))

season_found = None
for i, group in enumerate(months_groups):
    if month in group:
        season_found = season_names[i]
        break

if season_found:
    print(season_found)
else:
    print("Неверный номер месяца")
