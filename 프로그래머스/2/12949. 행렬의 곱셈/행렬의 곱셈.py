def solution(arr1, arr2):
    answer = [[]]
    r=len(arr1[0])
    ans=[[0]*len(arr2[0]) for _ in range(len(arr1))]
    for i in range(len(ans)):
        for j in range(len(ans[0])):
            for t in range(r):
                ans[i][j]+=arr1[i][t]*arr2[t][j]
            
    return ans