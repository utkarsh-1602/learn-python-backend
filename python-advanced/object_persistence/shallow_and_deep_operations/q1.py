# Shallow copy

import copy


mylist = [1,2,[3,4]]
shallow_copy = copy.copy(mylist)

# This means shallow_copy[0] references the same 1, shallow_copy[1] references the same 2, and shallow_copy[2] references the same sublist [3, 4].
# shallow_copy = copy.copy(mylist): Creates a shallow copy of mylist. The top-level list is copied, but the reference to the sublist [3, 4] is shared.

mylist[1] = 100
# Since integers are immutable, this operation changes the reference in mylist to point to a new integer 100. The original reference to 2 is not affected, so shallow_copy[1] still points to 2.

print(shallow_copy)


mylist[2][0] = 'utkarsh'
print(shallow_copy)