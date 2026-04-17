class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        maxi = arr[len(arr)-1]

        

        for i in range(len(arr)-1,-1,-1):
            temp = arr[i]
            if arr[i] > maxi:
                arr[i] = maxi
                maxi = temp
            else:
                arr[i] = maxi
            
        arr[-1] = -1
        return arr
