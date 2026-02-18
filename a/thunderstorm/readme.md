# Basic Java FRQ: Modeling a Thunderstorm
It is possible to calculate the distance from a thunderstorm by counting the number of seconds between seeing the flash of lightning and hearing the thunderclap. This can be expressed by the equation **distance = seconds / 5**. For example, if there are 10 seconds between the flash and the thunderclap, the storm is 2 miles away. (10 / 5 = 2)
<br><br>
Wind speed determines how fast a storm moves. For example, if the wind speed is 30 miles per hour, the storm will move 0.5 miles in one minutes (30 miles per hour / 60 minutes in an hour = 0.5 miles).
<br><br>
Implement a run method that asks the user for the starting seconds between the flash and the thunderclap. and the windspeed in miles per hour. (Assume the wind speed will not change until the storm arrives.)
<br><br>
Print how many miles away the storm is at the start. Then print how far away the storm will be each minute between now and when it arrives. (It arrives when the distance from the storm is ≤ 0.)
<br><br>
Sample output:<br>
&nbsp;&nbsp;&nbsp;&nbsp;"The storm is now 2.0 miles away"<br>
&nbsp;&nbsp;&nbsp;&nbsp;"In 1 minutes, the storm will be 1.5 miles away."<br>
&nbsp;&nbsp;&nbsp;&nbsp;"In 2 minutes, the storm will be 1.0 miles away."<br>
&nbsp;&nbsp;&nbsp;&nbsp;"In 3 minutes, the storm will be 0.5 miles away."<br>
&nbsp;&nbsp;&nbsp;&nbsp;"In 4 minutes, the storm will be here."
<br><br>
Precondition #1: `seconds` and `windspeed` are positive, non-zero doubles.<br>
Precondition #2 `windSpeed` is constant.
<br><br>
Postcondition #1: Print the distance from the storm at the start time and at every subsequent minute until the storm arrives.<br>
Postcondition #2: The method outputs a correct result for any positive, non-zero initial values of `seconds` and `windspeed`.
