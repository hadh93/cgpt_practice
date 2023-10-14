
def generate_permutation(N, M):
    def backtracking(curr_permutation):
        if len(curr_permutation) == M:
            permutation.append(tuple(curr_permutation))
            return
        for num in range(1, N+1):
            if num not in curr_permutation:
                curr_permutation.append(num)
                backtracking(permutation)
                curr_permutation.pop(num)

    permutation = []
    backtracking([])
    return permutation


N, M = map(int, input().split())

ans = generate_permutation(N, M)

for aPerm in ans:
    for n in aPerm:
        print(n, end=' ')
    print()
