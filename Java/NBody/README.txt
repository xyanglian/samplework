Name: Liane Yanglian
NetID: xy48
Hours Spent: 8.5 hours
Consulted With: Yi Lu (TA)
Resources Used: NONE
Impressions: I didn't understand the writeup and read many times before I had a sense of what I was supposed to do. This assignment was quite fun once I got the hang of it. 

Question 1: What is the final position of the planets after 1,000,000
seconds with a timestep of 25,000?

                 px                        py
                                 
                                 
earth    1.4657072579675333E11    2.9603571820026024E10 

mars     2.265919409244593E11     2.4055025673504623E10 

mercury  3.863596759797241E10     4.2569286276404396E10 

sun      26826.758124022017       2979.2451384889378 

venus    1.0243682251001347E11    3.4391417962295876E10 


Question 2: For what values of timeStep, does the simulation no longer behave correctly? 

I used a totalTime of 10,000,000 (all units are seconds) for all my trials to keep the total time constant and in perspective. I started from the default value, 25000 for timeStep, and then multiplied it by 10 for each of the trails to reduce the number of trials needed. However, I noticed than for 2,500,000, one of the planets (the grey one) is missing from the screen so I tried 350,000 instead. As it turned out, after the value of timeStep exceeds timeStep = 450,000, the planets stop at a different position then the default stopping position I saw with the default values of timeStep = 25,000 and totalTime = 10,000,000. This can be an indication that the planets are not following their orbits around the Sun.
Furthermore, the planets start to be more visually off the orbits around the Sun starting from timeStep = 1,200,000, and obviously so at around timeStep = 1,250,000. At timeStep = 1,300,000, one of the planets (the grey one) starts to look like it's flying off, and half of it flies off the screen at around timeStep = 1,395,000.


