import sys
def game_start():
        exit = 0
        used_space = list()
        for i in range(5):
            used_space.append(player1())
            user1_move = used_space[-1]
            if used_space.count(user1_move) == 2:
                print("You can't do that!")
                break
            print()
            if i != 4:
                used_space.append(player2())
                user2_move = used_space[-1]
                if used_space.count(user2_move) == 2:
                        print("You can't do that!")
                        break
        if i == 4:
            print("The match was a draw!")
                
                
def player1():
    player1 = input("User1 choice: ")
    if player1 not in ['a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3']:
        print("invalid move! restart again")
        sys.exit()
    catch_list = user1_choice(player1)
    # The below code is to check xxx combo
    # this one is to check for horizontal
    for ma in range(3):
        Str = ''
        for mb in range(3):
            Str += catch_list[ma][mb]
        if Str == "xxx":
            print("Player 1 you won!")
            sys.exit()
            break
            # print(Dict[ma][mb])
    # this is for vertical 
    for ma in range(3):
        Str = ''
        for mb in range(3):
            Str += catch_list[mb][ma]
        if Str == "xxx":
            print("Player 1 you won!")
            sys.exit()
            break
    # this is for diagonal
    Str = ''
    for ma in range(3): #this is for \ diagonal
        Str += catch_list[ma][ma]
    if Str == "xxx":
        print("Player 1 you won!")
        sys.exit()
    Str = ''
    for ma in range(3): 
        Str += catch_list[2-ma][ma]   
    if Str == "xxx":
        print("Player 1 you won!")
        sys.exit()
    return player1

def player2():
    player2 = input("User2 choice: ")
    if player2 not in ['a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3']:
        print("invalid move! restart again")
        sys.exit()
    catch_list = user2_choice(player2)
    # The below code is to check OOO combo
    # this one is to check for horizontal
    for ma in range(3):
        Str = ''
        for mb in range(3):
            Str += catch_list[ma][mb]
        if Str == "OOO":
            print("Player 2 you won!")
            sys.exit()
            break
            # print(Dict[ma][mb])
    # this is for vertical 
    for ma in range(3):
        Str = ''
        for mb in range(3):
            Str += catch_list[mb][ma]
        if Str == "OOO":
            print("Player 2 you won!")
            sys.exit()
            break
    # this is for diagonal
    Str = ''
    for ma in range(3): #this is for \ diagonal
        Str += catch_list[ma][ma]
    if Str == "OOO":
        print("Player 2 you won!")
        sys.exit()
    Str = ''
    for ma in range(3): 
        Str += catch_list[2-ma][ma]   
    if Str == "OOO":
        print("Player 2 you won!")
        sys.exit()
    return player2
                        
def user1_choice(user1):
        Dict[user1] = 'x'
        L = [
        [Dict['a3'], Dict['b3'], Dict['c3']], 
        [Dict['a2'], Dict['b2'], Dict['c2']], 
        [Dict['a1'], Dict['b1'], Dict['c1']]
        ]
        # Str = ''
        # for ma in range(3):
        #     for mb in range(3):
        #          Str += L[ma][mb]
        # print(Str)
        # print(Dict)
        print(f"3  {L[0][0]} | {L[0][1]} | {L[0][2]} ")
        print("  -----------")
        print(f"2  {L[1][0]} | {L[1][1]} | {L[1][2]} ")
        print("  -----------")
        print(f"1  {L[2][0]} | {L[2][1]} | {L[2][2]} ")
        print("   a   b   c")
        return L   


def user2_choice(user2):
        Dict[user2] = 'O'
        L = [
        [Dict['a3'], Dict['b3'], Dict['c3']], 
        [Dict['a2'], Dict['b2'], Dict['c2']], 
        [Dict['a1'], Dict['b1'], Dict['c1']]
        ]
        # print(Dict)
        print(f"3  {L[0][0]} | {L[0][1]} | {L[0][2]} ")
        print("  -----------")
        print(f"2  {L[1][0]} | {L[1][1]} | {L[1][2]} ")
        print("  -----------")
        print(f"1  {L[2][0]} | {L[2][1]} | {L[2][2]} ")
        print("   a   b   c")
        return L  
            
Dict = {'a1': "-", 'a2': "-", 'a3': "-", 'b1': "-", 'b2': "-", 'b3': "-", 'c1': "-", 'c2': "-", 'c3': "-"}
L = [
    [Dict['a3'], Dict['b3'], Dict['c3']], 
    [Dict['a2'], Dict['b2'], Dict['c2']], 
    [Dict['a1'], Dict['b1'], Dict['c1']]
]

# for row in L:
#     print(row)

print(f"3  {L[0][0]} | {L[0][1]} | {L[0][2]} ")
print("  -----------")
print(f"2  {L[1][0]} | {L[1][1]} | {L[1][2]} ")
print("  -----------")
print(f"1  {L[2][0]} | {L[2][1]} | {L[2][2]} ")
print("   a   b   c")

print("please use grid notation like a1 b2 c3 etc")
game_start()       
        

# L = [
#     [Dict['a3'], Dict['b3'], Dict['c3']], 
#     [Dict['a2'], Dict['b2'], Dict['c2']], 
#     [Dict['a1'], Dict['b1'], Dict['c1']]
# ]

# print(Dict)
# for row in L:
#     print(row)
