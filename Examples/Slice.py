# Slicing is a way to extract a portion of a sequence (for example a string in a list)

# sequence[start:end:step] - where start is the index of the first element to INCLUDE in the slice, end is the index
# of the first element to EXCLUDE from the slice, and step is the stride of increment for the slice.

numbers = [1, 2, 3, 4, 5]

slice = numbers[1:4]
print(slice)
# prints [2, 3, 4]
# this will create a new list called slice_example containing the elements at indices -3 and -2 of the original list
# numbers

