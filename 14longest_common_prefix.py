# Write a function to find the longest common prefix string amongst an array of strings.

def longestCommonPrefix(strs):
    if not strs:
        return ""

    store = strs[0]

    for i in strs[1:]:
        while not i.startswith(store):
            store = store[:-1]
            if not store:
                return ""
    return store

input1 = ["flower","flow","flight"]
result = longestCommonPrefix(input1)
print(result)