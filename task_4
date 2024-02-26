import csv


def bug_count(game):
    """
    Считает количество ошибок в игре
    :param game: Название игры
    :return: Количество ошибок
    """
    count = 0
    for line in lines:
        if game in line:
            count += 1
    return count

# Открывает файл
file = open('game.txt', encoding='utf8')
lines = [file.readline()[:-1].split('$') for _ in file]
lines.remove(lines[-1])

# Новая база данных игр
new_lines = []

# Добаляет счетчик ошибок в строку и обновляет базу данных
for element in lines:
    error_count = bug_count(element[0])
    element.append(str(error_count))
    new_lines.append(element[::-1])

new_lines.sort()
new_lines = new_lines[::-1]
new_lines = [line[::-1] for line in new_lines]

# Создает новый файл
with open('game_counter.csv', 'w', encoding='utf8', newline='') as file:
    writer = csv.writer(file, delimiter='$')
    writer.writerow(['GameName', 'characters', 'nameError', 'date', 'counter'])
    writer.writerows(new_lines)
