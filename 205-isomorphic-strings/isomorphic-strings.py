class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
           return False

        map_s_t = {}
        map_t_s = {}

        for i in range(len(s)):
            a = s[i]
            b = t[i]

            # s -> t
            if a in map_s_t:
                if map_s_t[a] != b:
                    return False
            
            else:
                map_s_t[a] = b


            # t -> s
            if b in map_t_s:
                if map_t_s[b] != a:
                    return False
            
            else:
                map_t_s[b] = a

        return True
        