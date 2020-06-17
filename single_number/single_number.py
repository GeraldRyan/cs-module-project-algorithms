'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Your code here

    for item in arr:
        count = 0
        for j in range(len(arr)):
            if arr[j] == item:
                count +=1
        if count == 1:
            print(item)
            return item



if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")