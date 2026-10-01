class Solution:
    def validStrings(self, n: int) -> List[str]:
        result=[]
        def backtrack(current):
            if len(current)==n:
                result.append(current)
                return

            backtrack(current+"1")

            if len(current)==0 or current[-1] != "0":
                backtrack(current + "0")
        
        backtrack("")
        return result
        