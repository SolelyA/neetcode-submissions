class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for string in strs:
            l = len(string)
            s = f"{l}|" + string
            encoded_string += s
        return encoded_string

    def decode(self, s: str) -> List[str]:
        ans = []
        l_str = ""
        i = 0
        while i < len(s):
            c = s[i]
            if c != "|":
                l_str += f"{c}"
                i += 1
            else:
                decoded_str = s[i + 1:i + int(l_str) + 1]
                ans.append(decoded_str)
                i += int(l_str) + 1
                l_str = ""
        return ans

