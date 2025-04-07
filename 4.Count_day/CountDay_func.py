class Solution(object):
    def dayOfYear(self, date):
        year, month, day = map(int, date.split("-"))
        
        day_per_month = [31, 28, 31, 30, 31, 30,
                      31, 31, 30, 31, 30, 31]
        
        if (year %4 == 0 and year %100 == 0) or (year %100 ==0):
            day_per_month[1] = 29
        total_day = 0
        for month in range( 0, month -1 ):
            total_day += day_per_month[month]
            
        return total_day + day
        
        