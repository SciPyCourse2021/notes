### Homework 1

Use docstrings and good style, and don't forget to test your code! Optimal solutions to these can be as short as 6 lines of code or less. If yours are much longer, then you're probably doing it the hard way. Write your solutions in a file named `yourname_homework1.py` and submit to `m.spacek@lmu.de` before class 03 (May 4).

1. Write a function called `vowelcount()` that takes a string as an argument, and returns the number of vowels in the string. Test it, e.g. `vowelcount('hEllo')`, `vowelcount('wOrld')`. It should ignore whether the vowels are captial or lowercase.

2. Write a function called `metric()` that takes two numbers `x` and `y`, prints their difference and sum in a single clear, nicely formatted message (e.g. `difference is 1, sum is 5`), and returns the difference divided by the sum. Test it, e.g. `metric(2, 3)`, `metric(10, 0.1)`. What happens if the sum is 0? What can you do to handle that case?

3. Write a function called `multtable()` that takes a number `n` and prints out the multiplication table for integers 1 through `n`. The multiplication table should look like a spreadsheet, with rows containing values `1 2 3...n`, `2 4 6...2n`, `3 6 9...3n`, etc. Hint: use two `for` loops, each with a different loop variable. Bonus: check the help for `print()` to figure out how to print each row in the table in a single horizontal line.
