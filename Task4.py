from typing import Optional


def checked_access(L:list[int], idx:int) -> Optional[int]:
    test = idx >= 0 and idx < len(L)                            # test (first call): None, test (second call): 1
    if test:                                                    # This check prevents an IndexError
        return L[idx]
    else:
        return None


first = checked_access([1, 0, 1], 9)                    # first: None
second = checked_access([1, 0, 1], 2)                   # second: 1
print()

def length_sum(L:list[str]) -> int:
    if len(L) > 2:
        result = len(L[0]) + len(L[1]) + len(L[2])          # For first call (length: 5, > 2)
    elif len(L) > 1:                                        # 4 + 2 + 3 (lengths of "this", "is", "the")
        result = len(L[0]) + len(L[1])                      # For third call (length: 2, > 1)
    elif len(L) > 0:                                        # 7 + 4 (lengths of "another" and "call")
        result = len(L[0])                                  # For second call (length 1, > 0)
    else:                                                   # 11 (length of "second call")
        result = 0
    return result


first = length_sum(["this", "is", "the", "first", "call"])
second = length_sum(["second call"])
third = length_sum(["another", "call"])
print()

def surprising(L:list[str], other:str) -> list[str]:
    L.append(other.upper())
    return L


words = ["this", "is", "confusing", "code."]
first = surprising(words, "Avoid")
second = surprising(words, "such.")
            # "this", "is", "confusing", "code.", "AVOID", "SUCH."
            # Both values of first and second are the same as the value of words
            # The original list is modified by the function instead of a copy.
            # All three variables are updated when the list is changed since they all point to this same list.
print()