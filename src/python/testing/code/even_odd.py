def even_odd(list):
    odd_num = []
    even_num = []
    for num in list:
        if num %2 ==0 :
            even_num.append(num)
        else:
            odd_num.append(num)
            
    return print( f"odd list is{odd_num}"),print( f"even list is{even_num}")