import csv

with open('game.csv', encoding='utf8') as file:
    reader = list(csv.reader(file, delimiter='$'))[1:]

    new_data = []

    for GameName, characters, nameError, date in reader:
        if '55' in nameError:
            warning = (f"У персонажа {characters} в игре {GameName} нашлась ошибка с кодом: {nameError}. "
                       f"Дата фиксации: {date}")
            nameError = 'Done'
            date = '0000-00-00'
            print(warning)
        new_data.append([GameName, characters, nameError, date])

with open('game_new.csv', 'w', newline='', encoding='utf8') as file:
    writer = csv.writer(file, delimiter='$')
    writer.writerow(['GameName', 'characters', 'nameError', 'date'])
    writer.writerows(new_data)
