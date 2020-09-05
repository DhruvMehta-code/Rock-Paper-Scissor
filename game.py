import random 
print('"****Please Read Instruction****"')
print("For Rock Please Type R")
print("For Paper Please Type P")
print("For Scissor Please Type S")
print("")
while True:
    n = input("Do you want to play Rock Paper Scissor [y/n] ? \n")
    if n == "y" or n == "Y":
        game_list = ["R", "P" ,"S","r","p","s"]
        select = random.choice(game_list)
        print("")
        word = input("Enter R,S or P: ")
        if  (word == "R") or (word == "S") or (word == "P") or (word == "r") or (word == "s") or (word == "p"):
            if select == word:
                print("draw !! computer also choose",word)
                print("")
                continue
            else:
                if select == "R" or select == "r":
                    if (select == "R" or select == "r") and (word == "s" or word == "S"):
                        print("You Lost !!! computer choose", select)
                        print("")
                        continue
                    if (select == "R" or select == "r") and (word == "p" or word == "P"):
                        print("You Won !!! computer choose", select)
                        print("")
                        continue
                elif select == "P" or select == "p":
                    if (select == "p" or select == "P") and (word == "s" or word == "S"):
                        print("You Won !!! computer choose", select)
                        print("")
                        continue
                    if (select == "p" or select == "p") and (word == "r" or word == "R"):
                        print("You Lost !!! computer choose", select)
                        print("")
                        continue
                else:
                    if (select == "S" or select == "s") and (word == "p" or word == "P"):
                        print("You Lost !!! computer choose", select)
                        print("")
                        continue
                    if (select == "s" or select == "S") and (word == "r" or word == "R"):
                        print("You Won !!! computer choose", select)
                        print("")
                        continue
        else:
            print("Enter proper letter give in instruction")
            print("")
            continue
    else:
        exit()
