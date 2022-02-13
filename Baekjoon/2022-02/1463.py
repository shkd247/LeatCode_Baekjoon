import sys 

def mysolution():
    input = sys.stdin.readline
    n = int(input())
    dp = [0] * (n+1)
    
    for i in range(2, n+1):
        dp[i] = dp[i-1]+1
        if i%3==0:
            dp[i] = min(dp[i], dp[i//3]+1)
        if i%2==0:
            dp[i] = min(dp[i], dp[i//2]+1)
            
    print(dp[n])
    
def solution():
    input = sys.stdin.readline

if __name__=='__main__':
    mysolution()