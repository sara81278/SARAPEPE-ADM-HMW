def minion_game(string):
    cPoints = minion_game_consonant(string)
    vPoints = minion_game_vowel(string)
    if(cPoints == vPoints):
        print('Draw')
    else:
        print(*max([('Stuart',cPoints),('Kevin', vPoints)],
            key = lambda k: k[1]))

def minion_game_consonant(string):
    points = 0
    for i in range(0,len(string)):
        if(not (s[i].upper() in "AEIOU")):
            points = points + len(string)-i
    return points

def minion_game_vowel(string):
    points = 0
    for i in range(0,len(string)):
        if(s[i].upper() in "AEIOU"):
            points = points + len(string)-i
    return points

