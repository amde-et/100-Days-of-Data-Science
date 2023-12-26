class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        lis=[]
        for i in range(len(names)):
            lis.append([heights[i],names[i]])
        lis.sort(reverse=True)
        lis1=[]
        for i in range(len(names)):
            lis1.append(lis[i][1])
        return lis1