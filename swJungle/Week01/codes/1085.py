coordinates_list = input().split()
x = int(coordinates_list[0])
y = int(coordinates_list[1])
w = int(coordinates_list[2])
h = int(coordinates_list[3])
vales_list = [x,y,w-x,h-y]
print(min(vales_list))