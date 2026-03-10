public class MyProgram extends ConsoleProgram
{
    public void run()
    {
        String password = readLine("Enter a password: ");
        System.out.println("You password meets the requirements: " + passwordRuleCheck(password));
    }
    
    public boolean passwordRuleCheck(String userPass)
    {
        String digits = "0123456789";
        String specialCharacters = "@%#";
        
        int digitsCounter = 0;
        int specialCharCounter = 0;
        
        if (userPass.length() < 8)
        {
            return false;
        }
        
        for (int i = 0; i < userPass.length(); i++)
        {
            char cur = userPass.charAt(i);
            
            if (digits.indexOf(cur) != -1)
            {
                digitsCounter += 1;
            }
            
            if (specialCharacters.indexOf(cur) != -1)
            {
                specialCharCounter += 1;
            }
        }
        
        if (digitsCounter > 0 && specialCharCounter > 0)
        {
            return true;
        }
        else
        {
            return false;
        }
    }
}
