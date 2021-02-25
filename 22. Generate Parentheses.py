from itertools  import combinations  as cb, permutations as perm

class Solution:


    @staticmethod
    def is_valid(brace):
        if brace.startswith(')') or brace.endswith('('):
            return False
        stack = []

        braces=list(brace)

        open1=['(' ]
        close1=[')']
        for element in braces:

            obrace=open1[close1.index(element)] if element in close1 else None

            if not stack:
                stack.append(element)
            elif obrace==stack[-1]:
                stack.pop()
            else:
                stack.append(element)
        if not stack:
            return True
        else:
            return False



    def generateParenthesis(self, n):

        rlist = []
        left = right = n




        if left == right:














s = Solution()
s.generateParenthesis(8)




#
# from itertools  import combinations  as cb, permutations as perm
#
# class Solution:


#     @staticmethod
#     def is_valid(brace):
#         if brace.startswith(')') or brace.endswith('('):
#             return False
#         stack = []
#
#         braces=list(brace)
#
#         open1=['(' ]
#         close1=[')']
#         for element in braces:
#
#             obrace=open1[close1.index(element)] if element in close1 else None
#
#             if not stack:
#                 stack.append(element)
#             elif obrace==stack[-1]:
#                 stack.pop()
#             else:
#                 stack.append(element)
#         if not stack:
#             return True
#         else:
#             return False
#
#
#
#     def generateParenthesis(self, n):
#
#         rlist = []
#         str1='()'*n
#         # print(str1)
#         # print(list(cb(str1,6) ))
#         for element in set(perm(str1)):
#             # print(''.join(element))
#             if self.is_valid(''.join(element)):
#                 rlist.append(''.join(element))
#         #
#         # print(set(perm(str1,3)))
#         print(rlist)
#         return rlist
#
#
#
# s = Solution()
# s.generateParenthesis(8)

