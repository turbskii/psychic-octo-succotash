smallest_so_far = 1000
print('before', smallest_so_far)
for the_num in [23, 43, 176, 1667, 2, 11, 69] :
    if the_num < smallest_so_far:
        smallest_so_far = the_num
    print(smallest_so_far, the_num)

print ('after', smallest_so_far)
