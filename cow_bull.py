num_list = [0,1,2,3,4,5,6,7,8,9]
guesed_list = []
reuse_list = []
def random_number():
    import random
    to_guess_num = []
    i = 1
    while True:
        n = random.randint(0,9)
        if n not in to_guess_num:
            to_guess_num.append(n)
            if len(to_guess_num) == 5:
                break
        i+=1
   return to_guess_num
def cow_bull():
    print("wellcome to game")
#     print("we have these numbers to guess")
    to_guess_num = random_number()
    for i in range(0,10):
        guess = int(input("enter guess number:-"))
        position = int(input("enter the position b/w 1 to 5:-"))
        if guess in reuse_list:
            reuse_list.remove(guess)
        if guess in to_guess_num:
            i = 0
            while i < len(to_guess_num):
                if to_guess_num[i] == guess:
                    pos = i
                    if position == pos:
                        print("bull")
                        guesed_list.insert(position,guess)
                    else:
                        print("cow")
                        reuse_list.append(guess)
                        print("you can reuse these numbers",reuse_list)
                i+=1
        else:
            print("wrong guess")
    if guesed_list == to_guess_num:
        print("you won the game")
    else:
        print("oops you lost the game")
while True:
    cow_bull()
    wish = input("do you want to play again,selct y/n:")
    if wish == "y":
        cow_bull()
    else:
        break
  
  
