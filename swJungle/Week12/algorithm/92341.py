from collections import defaultdict
import math
def solution(fees, records):
    answer = []
    records_by_car = defaultdict(list)
    fees_by_car = defaultdict(int)
    
    
    for record in records:
        time , car_num , x = map(str,record.split())
        
        hour , minute = int(time[0:2]),int(time[3:5])
        
        records_by_car[int(car_num)].append(hour*60+minute)
    
    for key , value in records_by_car.items():
        if len(value) % 2 == 1:
            value.append(23*60+59)
            
        tmp = 0
        for i in range(0,len(value)//2 + 1,2):
            tmp += value[i+1] - value[i]
        
        if tmp<= fees[0]:
            cost = fees[1]
        else:
            cost = fees[1] + (math.ceil(((tmp-fees[0])/fees[2])) * fees[3])
            
        fees_by_car[key] = cost
   
    for j in sorted(fees_by_car.keys()):
        answer.append(fees_by_car[j])
    
    return answer

print(solution([180, 5000, 10, 600],["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))

from collections import defaultdict
import math
def solution(fees, records):
    answer = []
    records_by_car = defaultdict(list)
    fees_by_car = defaultdict(lambda : 0)
    
    
    for record in records:
        time , car_num , x = map(str,record.split())
        
        hour , minute = int(time[0:2]),int(time[3:5])
        
        records_by_car[int(car_num)].append(hour*60+minute)
        
    for record in records:
        time , car_num , x = map(str,record.split())
        
        hour , minute = int(time[0:2]),int(time[3:5])
        
        # records_by_car[int(car_num)].append(hour*60+minute)
        
        if x == "IN":
            fees_by_car[int(car_num)] += 1439 - (hour*60+minute)
        else:
            fees_by_car[int(car_num)] -= 1439 - (hour*60+minute)
    
#     for key , value in records_by_car.items():
#         if len(value) % 2 == 1:
#             value.append(23*60+59)
#         tmp = 0
#         for i in range(0,len(value)//2 + 1,2):
#             tmp += value[i+1] - value[i]
        
#         if tmp<= fees[0]:
#             cost = fees[1]
#         else:
#             cost = fees[1] + (math.ceil(((tmp-fees[0])/fees[2])) * fees[3])
            
#         fees_by_car[key] = cost

   
    for j in sorted(fees_by_car.keys()):
        total = fees_by_car[j]
        if total <= fees[0]:
            answer.append(fees[1])
        else:
            answer.append(fees[1] + (math.ceil(((total-fees[0])/fees[2])) * fees[3]))
    
    return answer