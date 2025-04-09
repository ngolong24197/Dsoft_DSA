class Solution(object):
    
    ##Use lIst
    def dayOfYear(self, date):
        year, month, day = map(int, date.split("-"))
        
        day_per_month = [31, 28, 31, 30, 31, 30,
                      31, 31, 30, 31, 30, 31]
        
        if (year %4 == 0 and year %100 == 0) or (year %400 ==0):
            day_per_month[1] = 29
        total_day = 0
        for s in range( 0, month -1 ):
            total_day += day_per_month[s]
            
        return total_day + day
        
    ## use Dict 
    def dayOfYear2(self,date):
            year, month, day = map(int, date.split("-"))
            
            day_per_month= { 1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
            7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
            
            if (year %4 == 0 and year %100 == 0) or (year %400 ==0):
                day_per_month[2] = 29  
            
            total_date = sum(day_per_month[m] for m in range(1,month)) + day
            return total_date
        
        