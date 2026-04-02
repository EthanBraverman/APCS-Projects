public class CareerFair extends ConsoleProgram
{
    public void run()
    {
        Student sam = new Student(5);
        System.out.println("sam will begin in room 5.");
        
        System.out.println("sam's current room is " + sam.getRoom() + ".");
        
        sam.nextRoom();
        System.out.println("sam is moved to the next room (room 6).");
        
        System.out.println("sam's current room is " + sam.getRoom() + ".");
        
        Student fran = new Student(3);
        System.out.println("fran will begin in room 3.");
        
        sam.nextRoom();
        System.out.println("sam is moved to the next room (room 1).");
        
        System.out.println("sam's current room is " + sam.getRoom() + ".");

        System.out.println("fran's current room is still " + fran.getRoom() + ".");
    }
}
