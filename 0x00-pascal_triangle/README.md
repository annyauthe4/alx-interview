<h1> Pascal Triangle </h1>
Pascal triangle is a useful mathematical solution used in algebra, probability and combinatorics.
It follows the formula
nCr = n! // r! * (n - r)!

<h1><i> How to get the result</i></h1>
The result is a list of lists.
The next list is derived by assuming 0 before the first element and the last element in the previous list.
So that the elements of the next list will be the sum of the two numbers above it.
Note that the first number in the triangle is 1 and every other rows have 1 as the first and the last elements.

res = [[1]] a list of lists with the first list
A loop is set to run for n number of times, in our case n-1 since the first list is derived.
A temporary list is set which adds 0 as the first and the last element of the current list.
An empty list is set as the current row.
Another loop is used to generate the elements of the current list which ranges as the lenght of the
last list in the list of lists + 1.
the temp is them appended on the row as the value of the first element and the element next to it.
The row is appended to the res at the end of the loop.
