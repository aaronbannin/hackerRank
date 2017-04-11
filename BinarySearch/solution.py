def binary_search(input_array, target):
    # (list) -> int
    # takes in list and returns index of target or -1 if not found

    begin = 0
    end = len(input_array)-1

    print('begin target={} list={}'.format(target, input_array))
    while end - begin > 1:
        mid = int((end+begin)/2)
        # print('begin={} end={} mid={}'.format(begin, end, mid))
        if input_array[mid] == target:
            return mid
        elif input_array[begin] == target:
            return begin
        elif input_array[end] == target:
            return end
        elif target > input_array[mid]:
            begin = mid
        elif target < input_array[mid]:
            end = mid
        else:
            raise

    return -1
