for num in range(1, 101):
    string = ''
    
    # ここから記述
    
    # 割る数を大きい順に実行しないと先に3割り切れる数が実行されてしまう為
    if num % 3 == 0 and num % 5 == 0:
        string += 'FizzBuzz'
    elif num % 5 == 0:
        string += 'Buzz'
    elif num % 3 == 0:
        string += 'Fizz'
    else:
        # numを文字列に変換
        string += str(num)
        
    # ここまで記述
    
    print(string)