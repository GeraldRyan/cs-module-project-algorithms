'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n):
    # Your code here
    r = n 
    if n ==1:
        return 1
    if n == 0:
        return 1
    if n ==2:
        return 2
    max_large_bites, ways = n//3,0
    # while r >= 3:
    #     r = r-3
    #     large_bites += 1
    # while r >=2:
    #     r = r-2
    #     medium_bites += 1
    # while r>=1:
    #     r = r-1
    #     small_bites +=1

    for large_bites in range(max_large_bites,0,-1):
        max_medium_bites = n-(large_bites*3)//2
        for medium_bites in range(max_medium_bites,0,-1):
            ways +=1
    # if (max_large_bites == 0) and (n//2 ==0):
    #     ways = 1

    return ways

    # print("large, medium and small bites", large_bites, medium_bites, small_bites)
    

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
