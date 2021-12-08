a = [0,0,0,0]
b = 900
answer = ''
temp = []
for i in a:
    if i<10:
        temp.append([str(i),i*1111])
    elif i<100:
        j = str(i)
        temp.append([j,int(j*2)])
    elif i<1000:
        j = str(i)
        temp.append([j,int(j+j[0])])
    else:
        temp.append([str(i),i])

temp.sort(key=lambda x: (x[1]),reverse=True)

for k in temp:
    answer += k[0]

print(temp)
print(answer)