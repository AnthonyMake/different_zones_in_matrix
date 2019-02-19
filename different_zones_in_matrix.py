'''
For a given Matrix A, this code will
compute how many separate areas are covered by the same number 

--this was supposed to run inside a codility test, 
so the same testcase has been included--

the output for this test should be as follows:
>> the total different zones for the matrix A are: 11

feel free to change the testcase as you wish, 
please consider that A should be matrix-shaped.

Antonio Vasquez 20180219
'''

A = [[5, 4, 4],
    [4, 3, 4],
    [3, 2, 4],
    [2, 2, 2],
    [3, 3, 4],
    [1, 4, 4],
    [4, 1, 1]]

def solution(A):
        
    # lets make a set with the color values and where their 
    # points are located
    color_set = {}
    total_different_zones = 0
    
    for i in range(len(A)):
        for j in range(len(A[i])):
            
            current_color = A[i][j]
            
            if current_color not in color_set:
                color_set[A[i][j]] = []
                
            color_set[A[i][j]].append((i,j))

    for color in color_set:
        
        # print('color: ' + str(color) + ' has ', end = ' ')

        dot_list = color_set[color]
        len_list = len(dot_list)

        count_region = 1

        for i in range(0,len_list-1):

            same_row = dot_list[i][0] == dot_list[i+1][0]
            same_col = dot_list[i][1] == dot_list[i+1][1]

            if same_col or same_row:
                count_region += 0
            else:
                count_region += 1    
        
        total_different_zones += count_region
        # print(str(count_region) + ' zones')

    return total_different_zones
    
print('the total different zones for the matrix A are: ' + str(solution(A)))
