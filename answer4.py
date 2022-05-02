def div(a,b):
    result = []
    for element in range(a,b+1):
        if (element % 2 == 0) and (not element % 3== 0):
            result.append(element)
    return result

nums = div(0,20)
print(nums)