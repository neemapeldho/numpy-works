"""
Naive bayes algorithm 
=====================

Used for classification
======================

where prediction is based on probability based calculation
==========================================================

probability : chances for occuring an event
===========================================

probability (head) = 1 / 2 = 0.5

p(dice) = 1 / 6 

types of probability
=====================
marginal - one chance of occur
# chances for occuring a single event A

joint   - occur same
# chances for occuring both events A and B

conditional - based on one occur predict next one (naive bayes follow)
# chances for occuring event A where event B has already occured
# based on the result B we need to calculate the probability of occuring event A



weather          Temp       play
=======         ======      =====
sunny            hot         No
sunny            hot         No
rainy            mild        Yes
rainy            cool        Yes
sunny            cool        No


Prior probability
=================
P(Yes) = 2 / 5
P(No)  = 3 / 5


Conditionals
============
P(weather = "rainy" | play = "Yes") = 2/2  = 1   # rainy yes = 2 , play yes = 2
P(weather = "rainy" | play = "No")  = 0/3  = 0

P(Temp = "hot" | play = "Yes") = 0/2  = 0      # hot yes = 0  ,   play  yes = 2
P(Temp = "hot" | play = "No")  = 2/3  = 0.67


Joint Likelihood
================
P(Yes|features(weather = "rainy",Temp = "hot")) = 1 * 0     = 0
P(No|features(weather = "rainy",Temp = "hot" )) = 0 * 0.67  = 0


Unnormalized posteriors = joint likelihood * prior
=======================
P(Yes|features(weather = "rainy",Temp = "hot")) * P(Yes) = 0 * 2/5 = 0
P(No|features(weather = "rainy",Temp = "hot" )) * P(No)  = 0 * 3/5 = 0
"""

