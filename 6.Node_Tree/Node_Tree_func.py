import math


class Solution(object):
    def pathInZigZagTree(self, label):
        path = []
        while label > 0:
            path.append(label)
            level = int(math.log2(  ))
            label = (2 ** level + 2 ** (level + 1) - 1 - label) // 2
        return path[::-1]