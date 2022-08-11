import random
a = 0 # number of player wins
b = 0 # number of bot wins
for i in range(3):
    print("Round№",1+1)
    player = int(input("Menu:\n1)rock\n2)paper\n3)scissors\nyour choice: "))
    bot = random.randint(1,3)
    if (player == 1 and bot == 1) or (player == 2 and bot == 2) or (player == 3) and (bot == 3):
        print("Draw")
    elif (player == 1 and bot == 2) or (player == 2 and bot == 3) or (player == 3) and (bot == 1):
        print("The player win")
        a = a + 1
    elif (player == 1 and bot == 3) or (player == 2 and bot == 1) or (player == 3) and (bot == 2):
        print("The bot win")
        b = b + 1
    v = input("Press Enter to go to the next round")
if a > b:
    print("Player wins with score",a,":",b)
elif a < b:
    print("Bot wins with a score",b,":",a)
