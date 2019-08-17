import re


def findMatchV1(possibleMatches, crossword):
    crossword_length = len(crossword)
    possible_matches_by_length = [word for word in possibleMatches if len(word) == crossword_length]

    if len(possible_matches_by_length) == 1:
        return possible_matches_by_length[0]

    for word in possible_matches_by_length:
        crossword_splited = crossword.split('.')
        crossword_splited = [n for n in crossword_splited if n != ''].pop()
        crossword_position = word.find(crossword_splited)

        if crossword_position > -1:
            return word

        return ""


def findMatchV2(possibleMatches, crossword):
    crossword_length = len(crossword)
    possible_matches_by_length = [word for word in possibleMatches if len(word) == crossword_length]

    if len(possible_matches_by_length) == 1:
        return possible_matches_by_length[0]

    for word in possible_matches_by_length:
        letters = re.findall('\w+', crossword)

        if len(letters):
            crossword_position = word.find(letters.pop())

            if crossword_position > -1:
                return word

        return ""


possibleMatches = ['Abomasnow', 'Abra', 'Absol', 'Accelgor', 'Aegislash', 'Aerodactyl' 'Aggron', 'Aipom', 'Alomomola', 'Ambipom', 'Azurill', 'Bergmite', 'Bibarel', 'Bisharp']
crossword_list = ['...arel', 'Ab..', 'Ab...', '..sol', '...gmi..', '...ha..']

for crossword in crossword_list:
    print('----Using version 1 ----')
    result = findMatchV1(possibleMatches, crossword)
    print('Version 1 result:', result)

    print('----Using version 2 ----')
    result = findMatchV2(possibleMatches, crossword)
    print('Version 2 result:', result)
    print('-------------------------------')
