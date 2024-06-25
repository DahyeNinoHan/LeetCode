class Solution:
    def defangIPaddr(self, address: str) -> str:
        str = address.replace('.','[.]')
        return str

a = Solution()

address = ''

a.defangIPaddr(address)