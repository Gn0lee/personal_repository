from typing import Any
import sys
from collections import deque

class FixedStack:
    class Empty(Exception):
        pass
    
    class Full(Exception):
        pass
    
    def __init__(self, maxlen : int) -> None:
        self.__stk = deque([],maxlen)
        self.maxlen = maxlen
    
    def size(self) -> None:
        print(len(self.__stk)) 
    
    def empty(self) -> None:
        if len(self.__stk) == 0:
            print(1)
        else:
            print(0)
    
    def is_full(self) -> bool:
        return len(self.__stk) == self.maxlen
    
    def push(self,value : Any) -> None:
        # if self.is_full:
        #     raise FixedStack.Full
        self.__stk.append(value)
        
    
    def pop(self) -> None:
        if len(self.__stk) == 0:
            print(-1)
        else:
            print(self.__stk.pop())
    
    def top(self) -> None:
        if len(self.__stk) == 0:
            print(-1)
        else:    
            print(self.__stk[-1])
    
    def clear(self) -> None:
        self.__stk.clear()
    
    def find(self, value : Any) -> Any:
        try:
            return self.__stk.index(value)
        except ValueError:
            return -1
    
    def count(self,value : Any) -> Any:
    
        return self.__stk.count(value) 
    
    def __contains__(self,value : Any) -> bool:
        return value in self.__stk
    
    def dump(self) -> None:
        if len(self.__stk) == 0:
            print('스택이 비어있습니다.')
        else:
            print(list(self.__stk))

stack = FixedStack(100000)
testcase = int(input())
for i in range(testcase):
    command = tuple(map(str,sys.stdin.readline().split()))
    if command[0] == 'push':
        stack.push(command[1])
    elif command[0] == 'pop':
        stack.pop()
    elif command[0] == 'size':
        stack.size()
    elif command[0] == 'empty':
        stack.empty()
    else:
        stack.top()
