import random

# Генерируем случайное число от 1 до 100
number = random.randint(1, 100)
guesses_taken = 0

print("Добро пожаловать в игру 'Угадай число'!")

while True:
    # Запрашиваем у пользователя ввод числа
    guess = input("Введите число от 1 до 100: ")
    guess = int(guess)
    
    # Увеличиваем счетчик попыток
    guesses_taken += 1
    
    # Проверяем, угадал ли пользователь число
    if guess == number:
        print(f"Поздравляю, вы угадали число за {guesses_taken} попыток!")
        break
    elif guess < number:
        print("Загаданное число больше вашего.")
    else:
        print("Загаданное число меньше вашего.")
10
