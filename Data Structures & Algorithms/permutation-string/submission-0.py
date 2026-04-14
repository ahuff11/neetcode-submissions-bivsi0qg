class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
       #use ord() to set the characters to a number from 0-26
       # sliding window through and shrink left until key is 0 
        # iterate through s1 and save it as a pair in an array that can be done like this array[stuff] +=1

        #set my left pointer 
        #iterate through s2 removing the key from counts 
        #then while loop through depending on if the counts is < 0
        #1 that means a character is not in s1
        #2 too many of a character that is in s1
        #shrink from the left until counts is 0 again
        

        # check if the window size matches the s1 and return true if so 
        count = [0] *26
        for i in s1:
            count[ord(i) - ord('a')] +=1

        l = 0
        for r in range(len(s2)):
            key = ord(s2[r]) - ord('a')
            count[key] -=1

            while count[key] < 0:
                count[ord(s2[l])- ord('a')] +=1
                l+=1


            if len(s1) == r -l +1:
                return True
        return False


