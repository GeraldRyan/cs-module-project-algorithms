'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n):
    # Your code here
    r = n 
    large_bites, medium_bites, small_bites, ways = 0,0,0, 0
    while r >= 3:
        r = r-3
        large_bites += 1
    while r >=2:
        r = r-2
        medium_bites += 1
    while r>=1:
        r = r-1
        small_bites +=1

    print("large, medium and small bites", large_bites, medium_bites, small_bites)
    

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
