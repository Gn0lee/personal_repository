from functools import reduce
heights_list = []
for i in range(9):
    height = int(input())
    heights_list.append(height)

# heights_list = [2,4,5,8,3,7]

factor = reduce(lambda x, y : x + y,heights_list) - 100
notMembers = []

for i in range(9):
    if(len(notMembers) == 0):
        for j in range(9):
            if (i != j):
                sum = heights_list[i]+heights_list[j]
                if(sum == factor):
                    notMembers.append(heights_list[i])
                    notMembers.append(heights_list[j])
                    break
    else:
        break

heights_list.remove(notMembers[0])
heights_list.remove(notMembers[1])
heights_list.sort()
for i in range(7):
    print(heights_list[i])