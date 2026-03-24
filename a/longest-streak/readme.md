# The Longest Streak

Write a run method that simulates flipping a coin 100 times, by generating a random boolean. If the random boolean is `true`, the flip is Heads. If the random boolean is `false`, the flip is Tails. 

Your first few lines of code must be:

```
import java.util.Random;
public class MyProgram extends ConsoleProgram
{
    public void run()
    {
        Random r = new Random();
```

The code to generate a random boolean is: `r.nextBoolean()`
<br><br>
Print out the result of every flip (either heads or tails). After 100 flips, print the results:
- Total number of heads and tails (as an integer)
- Longest streak of heads (as an integer)
- % heads and % tails (as a decimal)
