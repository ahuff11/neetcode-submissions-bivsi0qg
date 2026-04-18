class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #hash map loop through both and append where num 1 number is 
        indexMap = {}
        for i in range(len(nums2)):
            indexMap[nums2[i]] = i


        res = []
        for i in range(len(nums1)):
            res.append(indexMap[nums1[i]])

        return res