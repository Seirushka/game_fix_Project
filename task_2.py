import csv

with open('game.csv', encoding='utf8') as file:
    reader = list(csv.reader(file, delimiter='$'))[1:]

    new_data = []

    for GameName, characters, nameError, date in reader:
        if GameName == 'Starfield':
            print(1)


'''
with open('game_new.csv', 'w', newline='', encoding='utf8') as file:
    writer = csv.writer(file, delimiter='$')
    writer.writerow(['GameName', 'characters', 'nameError', 'date'])
    writer.writerows(new_data)
'''