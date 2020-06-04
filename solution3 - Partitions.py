"""
Researching found that this is a partition problem (number theory). We are looking to generate the sum of partitions where there are distinct parts
Was difficult at first to get head around however notes from my uni course and a great wikipedia article 'Partition (number theory)' helped me generate this
"""
def solution(n):
    # create an empty table where first index is 1 and rest are zeroes 
    sequence = [1]+[0]*n
    # loop through each integer from 1 to n (inclusive)
    for x in range(1, n+1):
        # from the final index go down adding the difference between index value and the integers. this is how we make the sequence
        for y in range(n, x-1, -1):
            sequence[y] += sequence[y-x]
    # once the sequence is complete it has the distinct part partition number but stairs cannot be of 1 type of brick so that is removed
    return sequence[n]-1
