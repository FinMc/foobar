def solution(params):
    treeSize = 2**params[0] - 1
    values = params[1]
    parents = []
    for val in values:
        parents.append(findParent(val, treeSize, 1))

    def findParent(val, root, level):
        # if value is root of tree
        if val == root:
            return -1
        prev = 0
        
        while True:

            # left of tree`
            if val < root+1//2:
                None
            # right of tree
            else:
                None
            
