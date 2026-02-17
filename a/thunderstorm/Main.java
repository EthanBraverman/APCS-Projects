public class Main extends ConsoleProgram
{
    public void run()
    {
        double seconds = readDouble("How many seconds are between the flash and the thunderclap? ");
        double windSpeed = readDouble("What is the wind speed in mph? ");
        
        double distance = seconds / 5;
        windSpeed /= 60;
        
        System.out.println();
        System.out.println("The storm is now " + distance + " miles away.");
        
        int timeElapsed = 1;
        
        for (double i = distance - windSpeed; i > 0; i -= windSpeed)
            {
                System.out.println("In " + timeElapsed + " minutes, the storm will be " + i + " miles away.");
                timeElapsed ++;
            }
        
        System.out.println("In " + timeElapsed + " minutes, the storm will be here.");
    }
}
