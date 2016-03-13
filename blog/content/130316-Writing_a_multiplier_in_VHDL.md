Title: Writing a 2x2 Matrix Multiplier in VHDL
Date: 2016-03-13
Category: VHDL
Authors: habeebq

There probably isnt a lot to talk about in a simple 2x2 matrix multiplier, but I thougt I'd like to post something basic and then explore its various aspects like verification and coding style etc.

In this post (which I am writing in markdown), I am not going to go to the effort of writing matrix notation so I will try to describe what I can in basic text form.

A simple 2x2 matrix contains just 4 elements in the form of:

    a(i,j) | where i=0,1 and j=0,1


### Data structure

In order to represent this in VHDL we need to create a data structure.

The usual way I do this is in two steps:

    :::vhdl
    type t_1d_array is array(integer range 0 to 1) of std_logic_vector(7 downto 0);
    type t_2d_array is array(integer range 0 to 1) of t_1d_array;

The alternative is to declare a 2D array directly:

    :::vhdl
    type t2_2d_array is array(integer range 0 to 1, integer range 0 to 1) of std_logic_vector(7 downto 0);

I dont see a real difference between declaring the arrays either way.
In terms of hardware synthesized there could be a difference(timing, prioritized paths), depending on how you access or assign the arrays (row-wise or column-wise operations).
However for a matrix multiplier where each element is assigned/accessed in the same way, it probably makes no difference.
It is probably more of a logical distinction, especially when declaring look-up-tables, how you partition your arrays.

The slight difference in accessing the elements of the array will be:

    :::vhdl
    signal a : t_2d_array;
    a(x)(y) <= value;

while for the second declaration:

    :::vhdl
    signal a : t2_2d_array;
    a(x,y) <= value;
    


