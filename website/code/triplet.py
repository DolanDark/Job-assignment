
def target_triplet(arr, Y):
    import sys

    split_arr = list(arr.split())
    int_arr = [int(i) for i in split_arr]
    Y = int(Y)

    value = sys.maxsize         #can be some high number
    #value = 9000000
    temp_arr = []

    for i in range(len(int_arr)):
        for j in range(i + 1, len(int_arr)):
            for k in range(j + 1, len(int_arr)):
                if (abs(Y - value) > abs(Y - (int_arr[i] + int_arr[j] + int_arr[k]))):
                    value = (int_arr[i] + int_arr[j] + int_arr[k])
                    temp_arr = []
                    temp_arr = [int_arr[i], int_arr[j], int_arr[k]]

    return f'The closest to the target value {Y} is sum of {temp_arr} = {value}'


# test cases
# arr = "1 -4 5 3 2"
# a = 5
# arr2 = "7 20 -6 4 6"
# b = 20

# value = target_triplet(arr, a)
# print(value)
# value = target_triplet(arr2, b)
# print(value)
