
def solution(ls):
    #lambda allows the key to be generated for each parameter from the map
    # map turns each value between each point to an integer so it can be compared using sort()
    ls.sort(key=lambda x: map(int, x.split(".")))
    return ls
