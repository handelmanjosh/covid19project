# covid19project
stochastic simulation designed to test the spread of COVID-19 through a school-like environment

This was done in two weeks as my earlier project with my mentor over the summer fell through. Some parts aren't that pythony because I learned python as I was doing the project

The added file, vaxmask0to4.py, is a variation of the simulation testing the effect of masking with an effectivity of 10% to 40%, and vaccination of 20 to 80 people per day. 

The "threadingalternate" file is the most recent iteration of the school simulation. Feel free to play around with the parameters, they are located starting at line 877. The simulation takes a while to run, 12 hours on average on my computer. The original plan with a timestep of 1 second, allowing me to simulate spread while people are on the move, took >80 hours to run. 

Basically what the simulation does is 
1. Create a simulated school environment based upon my school (held constant throughout trials)
2. Simulate spread on a person-by-person basis
3. Implement control methods in a realistic way, evaluate their success


The novelty of this simulation is threefold. 
1. It dynamically changes networks based on realistic variations in contact throughout the environment over time without the need for complicated equations
2. It implements control methods in a realistic way, not by simply changing parameters in differential equations
3. People are represented as individuals, not as part of a group like in compartmental models


In the simulation itself, there are a lot of parameters that can be changed. I could not run all tests at the same time due to computational limitations, so I would change different parameters, making different files that I could run on my different computers. A whole bunch of possible variations were just added. 
