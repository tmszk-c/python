tab = [9,41,12,3,74,15] 
class sherch_number():
    found = False
    print("before", found)
    for value in tab:
        if value == 3:
            found = True
        print(found, value)
        found = False
    print('after', found)

class the_largest_value():
    largest_so_far = -1
    print('before', largest_so_far)
    for the_number in tab:
        if the_number > largest_so_far:
            largest_so_far = the_number
        print(largest_so_far, the_number)
    print('after', largest_so_far)

    jslkj;lkfjslkdjf dkjfsldkf class the_smallest_value():  
    smallest_so_far = None
    print('before', smallest_so_far)
    for the_number in tab:
        if smallest_so_far is None:
            smallest_so_far = the_number
        elif the_number < smallest_so_far:
            smallest_so_far = the_number
        print(smallest_so_far, the_number)
    print('after', smallest_so_far)