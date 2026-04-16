def smallest(n:float, m:float) -> float:
    if n < m:
        return n                            # For neither. Both calls return m.
    else:
        return m

first = smallest(3, 2)              # first: 2
second = smallest(2, 2)             # second: 2. Yes because 2 < 2 is not true, so m is returned.
print()

def function2(a:int, b:int, c:int) -> int:
    if a > b and a > c:
        return a - b                        # When a > b AND a > c
    elif b > c:
        return b + c                        # When a is not the largest value and b > c
    else:
        return 2 * c                        # When a is not the largest value and b < c


answer1 = function2(3, 2, 1)        # answer1: 1
answer2 = function2(2, 3, 1)        # answer2: 4
answer3 = function2(2, 1, 3)        # answer3: 6
print()