def main():
    #ランダムに並べられた重複のない整数の配列
    array = [5, 4, 6, 2, 1, 9, 8, 3, 7, 10]
    # ソート実行
    sortedArray = sort(array)
    # 結果出力
    [print(i) for i in sortedArray]

def sort(array):
    # 要素が一つの場合はソートの必要がないので、そのまま返却
    # 1以下のリストが存在したので==を<=に変更しました。
    if len(array) <= 1:
        return array

    # 配列の先頭を基準値とする
    pivot = array[0]
    
    # ここから記述
    
    # 空リストの作成
    arr_left = []
    arr_right = []
    # 初期値の設定
    p_count = 0
    
    # pivot以上と未満を分ける
    for arr in array:
        if arr < pivot:
            arr_left.append(arr)
        elif arr > pivot:
            arr_right.append(arr)
        # pivotと同値なら数える(最終的にpivotは1になり、必然的に初めのpivotに帰着する)
        else:
            p_count += 1
    
    # 繰り返し
    arr_left = sort(arr_left)
    arr_right = sort(arr_right)
    # 並べ替えが終了したリストをまとめる
    return arr_left + [pivot] * p_count + arr_right
    
    # ここまで記述 
if __name__ == '__main__':
    main()