index_arr =[{(7, 1), (2, 1), (3, 1), (6, 1)},{ (1, 1), (5, 1), (4, 1)}]
after_safe_area = [{(7, 1)}, {(1, 1)}]
first_num = len(index_arr)

for a in range(len(after_safe_area)):
    for b in range(len(index_arr)):
        if (after_safe_area[a].isdisjoint(index_arr[b]) == False):
            first_num -= 1 
    first_num += 1
print(first_num)