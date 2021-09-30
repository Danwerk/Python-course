def format_time(minutes: int) -> str:
    hours = minutes // 60
    if minutes < 60:
        return f'{minutes}min'
    else:
        minutes = minutes % 60
        if minutes == 0:
            return f'{hours}h'
        else:
            return f'{hours}h {minutes}min'


def lucky_guess(n: int) -> bool:
    lucky_nums = [1, 3, 7]
    str_num = str(n)
    if n in lucky_nums:
        return True
    elif n >= -6 and n <= 121 and n % 13 == 0:
        return True
    elif n < 0 and '5' not in str_num and '6' not in str_num:
        return True
    else:
        False


#print(lucky_guess(7))
#print(lucky_guess(26))
#print(lucky_guess(32))


def sum_of_a_beach(s: str) -> int:
    low_case = s.lower()
    count = 0
    beach_list = ['sand', 'water', 'fish', 'sun']
    for beach_elem in beach_list:
        beach_elem_len = len(beach_elem)
        for i in range(len(s)):
            if low_case[i:i + beach_elem_len] == beach_elem:
                count += 1
    return count




def index_index_value(nums: list) -> int:
    """
    Return value at index.

    Take the last element.
    Use the last element value as the index to get another value.
    Use this another value as the index of yet another value.
    Return this yet another value.

    If the the last element points to out of list, return -1.
    If the element at the index of last element points out of the list, return -2.

    All elements in the list are non-negative.

    index_index_value([0]) => 0
    index_index_value([0, 2, 4, 1]) => 4
    index_index_value([0, 2, 6, 2]) => -2  (6 is too high)
    index_index_value([0, 2, 4, 5]) => -1  (5 is too high)

    :param nums: List of integer
    :return: Value at index of value at index of last element's value
    """

    last_elem = nums[-1]
    if last_elem > len(nums):
        return -1
    new_elem = nums[last_elem]
    if new_elem > len(nums):
        return -2
    else:
        yet_another_elem = nums[new_elem]
        return yet_another_elem


print(index_index_value([0]))
print(index_index_value([0, 2, 4, 1]))
print(index_index_value([0, 2, 6, 2]))
print(index_index_value([0, 2, 4, 5]))