import java.util.Random;
public class MyProgram extends ConsoleProgram
{
    public void run()
    {
        Random r = new Random();
        
        String currentSide = "";
        
        int headsCounter = 0;
        int tailsCounter = 0;
        
        int headStreak = 0;
        int headStreakSave = 0;
        
        for (int i = 0; i < 100; i++)
        {
            boolean flip = r.nextBoolean();
            
            if (flip == true)
            {
                currentSide = "Heads";
                headsCounter++;
                headStreak++;
                if (headStreak > headStreakSave)
                {
                    headStreakSave = headStreak;
                }
            }
            else if (flip == false)
            {
                currentSide = "Tails";
                tailsCounter++;
                headStreak = 0;
            }
            
            System.out.println(currentSide);
        }
        
        double percentHeads = (double)headsCounter / 100;
        double percentTails = (double)tailsCounter / 100;
        
        System.out.println("");
        System.out.println("Total number of heads: " + headsCounter);
        System.out.println("Total number of tails: " + tailsCounter);
        System.out.println("");
        System.out.println("Longest streak of heads: " + headStreakSave);
        System.out.println("");
        System.out.println("% heads: " + percentHeads);
        System.out.println("% tails: " + percentTails);
    }
}
