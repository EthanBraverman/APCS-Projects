public class MyProgram extends ConsoleProgram
{
    public void run()
    {
        
        int integer1 = 1;
        boolean intPos = false;
        
        while(intPos == false)
        {
            integer1 = readInt("Enter a positive integer: ");
            if(integer1 > 0)
            {
                intPos = true;
            }
            else
            {
                System.out.println("That integer is not positive.");
                System.out.println("");
            }
        }
        
        System.out.println("");
        System.out.print(integer1);
        
        while(integer1 != 1)
        {
            if(integer1 % 2 == 0)
            {
                integer1 /= 2;
            }
            else if(integer1 %2 == 1)
            {
                integer1 *= 3;
                integer1 += 1;
            }
            
            System.out.print(" " + integer1);
        }
        
    }
}
