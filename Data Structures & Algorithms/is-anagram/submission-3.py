class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        return sorted(s) == sorted(t)

               
                
             


        

# if the string is not == to the other string then stop
# sort the strings at the end so that I can know if its right. 

#0(1) time complexity

