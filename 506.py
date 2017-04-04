'''
Relative Ranks 
 Given scores of N athletes, find their relative ranks and the people with the top three highest scores, 
 who will be awarded medals: "Gold Medal", "Silver Medal" and "Bronze Medal".

Example 1:
Input: [5, 4, 3, 2, 1]
Output: ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]
Explanation: The first three athletes got the top three highest scores, so they got "Gold Medal", "Silver Medal" and "Bronze Medal". 
For the left two athletes, you just need to output their relative ranks according to their scores.

Note:

    1.N is a positive integer and won't exceed 10,000.
    2.All the scores of athletes are guaranteed to be unique.

'''

class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        #test case:[3,2,5,4,1]
        sorted_nums=sorted(nums)[::-1]
        #[5,4,3,2,1]
        rank=["Gold Medal", "Silver Medal", "Bronze Medal"]+map(str, range(4,len(nums)+1))
        #["Gold Medal", "Silver Medal", "Bronze Medal","4", "5"]
        new_dict=dict(zip(sorted_nums,rank))
        #{5:"Gold Medal", 4:"Silver Medal" ,3:"Bronze Medal" ,2: "4", 1: "5"}      
        return map(new_dict.get,nums)
        #["Gold Medal", "Silver Medal" , "Bronze Medal","4","5"]
        '''
        iterate keys from your list using map function:
        lstval = list(map(dct.get, lst))
        Or if you prefer list comprehension:
        lstval = [dct[key] for key in lst]
        '''
