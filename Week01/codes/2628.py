rec_list = input().split()
rec_x_len = int(rec_list[0])
rec_y_len = int(rec_list[1])
cut_nums = int(input())
cuts_list = []
cuts_x_list =[]
cuts_y_list = []

for cut_num in range(cut_nums):
    cuts_list.append(input().split())
for cut_list in cuts_list:
    if(cut_list[0] == "0"):
        cuts_x_list.append(int(cut_list[1]))
    else:
        cuts_y_list.append(int(cut_list[1]))

# print(cuts_x_list)
# print(cuts_y_list)
x1_list = cuts_x_list + [0]
x1_list.sort()
x2_list = cuts_x_list + [rec_y_len]
x2_list.sort()
# print(x1_list)
# print(x2_list)
y1_list = cuts_y_list + [0]
y1_list.sort()
y2_list = cuts_y_list + [rec_x_len]
y2_list.sort()
# print(y1_list)
# print(y2_list)
dif_x = []
dif_y = []

for i in range(len(x1_list)):
    dif_x.append(x2_list[i]-x1_list[i])
for i in range(len(y1_list)):
    dif_y.append(y2_list[i]-y1_list[i])

print(max(dif_x) * max(dif_y))