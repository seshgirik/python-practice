from collections import Counter


class Solution:
    return_list = []
    match_set = set()

    def group_anagrams(self, strs):

        while strs:
            element = strs.pop(0)
            sorted_element = ''.join(sorted(element))
            print(self.match_set)
            if sorted_element not in self.match_set:
                self.match_set.add(sorted_element)
                self.return_list.append([element])
            else:
                self.add_anagram(element)
                self.match_set.add(sorted_element)



        print(self.return_list)
        return self.return_list

    def add_anagram(self, element):
        # if not self.return_list:
        #     return False
        for sublist in self.return_list:
            sublist_element = sublist[0]
            if self.is_anagram(sublist_element, element):
                sublist.append(element)
                return True
        # print(self.return_list)
        # print(element)
        # self.return_list.append([element])

    @staticmethod
    def is_anagram(sublist_element, element):

        if len(sublist_element) == len(element) and not (set(element) - set(sublist_element)) and (Counter(sublist_element) == Counter(element) ):
            return True
        return False


# strs1 = ["eat","tea","tan","ate","nat","bat"]
strs1 = [""]
s = Solution()
s.group_anagrams(strs1)


