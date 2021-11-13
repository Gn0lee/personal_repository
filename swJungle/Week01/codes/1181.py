times = int(input())
words_list = []
words_info_list = []
for i in range(times):
    word = input()
    if(word not in words_list):
        words_list.append(word)
        word_info = (len(word),word)
        words_info_list.append(word_info)        
    else:
        continue
words_info_list.sort(key=lambda x :(x[0],x[1]))
for word in words_info_list:
    print(word[1])