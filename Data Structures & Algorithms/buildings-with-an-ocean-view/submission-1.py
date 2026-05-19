class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        n = len(heights)
        
        ocean_view = [n-1]

        tallest_building = heights[-1]

        for i in range(len(heights)-2, -1, -1):

            if heights[i] > tallest_building:
                ocean_view.append(i)
                tallest_building = heights[i]

        ocean_view.reverse()
        return ocean_view


""""
 0 1 2 3 4 5 6
[1,3,2,4,2,5,1]
-----------t


ans = [5, 6]

"""