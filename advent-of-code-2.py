# A B C opponent play
# X Y Z your play

# A Rock
# B Paper
# C Scissor

# X Rock 1
# Y Paper 2
# Z Scissor 3

# Draw
# A X
# B Y
# C Z

# Win
# A Y
# B Z
# C X

# Lose
# A Z
# B X
# C Y 

# X lose
# Y draw
# Z win


with open('advent-of-code-2.txt','r') as f:
    lines = f.readlines()
    opponent_play = []
    your_play= []
    for x in lines:
        game = x.split(' ')
        opponent_play.append(game[0])
        your_play.append(game[1].rstrip('\n'))
    
    games_list = list(zip(opponent_play,your_play))

    game_points = 0
    strategy_points = 0

    symbol_points = {'A':1,'B':2,'C':3}
    points_dict = {('A','X'):4,('B','Y'):5,('C','Z'):6,('A','Y'):8,('B','Z'):9,('C','X'):7, ('A','Z'):3,('B','X'):1,('C','Y'):2}
    win_lose_draw = {('A','X'):'C',('B','X'):'A',('C','X'):'B',('A','Y'):'A',('B','Y'):'B',('C','Y'):'C', ('A','Z'):'B',('B','Z'):'C',('C','Z'):'A'}
    win_lose_draw_points = {'X' :0,'Y':3,'Z':6}


    for game in games_list:
        game_points += points_dict[game]

    for game in games_list:
        strategy_points += win_lose_draw_points[game[1]] + symbol_points[win_lose_draw[game]]
        
        

    print(game_points)
    print(strategy_points)