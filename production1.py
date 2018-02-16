def remove_duplicates(a_list):
    bb_list = [a_list[0]]
    for i in a_list:
        if i in bb_list:
            continue


        else:
            bb_list.append(i)
    return bb_list

print(remove_duplicates([1,2,3,4,4,1]))
