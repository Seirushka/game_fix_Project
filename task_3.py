character_name = input()
while character_name != 'game':
    file = open('game.txt', encoding='utf8')
    lines = [file.readline()[:-1].split('$') for _ in file]
    lines.remove(lines[-1])

    list_games = []

    for line in lines:
        if line[1] == character_name:
            list_games.append(line[0])

    if len(list_games) > 0:
        print(f"Персонаж {character_name} встречается в играх:")
        count = 0
        for game in list_games:
            #if count < 5:
            print(game)
            count += 1
            #else:
            #    print('и др.')
            #    break
    else:
        print('Этого персонажа не существует')

    character_name = input()
