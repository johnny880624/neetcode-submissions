class Solution:

    def encode(self, strs: List[str]) -> str:
        str_result = ""
        for s in strs:
            str_result += f"{len(s)}#{s}"
        return str_result


    def decode(self, s: str) -> List[str]:
        i = 0
        list_result = []
        while i < len(s):
            j = s.find('#', i)
            length = int(s[i:j])
            list_result.append(s[j + 1 : j + 1 +length])
            i = j + 1 + length
        return list_result