import math


class Solution(object):
    def pathInZigZagTree(self, label):
        path = []
        while label > 0:
            path.append(label)
            level = int(math.log2(label))
            label = (2 ** level + 2 ** (level + 1) - 1 - label) // 2
        return path[::-1]
  
  
    
    def pathInZigZagTree2(self, label:int):
        path = []
        while label > 0:
            path.append(label)
            level = label.bit_length()
            label = (2 ** (level-1) + 2 ** (level) - 1 - label) // 2
        return path[::-1]
