#User function Template for python3

class Solution:
    def evenlyDivides(self, n):
        count = 0
        original_n = n  # Store the original number
        n = abs(n)  # Handle negative numbers
        
        while n > 0:
            digit = n % 10  # Extract the last digit
            if digit != 0 and original_n % digit == 0:  # Check divisibility
                count += 1
            n = n // 10  # Remove the last digit
        
        return count
    
       

  
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())

        ob = Solution()
        print(ob.evenlyDivides(N))
        print("~")

# } Driver Code Ends