# Python_Snake
Here I created a simple snake game and used q-learning library to train a Keras model to play the game.

# Snake game engine

Creating the initial snake game engine was an exercise I gave myself to help learn Python language.
A year later I came back to the project and recreated the same game using Numpy instead of Python Lists.

The difference in performance between the two approaches can be seen in examples bellow: 


![](images/high_pixel_count.png?raw=true)

To no one's surprise Numpy is great at handling big arrays quickly, and the first plot illustrates that very well.
While the execution time of lists is skyrocketing, Numpy holds its ground and barely nudges from its straight track. A truly magnificent sight. 

![](images/low_pixel_count.png?raw=true)

A different story is told in the second plot, though. When the game deals with very small arrays (up to ~ 17x17 pixels) 
the advantages of Numpy are overshadowed by its overhead. Here simple Python lists and newbie coding win against Numpy. 


To be honest, before creating the Numpy version of the game engine I expected it to crush my java-ish implementation of 
snake game with Python lists. And trust me was I disappointed to find that my new work was, in fact, slower. But after 
putting on the data scientist mask and analyzing the differences between the two game engines I was a tiny bit less bummed out 
about the whole situation - apparently my new implementation is pretty good. Just not in my use case...

# Chapter 2: The Model

The model, as of this point, has yet to be firmly decided on. The current version is a simple convolutional neural network 
taking the current game state and some previous frames as an input and producing an output of next frame's movement direction. 
The model is based on the q-learning reinforcement paper. Model itself can be improved once the data acquisition pipeline 
has been developed further, but as of now it is a prototype showing that the idea is plausible.


Example of current trained model at work:


![](images/gameplay/gameplay_0.gif?raw=true)

To be continued...
  
