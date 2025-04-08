# Description: This function finds the path from the root to a given node in a zigzag binary tree.
# A zigzag binary tree is a binary tree where the values of the nodes at each level are arranged in a zigzag pattern.

#Input: A label of a node in a zigzag binary tree.
#Output: The path from the root to the node with that label.

from Node_Tree_func import Solution

def main():
    solution = Solution()

    result1 = solution.pathInZigZagTree(14)
    
    result2 = solution.pathInZigZagTree2(14)
    
    print(result1)
    
    print(result2)
    
if __name__== "__main__":
    main()
