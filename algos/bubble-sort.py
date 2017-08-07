def bubble_sort(a_list):
    def swap(n1, n2):
        a_list[n1] = a_list[n1] ^ a_list[n2]
        a_list[n2] = a_list[n1] ^ a_list[n2]
        a_list[n1] = a_list[n1] ^ a_list[n2]
    for j in range(len(a_list)):
        for i in range(len(a_list) -1):
            if a_list[i] > a_list[i+1]:
                swap(i, i+1)
    return a_list