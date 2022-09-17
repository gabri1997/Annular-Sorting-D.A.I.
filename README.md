# Annular-Sorting-D.A.I
This is a project done for the course of Distributed Artificial Intelligence 

# What is it ?
The main scope of this project is to show the concept of Collective intelligence. Such a phenomenon is observable by analyzing how ants interact with each other.
Local interactions between individuals lead to a global self-organized system’s behavior; note that swarm intelligence is not an «accident» but a property of a various systems due to natural evolution.

The project is inspired by an intriguing hypothesis concerning the nesting mechanism of Temnothorax colonies
The study showed that Temnothorax ants formed cluster of objects in the nest, placing smaller brood items at the center with a greater density, while the bigger ones are placed in the contour,  forming an annular arrangement
This behavior is replied each time the ants were forced to migrate to a new nesting site

# The goal 

Despite the exact mechanism that ants use to re-create these  patterns is not fully known, we want to replicate the behaviour observed in Temnothorax colonies, where the broods were picked up and released forming a kind of annular structure, as shown by the pictures.

# The core algorithm

The core algorithm
Laden ants carry objects around the environment and at every step (after delay) they evaluate what placement score the carried object would have if it were to be deposited at the current point. That score will be used to probabilistically determine whether the object should be dropped. 
When evaluating the placement score of an object, the ant counts how many nearby objects fall within the minimum perimeter (these contributes with a predefined penalty) and how many fall within the maximum perimeter (these contributes with a predefined bonus).
As a result, groups of smaller objects will tend to «force out» larger objects!
