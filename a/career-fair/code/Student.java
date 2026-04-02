public class Student
{
    private int room;
    
    public Student(int room)
    {
        this.room = room;
    }
    
    public int getRoom()
    {
        return room;
    }
    
    public void nextRoom()
    {
        room += 1;
        
        if (room == 7)
        {
            room = 1;
        }
    }
}
