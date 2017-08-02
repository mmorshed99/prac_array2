#https://en.wikipedia.org/wiki/Pascal%27s_triangle
#Given numRows, generate the first numRows of Pascal’s triangle.
#
#Pascal’s triangle : To generate A[C] in row R, sum up A’[C] and A’[C-1] from previous row R - 1.
#
#Example:
#
#Given numRows = 5,
#
#Return
#
#[
#     [1],
#     [1,1],
#     [1,2,1],
#     [1,3,3,1],
#     [1,4,6,4,1]
#]
#
#
def generate(self, A):
        pascal = []
        if A == 0:
          return pascal
        if A>=1:
          pascal.append([1])
        if A>=2:
          pascal.append([1,1])
        if A > 2:
            for i in range(3,A+1):
               temp = []
               temp.append(1)
               for j in range(0,len(pascal[i-2])-1):
                  temp.append(pascal[i-2][j] + pascal[i-2][j+1])
               temp.append(1)
               pascal.append(temp)
        return pascal
