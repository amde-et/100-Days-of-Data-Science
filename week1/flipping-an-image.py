class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:

        for img in image:
            img.reverse()
        for i in range(len(image)):
            for j in range(len(image[0])):
                image[i][j] = 1 - image[i][j] 
        return image
