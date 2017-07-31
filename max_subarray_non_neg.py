class Solution:
    # @param A : list of integers
    # @return a list of integers
    def maxset(self, A):
           global_max = 0
           global_elem_num = 0
           global_list = []
           local_max = 0
           local_elem_num = 0
           local_list = []
           for i in range(0,len(A)):
                if len(A) < 1:
                  break
                if A[i] < 0:
                  if local_max > global_max:
                    global_max = local_max
                    global_elem_num = local_elem_num
                    global_list = local_list
                  elif local_max == global_max:
                    if local_elem_num > global_elem_num:
                      global_elem_num = local_elem_num
                      global_list= local_list
                  local_list = []
                  local_elem_num = 0
                  local_max = 0
                  continue
                local_max += A[i]
                local_elem_num += 1
                local_list.append(A[i])
           if local_max > global_max:
              global_list= local_list
           elif local_max == global_max and local_elem_num >global_elem_num:
              global_list= local_list
           return global_list
