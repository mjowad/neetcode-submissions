class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_length = len(s)
        t_length = len(t)

        if s_length != t_length:
            return False

        s_letters_sum = defaultdict(int)
        for i in s:
            s_letters_sum[i] += 1 

        t_letters_sum = defaultdict(int)
        for i in t:
            t_letters_sum[i] += 1

        return s_letters_sum == t_letters_sum


