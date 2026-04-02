# Career Fair

Consider a Career Fair, designed to give students exposure to the activies of different professions. Students will move through various activity rooms during the course of the event, to explore a variety of career options. There are six different activity rooms, numbers from 1-6 (inclusive). An individual student may start in any activity room. Once the student has completed the activity in that room, the student will move on to the next room sequentially. For example, a student who starts in room 3 will move to room 4, and so on. Students in room 6 will move on to room 1.
<br><br>
The `Student` class is designed to track students' movements throughout the event. A `Student` object is constructed with a starting room number, which will be an integer from 1 to 6 (inclusive).
<br><br>
The table below lists some sample code segments and their results.
| **Code** | **Value Returned (blank if nothing is returned)** | **Explaination** |
| -------- | ------- | ------- |
| `Student sam = new Student(5);` |  | sam will begin in room 5. |
| `sam.getRoom();` | 5 | sam's current room is 5. |
| `sam.nextRoom();` |  | sam is moved to the next room (room 6). |
| `sam.getRoom();` | 6 | sam's current room is 6. |
| `Student fran = new Student(3);` |  | fran will begin in room 3. |
| `sam.nextRoom();` |  | sam is moved to the next room (room 1). |
| `sam.getRoom();` | 1 | sam's current room is 1. |
| `fran.getRoom();` | 3 | fran's current room is still 1. |

<br>

Write the complete `Student` class, including the constructor and any required instance variables and methods. Your implementation must meet all specifications and conform to the example.
