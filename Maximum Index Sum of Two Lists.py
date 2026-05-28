class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        d = {}

        
        for i in range(len(list1)):
            d[list1[i]] = i

        minimum = float('inf')
        ans = []

        
        for j in range(len(list2)):
            if list2[j] in d:
                total = j + d[list2[j]]

                if total < minimum:
                    minimum = total
                    ans = [list2[j]]

                elif total == minimum:
                    ans.append(list2[j])

        return ans
