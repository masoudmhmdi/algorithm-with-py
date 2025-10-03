
#solve with devide and conquer
def __max_sub_set(arr):
    n = len(arr)
    if(n == 1) : return max(arr[0], 0)

    maxLeft = __max_sub_set(arr[0:n//2])
    maxRight = __max_sub_set(arr[n // 2: n +1])

    ans = max(maxLeft, maxRight)

    ansL = sum = 0
    for i in range(n//2):
        sum += arr[i]
        if(sum > ansL):
            ansL = sum


    ansR = sum = 0
    for i in range(n//2, n):
        sum += arr[i]
        if(sum > ansR):
            ansR = sum


    return  max(ans,(ansL + ansR),0)


#dynamic programming
def __max_sub_set_2(arr):
   biggest_sub_set = 0
   for i in range(len(arr)):
       current_max = max(arr[i], biggest_sub_set)
       if(current_max > biggest_sub_set):
           biggest_sub_set = current_max
       return biggest_sub_set
