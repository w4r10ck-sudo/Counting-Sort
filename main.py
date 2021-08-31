# Counting sort
def counting_sort(tmp_arr):
    count_arr = [0 for i in range(10)]  # assuming range b/w 0 to 9
    for i in tmp_arr:
        count_arr[i] += 1  # incrementing the frequency of an item i
    for i in range(1, len(count_arr)):
        count_arr[i] = count_arr[i - 1] + count_arr[i]  # incrementing previous 2 numbers from 1st index to n
    output = [-1 for i in range(len(tmp_arr))]  # creating an output array initialized with -1
    for i in tmp_arr:
        # The modified count array indicates the position of each object in
        # the output sequence
        output[count_arr[i]-1] = i
        count_arr[i] -= 1
    return output


arr = [1, 4, 1, 2, 7, 5, 2]
print(counting_sort(arr))
