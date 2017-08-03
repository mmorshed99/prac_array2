def spiral_order(A):
    temp = []
    temp.append([])
    temp[0].append(1)
    if A == 1:
        return temp
    row = []
    for i in range(0,A):
        row.append([])
        for j in range(0,A):
            row[i].append(-1)
    cur_row = 0
    cur_col = 0
    direction = 1
    for i in range(0, A*A):

        if direction == 1:
           row[cur_row][cur_col] = i+1
           if cur_col+1 <= A-1:
             if row[cur_row][cur_col+1] == -1:
                cur_col += 1
             else:
                direction = 2
                cur_row += 1
                continue
           else:
             direction = 2
             cur_row += 1
             continue
        if direction == 2:
           row[cur_row][cur_col] = i+1
           if cur_row+1 <= A-1:
             if row[cur_row+1][cur_col] == -1:
               cur_row += 1
             else:
               direction = 3
               cur_col -= 1
               continue
           else:
             direction = 3
             cur_col -= 1
             continue
        if direction == 3:
           row[cur_row][cur_col] = i+1
           if cur_col - 1 >= 0:
             if row[cur_row][cur_col-1] == -1:
               cur_col -= 1
             else:
               direction = 4
               cur_row -= 1
               continue
           else:
               direction = 4
               cur_row -= 1
               continue

        if direction == 4:
           row[cur_row][cur_col] = i+1
           if cur_row-1 >= 0:
             if row[cur_row-1][cur_col] == -1:
               cur_row -= 1
             else:
               direction = 1
               cur_col += 1
               continue
           else:
             direction = 1
             cur_col += 1
             continue
             
    return row

print(spiral_order(1))
