def main():
    # 昇順にソートされた配列
    sorted_array = [1, 2, 3, 5, 12, 7890, 12345]
    # 探索対象の番号
    target_number = 7890
    # 探索実行
    target_index = serch_index(sorted_array, target_number)
    # 結果出力
    print(target_index)

def serch_index(sorted_array, target_number):
    
    # ここから記述
    
    # minはリストの左端
    min = 0
    # maxはリストの右端
    max = len(sorted_array) - 1
    # 探索領域の左端が右端の区間にいる間
    while min <= max:
        # 二分法を用いるため中間のmidを算出する。リストを指定したいためint型に変換
        mid = int((min + max) / 2)
        # リストの中間が探索対象に当てはまった時midを返す
        if sorted_array[mid] == target_number:
            return mid
        # リストの中間が選択対象より低い時midに1を足して次の範囲を探索する
        elif sorted_array[mid] < target_number:
            min = mid + 1
        # または、その反対は1を引いて前の範囲を探索する
        else:
            max = mid - 1
            
    # ここまで記述
    
    # 探索対象が存在しない場合、-1を返却
    return -1

if __name__ == '__main__':
    main()