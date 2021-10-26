


def binary_search(sequence,item):
    begin_index=0
    end_index=len(sequence)-1
    while begin_index<=end_index:
        midpoint=begin_index+(end_index-begin_index)//2
        midpoint_value=sequence[midpoint]
        if midpoint_value==item:
            return midpoint_value
        elif item<midpoint_value:
            end_index=midpoint-1
        else:
            begin_index=midpoint+1
    return "ERROR,YOUR REQUEST CAN'T BE COMPLETE"
sequence_a=[1,2,3,4,5,6,7,8,9,0]
item_a=123
print(binary_search(sequence_a,item_a))