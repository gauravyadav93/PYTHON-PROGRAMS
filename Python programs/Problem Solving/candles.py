import math
import os
import random
import re
import sys



def birthdayCakeCandles(candles):
    return(candles.count(max(candles)))
    
    
    
if __name__ == '__main__':
        candles_count = int(input().strip())
        candles = list(map(int, input().rstrip().split()))
        result = birthdayCakeCandles(candles)
    

