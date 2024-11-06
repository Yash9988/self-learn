"""
1233. Remove Sub-Folders from the Filesystem [MEDIUM]

Given a list of folders folder, return the folders after removing all sub-folders in those folders. You may return the
answer in any order.

If a folder[i] is located within another folder[j], it is called a sub-folder of it. A sub-folder of folder[j] must
start with folder[j], followed by a "/". For example, "/a/b" is a sub-folder of "/a", but "/b" is not a sub-folder of
"/a/b/c".

The format of a path is one or more concatenated strings of the form: '/' followed by one or more lowercase English letters.

    - For example, "/leetcode" and "/leetcode/problems" are valid paths while an empty string and "/" are not.


Example 1:
Input: folder = ["/a","/a/b","/c/d","/c/d/e","/c/f"]
Output: ["/a","/c/d","/c/f"]

Explanation: Folders "/a/b" is a subfolder of "/a" and "/c/d/e" is inside of folder "/c/d" in our filesystem.

Example 2:
Input: folder = ["/a","/a/b/c","/a/b/d"]
Output: ["/a"]

Explanation: Folders "/a/b/c" and "/a/b/d" will be removed because they are subfolders of "/a".

Example 3:
Input: folder = ["/a/b/c","/a/b/ca","/a/b/d"]
Output: ["/a/b/c","/a/b/ca","/a/b/d"]


Constraints:

    -> 1 <= folder.length <= 4 * 10^4
    -> 2 <= folder[i].length <= 100
    -> folder[i] contains only lowercase letters and '/'.
    -> folder[i] always starts with the character '/'.
    -> Each folder name is unique.


Concepts: Trie
"""


# My Solution
def removeSubfolders(folder: list[str]) -> list[str]:
    root = {}                                               # Initialise the tire root node
    for dr in folder:                                       # Iterate through all folders
        node = root                                         # Assign a reference point at the root node
        for ch in dr:                                       # Iterate through the folder path
            if ch not in node:                              # Check if the folder is absent in the current node
                node[ch] = {}                               # Initialise a new trie node as the value for the folder
            node = node[ch]                                 # Switch the reference pointer to the child trie-node
        node['//'] = True                                   # Mark the end of a folder path under a "special" key

    res = set([])                                           # Initialise a set to store all sub-folders
    for dr in folder:                                       # Iterate through all folders
        node, n = root, len(dr)                             # Assign a reference pointer at the root node
        flag = False                                        # Initialise a flag to denote addition of a path to the set
        for i, ch in enumerate(dr):                         # Iterate through the folder path
            if node.get('//', False) and dr[i] == '/':      # Check for sub-paths
                res.add(dr[:i])                             # Add the path to the set
                flag = True                                 # Set the flag
                break                                       # Break out of the loop
            node = node[ch]                                 # Switch the reference pointer to the child trie-node

        if not flag:                                        # Check if the flag is still unset
            res.add(dr)                                     # Add the complete folder path to the set

    return list(res)                                        # Return the result


# Optimised Solution
def removeSubfolders_op(folder: list[str]) -> list[str]:
    seen, ans = set(folder), []                             # Initialise a set of input folders and a result list
    for f in folder:                                        # Iterate through all folders
        for i, c in enumerate(f):                           # Iterate through the folder path
            if c == '/' and f[: i] in seen:                 # Check if the sub-paths has already been observed
                break                                       # Break out of the iteration
        else:
            ans.append(f)                                   # Append the path to the result
    return ans                                              # Return the result
