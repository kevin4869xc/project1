import random

def play_one():
    min = 0
    max = 100
    count = 0
    random_value = random.randint(min,max)
    print(random_value)

    if __name__ == "__main__":

        print("==========猜數字遊戲==========")
        while True:
            keyin = eval(input(f"請輸入{min}~{max}的數字"))
            count += 1
            if keyin >= min and keyin <= max:
                if keyin == random_value:
                    print(f"猜對了，共猜了{count}次")
                    break
                elif keyin > random_value:
                    print("再小一點")
                    max = keyin - 1
                elif keyin < random_value:
                    print("再大一點")
                    min = keyin + 1    
                print(f"猜錯了, 已猜了{count}次")
            else:
                print(f"超出範圍, 已猜了{count}次")

def play_game():
    while True:
        play_one()
        play_again = input("是否要繼續玩(y,n)")
        if play_again.lower() == "n":
            break

if __name__ == "__main__":
    play_game()
