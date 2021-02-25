"""二分查找"""
def binary_search(list,num):
    low=0
    high=len(list)-1

    while low<=high:
        mid=(low+high)//2
        guess=list[mid]
        if guess==num:
            return mid
        if guess< num:
            low=mid+1
        else :
            high=mid-1
    return None
my_list=[1,3,5,7,9]
print(binary_search(my_list,8))
