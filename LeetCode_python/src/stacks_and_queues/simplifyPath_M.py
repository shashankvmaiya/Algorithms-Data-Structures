'''
71. Simplify Path

Created on Jun 30, 2018
Given an absolute path for a file (Unix-style), simplify it.
path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"
@author: smaiya
'''

class Solution:
    # @param A : string
    # @return a strings
    def simplifyPath(self, A):
        paths = A.split('/')
        simplified_path = list()
        for path in paths:
            if path == '' or path == '.':
                continue
            elif path == '..':
                if simplified_path:
                    simplified_path.pop()
            else:
                simplified_path.append(path)
        output = '/'.join(simplified_path)
        return '/'+output


a = Solution()
inp = "/a/./b/../../c/"
inp = '/home/'
inp = '..'
out = a.simplifyPath(inp)
print ('Simplified Path = ', out)
