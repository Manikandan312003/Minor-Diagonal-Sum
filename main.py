def minorDiagonalSum(arr):
    sum,M=0,len(arr)
    for i in range(M):
        sum+=arr[i][M-1-i]
    return sum

print(minorDiagonalSum([[1,-2,-3],[-4,5,-6],[-7,-8,9]]))
print(minorDiagonalSum([[3,2],[2,3]]))