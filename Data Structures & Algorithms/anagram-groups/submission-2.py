class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        output = []
        trash = []
        for ind, val in enumerate(strs):
            d1 = {}
            if val not in trash:
                op = [val]
                for char in val:
                    if char in d1:
                        d1[char] += 1
                    else:
                        d1[char] = 1
            else:
                continue
            if ind != len(strs) - 1:
                for ind2, val2 in enumerate(strs[ind + 1:]):
                    d2 = {}
                    for char in val2:
                        if char in d2:
                            d2[char] += 1
                        else:
                            d2[char] = 1
                    if d1 == d2:
                        op.append(val2)
                        trash.append(val2)

            if op != []:
                output.append(op)
            op = []
        return output