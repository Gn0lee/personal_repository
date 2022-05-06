from itertools import permutations

def solution(user_id, banned_id):
    
    def chk(users):
        for user, ban in zip(users, banned_id):
            if len(user) != len(ban):
                return False
            
            for u, b in zip(user, ban):
                if b != "*" and u != b:
                    return False
        return True    
    
    answer_list = []
    
    for users in permutations(user_id, len(banned_id)):
        users_set = set(users)
        if chk(users) and users_set not in answer_list:
            answer_list.append(users_set)    
        
    
    return len(answer_list)