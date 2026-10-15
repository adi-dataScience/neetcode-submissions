from typing import List


def sort_words(words: List[str]) -> List[str]:
    # result=sorted(words,key=lambda w:len(w))
    # result.reverse()
    # return result  -> this results in reverse order after sorting by length

    result=sorted(words, key=lambda i:len(i), reverse=True)
    return result


def sort_numbers(numbers: List[int]) -> List[int]:
    result=sorted(numbers, key=lambda i: abs(i))
    return result

    # or
    # result=sorted(numbers,key=abs)


# do not modify below this line
print(sort_words(["cherry", "apple", "blueberry", "banana", "watermelon", "zucchini", "kiwi", "pear"]))

print(sort_numbers([1, -5, -3, 2, 4, 11, -19, 9, -2, 5, -6, 7, -4, 2, 6]))
