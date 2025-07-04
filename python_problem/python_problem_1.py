def brGame(player, num):
    while True:
        count = input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능): ")
        if not count.isdigit():
            print("정수를 입력하세요")
        elif count == "1" or count == "2" or count == "3":
            count = int(count)
            break
        else:
            print("1,2,3 중 하나를 입력하세요")

    for i in range(count):
        num += 1
        print(f"{player} : {num}")
        if num == 31:
            print(f"{'playerB' if player == 'playerA' else 'playerA'} win!")
            break
    return num

num = 0

while num < 31:
    num = brGame("playerA", num)
    if num == 31:
        break

    num = brGame("playerB", num)
    if num == 31:
        break