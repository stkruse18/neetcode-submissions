class Solution:

    def encode(self, strs: List[str]) -> str:
        empty = ""
        for string in strs:
            empty = empty + string + "#67"
        return empty



    def decode(self, s: str) -> List[str]:
        return (s.split('#67')[:-1])
