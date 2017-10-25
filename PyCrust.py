count = 1
while count <= 5:
    print(count)
    count += 1
# 1
# 2
# 3
# 4
# 5

while True:
    value = input("String to capitalize [type q to quit]: ")
    if value == "q":    # q 종료
        break
    number = int(value)
    if number % 2 == 0: # 짝수
        continue
    print(number, "squared is", number * number)
# String to capitalize [type q to quit]: 1
# 1 squared is 1
# String to capitalize [type q to quit]: 2
# String to capitalize [type q to quit]: 3
# 3 squared is 9
# String to capitalize [type q to quit]: 4
# String to capitalize [type q to quit]: 5
# 5 squared is 25
# String to capitalize [type q to quit]: q
#
# Process finished with exit code 0