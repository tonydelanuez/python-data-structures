def bubble_sort(a_list):
    """ 
    Iterate through the list
    maintain a swapped boolean
    if list[i] > list[i+1], swap and set swapped to True
    if not swapped on a pass, break
    """
    for j in range(len(a_list)):
        #print("Iteration: %i" % j)
        #print(a_list)
        swapped = False
        for i in range(len(a_list)-1):
            if (a_list[i] > a_list[i+1]):
                #print("Swapping %i, %i" % a_list[i], a_list[i+1])
                a_list = swap(i, i+1, a_list)
                swapped = True
        if not swapped:
            #print("Didn't need to swap! Ending algorithm.")
            break
    return a_list
    
def swap(loc1, loc2, arr):
    tmp = arr[loc1]
    arr[loc1] = arr[loc2]
    arr[loc2] = tmp
    return arr


arrs = []
arrs.append([1,1])
arrs.append([0,1,2,4,5])
arrs.append([1,1,1,2,2,2])
arrs.append([-8,-2,-1,0])
arrs.append([10, 13, 2, 1, 5])
arrs.append([1, 22, 13, 4, 9])
arrs.append([9, 1, 2, 3, 4, 5, 6, 7])

for arr in arrs:
    print("BUBBLE SORTING: ", arr)
    sorted_arr = bubble_sort(arr)
    print("Returned: ", sorted_arr)

