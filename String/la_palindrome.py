try:
    T = int(input())
    while T:
        value = input()
        str_len = len(value) // 2
        if str_len % 2 == 0:
            first_half = value[:str_len]
            second_half = value[str_len:]
        else:
            first_half = value[:str_len]
            second_half = value[str_len+1:]
        
        if sorted(first_half) == sorted(second_half):
            print("YES")
        else:
            print("NO")
        T -= 1
except Excepion as e:
    print(str(e))