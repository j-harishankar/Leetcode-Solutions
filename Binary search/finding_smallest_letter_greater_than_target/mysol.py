class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        result = 1000
        res = ''
        val1 = ord(target)
        for i in letters:
            val = ord(i)
            if val > val1:
                if (val - val1) < result:
                    res = i
                    result =  val - val1
        if res == "":
            return letters[0]
        return res 