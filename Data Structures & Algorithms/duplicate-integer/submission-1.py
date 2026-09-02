class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for i in nums:
            if i in seen:
                return True 
            seen.add(i)
        return False 
       


""""   So basically all I'm going to write is something that shows, "Hey this integer was typed in once so equals false," or "These integers were all typed in once equals false." Okay this integer has a duplicate so it is true. Basically I have to write a code that shows something like that  


 And based on hitting one to remember the numbers already, I'd have to use a dictionary (a hash map) 

So each number I iterate through, put that into a set and before I put that into the set, I need to make sure it doesn't exist in the set already. This would be O(N), since all we're doing is checking the set and then checking the number in the list. If I wrote it correctly, it would be O(N), not O(1), because it's more than one step 

Alright so this is pseudocode right now. The first thing I should do is create an empty list. Once I create the empty list, I write code. I look through the number list and when it looks through the number list, for each integer it checks it goes back to the set to check if it's there. If it's not there it will continue.

Once it finds something let me go back. Once it's not there it will continue and it will go back, check the list, 2nd number, "oh it's not in the list. Let me go back to the set." Let me go back to the 4th number, "oh it's not in the set. FALSE!"

Now if it was, I check the first, second, third, and fourth numbers, or 0, 1, 2, and 3 indices. If one of them was a duplicate then it would be TRUE and that's where we would end the problem. Correct? """