#Description: find the day of the year for the given date
#Input: A date string
#Output: interger representing the day of the year
from CountDay_func import *

def main():
    
    solution = Solution()
    
    date = "2019-01-09"
    result = solution.dayOfYear(date)
    print(result)


if __name__ == "__main__":
    main() 
