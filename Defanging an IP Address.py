class Solution:
    def defangIPaddr(self, address: str) :
        return address.replace('.',"[.]")
        
