#User function Template for python3

class Solution:
    def evenlyDivides(self, n):
        count=0
        m=str(n)
        for i in m:
            if i!='0':
                if n%int(i)==0:
                    count+=1
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