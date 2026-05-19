class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        
        start = 0
        end = 1

        prev = ""

        max_length = 1

        while end < len(arr):
            
            if arr[end-1] > arr[end] and prev != ">":
                max_length = max(max_length, end-start+1)
                end += 1
                prev = ">"
            elif arr[end-1] < arr[end] and prev != "<":
                max_length = max(max_length, end-start+1)
                end += 1
                prev = "<"
            else:
                if arr[end] == arr[end-1]:
                    end += 1

                start = end - 1
                prev = ""
            
            
        return max_length


"""
       s
         e
[2,4,3,2,2,5,1,4]
  < > > = < > <

"""