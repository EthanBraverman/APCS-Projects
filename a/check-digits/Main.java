public class MyProgram extends ConsoleProgram
{
    public void run()
    {
        String str = readLine("Enter your string: ");
        System.out.println();
        int option = readInt("Would you like to [1] get check digits for your string or [2] validate your check digits? ");
        System.out.println();
        
        if (option == 1)
        {
            System.out.println("Check digits for your string are: " + getCheckDigit(str));
        }
        else if (option == 2)
        {
            System.out.println("Your check digits are valid: " + isValid(str));
        }
        else
        {
            System.out.println("That is not a valid option.");
        }
    }
    
    public String getCheckDigit(String val)
    {
        String checkDigits = "";
        
        if (val.indexOf("5") != -1)
        {
            if (val.indexOf("9") == 0)
            {
                checkDigits += "H";
            }
            else
            {
                checkDigits += "h";
            }
        }
        else
        {
            if (val.indexOf("9") == 0)
            {
                checkDigits += "B";
            }
            else
            {
                checkDigits += "b";
            }
        }
        
        if (val.length() <= 3)
        {
            checkDigits += "3";
        }
        else if (val.length() >= 4 && val.length() <= 6)
        {
            checkDigits += "6";
        }
        else
        {
            checkDigits += "8";
        }
        
        return checkDigits;
    }
    
    public boolean isValid(String test)
    {
        String originalString = test.substring(0, test.length() - 2);
        String originalCheckDigits = test.substring(test.length() - 2, test.length());
        
        boolean valid = getCheckDigit(originalString).equals(originalCheckDigits);
        return valid;
    }
}
