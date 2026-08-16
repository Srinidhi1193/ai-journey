""" Write a program that:

Asks the user for a number n
Using nested loops, print a multiplication grid from 1 to n — rows and columns — like:
   1   2   3   4
   2   4   6   8
   3   6   9   12
   4   8   12  16

(for n=4: row i, column j, value = i*j, for i and j both from 1 to n)
3. Twist: while building the grid, skip printing any value that is a multiple of 3 — print -- in its place instead (but still keep the grid shape/alignment)
4. Separately, count how many values were skipped (i.e., how many multiples of 3 appeared in the grid), and print that count after the grid

Example, if n=4:

1   2   --  4
2   4   --  8
--  --  9   --
4   8   --  16
Skipped: 5

(Trace: 3,6,3,6,9,3,6,12 across the grid... — the point is to trust your loop, not manually match this exact grid; different people's n will differ) """

skip =0
n = int(input("Enter a number: "))
for i in range(n):
    for j in range(n):
        val = (i+1)*(j+1)
        if val % 3 ==0:
            val = "--"  
            skip+=1    
        print(val, end ="  ")
    print()
print("Skipped: ",skip)
