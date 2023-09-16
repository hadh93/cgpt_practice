def factorial(N,res):
    if N == 0:
        return 1
    elif N == 1:
        return res
    else:
        return factorial(N-1, res*N)



if __name__ == "__main__":
    N = int(input())
    answer = factorial(N,1)
    print(answer)