"""
I originally thought I could XOR each row at a time, however this took too long.
Therefore had to see what the pattern is in each case of XOR in binary form. There is a pattern every 4 decimal numbers.
Thus applied it to the solution where instead of generating each number just taking the pattern between start and end numbers
"""


def solution(start, length):

    totalXors = 0
    # Create a counter that starts at the end of the line and goes to 1
    for counter in xrange(length, 1, -1):

        # Find the end number of the line before the counter
        endNum = start+length-1-(length-counter)

        # If the number is even, provide pattern 1
        if start % 2 == 0:
            template = [endNum, 1, endNum ^ 1, 0]
        # If odd provide pattern 2
        else:
            template = [start, start ^ endNum, start-1, (start-1) ^ endNum]
            
        # Get the XOR for that line
        lineXors = template[(endNum-start) % 4]
        # XOR line with total
        totalXors = totalXors ^ lineXors
        # Increment start of line
        start += length

    # When counter is 1 number, just add that to the end of the XOR
    totalXors = totalXors ^ start

    # Return total XORs
    return totalXors
