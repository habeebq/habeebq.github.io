Title: Writing a 2x2 Matrix Multiplier in VHDL
Date: 2016-03-13
Category: VHDL
Authors: habeebq

There probably isnt a lot to talk about in a simple 2x2 matrix multiplier, but I thougt I'd like to post something basic and then explore its various aspects like verification and coding style etc.

In this post (which I am writing in markdown), I am not going to go to the effort of writing matrix notation so I will try to describe what I can in basic text form.

A simple 2x2 matrix contains just 4 elements in the form of:

    a(i,j) | where i=0,1 and j=0,1

In order to represent this in VHDL we need to create a data structure.

The usual way I do this is in two steps:

    :::vhdl
    type t_1d_array is array(integer range 0 to 1) of std_logic_vector(7 downto 0);

