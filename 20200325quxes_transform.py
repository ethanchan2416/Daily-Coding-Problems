# On a mysterious island there are creatures known as Quxes which come in three colors: red, green, and blue.
# One power of the Qux is that if two of them are standing next to each other, they can transform into a single creature of the third color.
# Given N Quxes standing in a line, determine the smallest number of them remaining after any possible sequence of such transformations.
# input = ['R', 'G', 'B', 'G', 'B']
# output = 1

testset = ['R', 'G', 'B', 'G', 'B']
homogeneous_set = ['R', 'R', 'R']
color_set = {'R', 'G', 'B'}


def check_equal(iterator):
    return len(set(iterator)) <= 1


def transform_min_num(testset):
    idx = 0
    while check_equal(testset) is False:
        if testset[idx] is not testset[idx + 1]:
            testset[idx + 1] = list(color_set.difference({testset[idx], testset[idx + 1]}))[0]
            testset.pop(idx)
            idx = 0
        else:
            idx += 1

    return len(testset)


print("testset = ", testset)
min_num = transform_min_num(testset)
print("Smallest number of remaining Quxes for testset is ", min_num)

print("homogeneous_set = ", homogeneous_set)
min_num = transform_min_num(homogeneous_set)
print("Smallest number of remaining Quxes for homogeneous_set is ", min_num)


# Display Results
# testset =  ['R', 'G', 'B', 'G', 'B']
# Smallest number of remaining Quxes for testset is  1
# homogeneous_set =  ['R', 'R', 'R']
# Smallest number of remaining Quxes for homogeneous_set is  3
# [Finished in 0.2s]
