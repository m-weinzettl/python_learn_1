def print_name():
    print("Markus")

nums = [1, 2, 3, 4, 5]
chars = ['a', 'b', 'c', 'd', 'e']

def test_print():
    count = 0
    while count < 5:
        print("Hallo Markus")
        count += 1

def test_count():
    for n in nums:
        print(n)

def test_merge():
    merge_list = []
    for n in nums:
        merge_list.append(n * "Markus")
    return merge_list

def test_list_comp():
    return[f"{n}{c}" for n, c in zip(nums, chars)]

def test_name_merge():
    return [f"{n}.Markus" for n in nums]