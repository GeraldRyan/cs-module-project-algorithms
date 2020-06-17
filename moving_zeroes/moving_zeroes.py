'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here
    print("array initial", arr)

    for j in range(len(arr)):
        if arr[j] != 0:
            # to_pop.append(j)
            arr.insert(0, arr.pop(j))
    print("array zeroed", arr)
    # for i in range(len(arr)):
    #     # if arr[i] == 0:
    #     #     next()
    #     smallest_i = i
        
    #     for j in range(i, len(arr)):
    #         if arr[j] < arr[smallest_i]:
    #             smallest_i = j

    #     arr[i], arr[smallest_i] = arr[smallest_i], arr[i]

    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2, 0,0,0,244]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")