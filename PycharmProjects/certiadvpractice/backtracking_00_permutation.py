def generate_permutations(N, M):
    def backtrack(curr_permutation):
        if len(curr_permutation) == M:
            permutations.append(tuple(curr_permutation))
            return

        for num in range(1, N + 1):
            if num not in curr_permutation:
                curr_permutation.append(num)
                backtrack(curr_permutation)
                curr_permutation.pop()

    permutations = []
    backtrack([])

    return permutations

N, M = map(int, input().split())
perms = generate_permutations(N, M)
for aPerm in perms:
    for i in aPerm:
        print(i, end = ' ')
    print()
