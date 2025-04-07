import math


class Solution(object):
    def pathInZigZagTree(self, label: int ) -> List[int]:
        row = int(log2(label) + 1)
        res = [0] * row
        while row:
            res[row-1] = label
            label = (2 ** row -1 - label + 2 ** (row -1 ))//2
            row -=1
        return res
    

    def pathInZigZagTree2(self, label:int):
        row = label.bit_length()  
        res = [0] * row
        while row:
            res[row-1] = label
        
            label = (2 ** row - 1 - label + 2 ** (row - 1)) // 2
            row -= 1
        return res
