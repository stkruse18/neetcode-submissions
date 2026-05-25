from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        s1dict = defaultdict(int)
        s2dict = defaultdict(int)

        # build s1 frequency
        for char in s1:
            s1dict[char] += 1

        k = len(s1)

        # build first window
        for i in range(k):
            s2dict[s2[i]] += 1

        # check first window
        if s1dict == s2dict:
            return True

        l = 0

        # slide window
        for r in range(k, len(s2)):

            # add new char
            s2dict[s2[r]] += 1

            # remove old char
            s2dict[s2[l]] -= 1

            if s2dict[s2[l]] == 0:
                del s2dict[s2[l]]

            l += 1

            if s1dict == s2dict:
                return True

        return False