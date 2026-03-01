# Basic Java FRQ: Convergence Algorithm

Mathematician Stanislau Ulam hypothesized that all positive integers converge to 1 if treated as follows:

- If it is odd, multiple by 3 and add 1
- If it is even, divide by 2
- Repeat this process with the result if each calculation

Write an algorithm that tests this theory

| Algorithm Steps | Sample Problem |
| -------- | ------- |
| **Step 1:** Start with a positive, non-zero integer | `integer1` is 3 |
| **Step 2:** If `integer1` is odd, multiply by 3 and add 1 <br> If `integer1` is even, divide by 2 | `integer1` is odd. 3 * 3 + 1 = 10. <br> `integer1` is now 10. |
| **Step 3:** Print the current value of `integer1` | Print 10 |
| **Step 4:** If `integer1` is 1, you ar finished | `integer1` is not 1. You are not finished. |
| **Step 5:** Repeat steps 2 - 4 until `integer1` is 1 | 10 / 2 = 5 &ensp; Print 5 <br> 5 * 3 + 1 = 16 &ensp; Print 16 <br> 16 / 2 = 8 &ensp; Print 8 <br> 8 / 2 = 4 &ensp; Print 4 <br> 4 / 2 = 2 &ensp; Print 2 <br> 2 / 2 = 1 &ensp; Print 1 <br> `integer1` is now 1, you are finished. |

Write a `run` method that follows the steps of Ulam's hypothesis, as described above. Ask users for an integer, and print the results on one line.
<br><br>
Sample output for `integer1 = 3`: **10 5 16 8 4 2 1**
<br><br>
**Precondition:** `integer1` is an integer greater than 0.
**Postcondition:** Prints all of the numbers on one line.
