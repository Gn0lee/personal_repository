import sys
import copy
times = int(sys.stdin.readline())

array = [list(map(int,sys.stdin.readline().split())) for i in range(times)]

final_area_num = [0]*102
 

for height in range(0,102):
    
    counting_arr = [ [(0,0)] + list(map(lambda x: (x+1,1) if array[i][x] > height else (x+1,0),range(times))) for i in range(times)]
    first_area = []
    cal_arr = []
    area = set()
    area2 = set()
    for i in counting_arr[0][::-1]:
        
        if i[1] != 0:
            area.add(counting_arr[0].pop())
            continue
        else:
            del counting_arr[0][-1]
            if area == set():
                continue
            else:
                first_area.append(area)
                area = set()

    index_arr = copy.deepcopy(first_area)
    first_num = len(first_area)
    for i in range(1,times):
        
        after_safe_area = []
        for k in counting_arr[i][::-1]:
            if k[1] != 0:
                area2.add(counting_arr[i].pop())
                continue
            else:
                del counting_arr[i][-1]
                if area2 == set():
                    continue
                else:
                    after_safe_area.append(area2)
                    area2 = set()
        if len(after_safe_area) != 0:
            
            for a in range(len(index_arr)):
                for b in range(len(after_safe_area)):
                    # if (after_safe_area[b].isdisjoint(index_arr[a]) == False):
                    #     break
                    # elif after_safe_area[b].isdisjoint(index_arr[a]) == True and b < len(after_safe_area)-1:
                    #     continue
                    # elif after_safe_area[b].isdisjoint(index_arr[a]) == True and b == len(after_safe_area)-1:
                    #     first_num += 1
                    if (after_safe_area[b].isdisjoint(index_arr[a]) == True):
                        if b < len(after_safe_area)-1:
                            continue
                        else:
                            first_num += 1
                    else :
                        break
        else:
            first_num += len(index_arr)
        index_arr = copy.deepcopy(after_safe_area)
    
    # area2 == set()
    # after_safe_area = []
    # for x in counting_arr[-2][::-1]:
    #     if x[1] != 0:
    #         area2.add(counting_arr[-2].pop())
    #         continue
    #     else:
    #         del counting_arr[-2][-1]
    #         if area2 == set():
    #             continue
    #         else:
    #             after_safe_area.append(area2)
    #             area2 = set()
    # # if len(after_safe_area) == 0:
    # #         after_safe_area = [{(0,1)}]
    # if len(after_safe_area) != 0:
    #     for a in range(len(after_safe_area)):
    #         for b in range(len(index_arr)):
    #             if (after_safe_area[a].isdisjoint(index_arr[b]) == True):
    #                     if b < len(after_safe_area)-1:
    #                         continue
    #                     else:
    #                         first_num += 1
    #             else :
    #                 break
    # else:
    #     first_num += len(index_arr)
    #     print(index_arr,"\t\t\t\t {} 째  합집합후".format(i))
    # print("높이 {}의 안전구역 수는 {}".format(height, len(index_arr)))
    # print(first_num, "\t\t 높이 {}의 안전구역 개수".format(height))
    final_area_num[height] = first_num
print(max(final_area_num))    
    
