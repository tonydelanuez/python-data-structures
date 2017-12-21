def subsetsRec(nums):
    results = []
    dfs(sorted(nums), 0, [], results)
    return results

def dfs(nums, index, path, results):
    results.append(path)
    for i in xrange(index, len(nums)):
        dfs(nums, i+1, path+[nums[i]], results)

def subsetsBit(nums):
    results = []
    for i in xrange(1 << len(nums)):
        tmp = []
        for j in xrange(len(nums)):
            if i & 1 << j:
                tmp.append(nums[j])
        results.append(tmp)
    return results

def subsets(nums):
    results = [[]]
    for number in sorted(nums):
        results += [item+[number] for item in results]
    return results


nums = [2, 3, 4, 5]
print(subsets(nums))
