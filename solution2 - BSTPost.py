def solution(height, values):
    
    #  find number of nodes in tree
    treeSize = 2**height - 1
    parents = []
    
    #Recursive function to find children of nodes
    def findChilds(val, root, prev, level):
        #find the math remainder of the tree depending on the level currently on
        remainder = 2**(height-level)-1

        #find left right and root of that level
        left = remainder + prev
        right = left + remainder
        root = right + 1
        
        #check if direct children match value
        if left == val or right == val:
            return root
        
        #if the value is on the right side of the root node change the prev value
        if val > left:
            prev = left
        
        # recursively call the function
        return findChilds(val, root, prev, level+1)
    
    # iterate through all the values and call the function
    for val in values:
        if val == treeSize:
            parents.append(-1)
        elif val > treeSize:
            parents.append(-1)
        else:
            parents.append(findChilds(val, treeSize, 0, 1))
    
    return parents
