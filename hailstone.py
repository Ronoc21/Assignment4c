# Conor Smith
# Date 4/21/21
# Description: defines function for hailstone sequence

def hailstone(num):
    answer = 2
    """Takes a number (num) and applies hailstone formula if number is greater than one. If number is one program is complete"""
    print(int(num))
    if num > 1:
        if num % 2 == 0:
            answer += hailstone(num / 2)
        else:
            answer += hailstone((num * 3) + 1)
    return answer
