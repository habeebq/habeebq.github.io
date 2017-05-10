Title: Practical Use of Types in VHDL
Date: 2016-08-06
Category: VHDL, Digital Design
Authors: habeebq

Types and subtypes are widely used in VHDL to organise your code and data.

So what prompted me to write about types? A colleague showed me some of his code
that was using types in a way that I hadnt realized possible before.
At that point I realized it was time for me to re-visit the core concepts of types. This
was something I was meaning to do for a long time, but never had the motivation to do so.


# Difference between Types and Subtypes
A type is a VHDL construct provided by the Language Definition.

A subtype is derrived from a type with additional constraints.

> However, subtypes are only safer in simulation; in real hardware, there are no boundary checks


# Examples of Types

    :::VHDL
    type enum_type is (STATE_IDLE,
                       STATE_READ,
                       STATE_WRITE,
                       STATE_COMPLETE);
    

# Word about the type that is record
Records are very useful types in organizing VHDL code.
However, being an abtract type they have some disadvantages.
Mainly different EDA tools handle them differently, and more often than not,
records become unrecognisable within the tool (for e.g. a synthesized netlist).
Moreover there are some challenges with a signal that is declared as a record type
as it needs to be assigned all within the same process so that tools do not get too confused.

# Enum Types
Enum types are great. They also suffer from visibility problems and debugging on an
emulator and FPGA can be tricky, as you need to know the mapping of an enum to a vector.

These types are frequently used in state machines.
The synthesis tools have the option to synthesise this as they want to optimize timing/area/power.
They can be encoded as a binary vector, or one-hot encoded.

Enum types can be cleverly used to make code a lot more readable and they can be used to replace integers, or as a pre-defined hash table.

# Ranged Types/Subtypes: Integer/Natural 
A range specifies a subset of values of a scalar type.

A range constraint is compatible with a subtype if each bound of the range belongs to the subtype or if the range constraint defines a null range.

[source](http://rti.etf.bg.ac.rs/rti/ri5rvl/tutorial/TUTORIAL/IEEE/HTML/1076_3.HTM)


On inital searching for a way to define a range type, for some reason I came up with nothing.

Until a colleague mentioned this to me, and since then I am dissapointed I didnt know about this before.

So lets say you need to pack fields into a big vector.

At some point you need to slice it to extract elements and put in elements.

##### Method one:
Define FIELD0_MSB, FIELD0_LSB and so on for each field in the vector.
The problem with this is inserted or removing a new field requires updating the table of all the fields.

##### Method two:
Define FIELD_OFFSET, FIELD_SIZE
also  FIELD1_OFFSET = FIELD0_OFFSET + FIELD0_SIZE
This allows you to easily insert/remove fields.
However this method is still very clunky and requires function to pack/unpack items.

It still doesnt allow easy slicing which has to be done:

vector(FIELD_TABLE(FIELD_ELEMENT).OFFSET + FIELD_TABLE(FIELD_ELEMENT).SIZE downto FIELD_TABLE(FIELD_ELEMENT).OFFSET);

Also, my simulation tools didnt like this, so I had to recode it as subtypes.

##### Method 3: Using subtypes

Define

	:::vhdl
	subtype field0 is std_logic_vector(13 downto 5);
	signal myvector : std_logic_vector(field0'RANGE);

However for the subtype you still need to define a table of MSBS and LSBS.

##### Method 4: Using range type
This is the one that eluded me and I am trying to get to grips with this one.

	:::vhdl
	subtype FIELD0_RANGE is integer range 13 downto 5;
	signal myvector : std_logic_vector(FIELD0_RANGE);

Personally I found this a bit counter-intuitive, until I accepted that an integer type is just a range type. And there is a difference between an integer type and an assigned integer value which takes up one value from the range of values in the integer type.

`FIELD0_RANGE` is just a constrained integer type, right?

signal my_int : FIELD0_RANGE := 8;

is a single value, right?

However we are not using an instance of that range, we are using the type definition of it.

The type definition itself is actually a range, whereas the signal is a single value from that range.

In method 3, we saw that std_logic_vector has an attribute `'RANGE` that returns a range. 

What is interesting is how you can interchange between a type and a value (while we could consider the value just another constrained type).

How does this work for enums?

What is the difference between `vector(ENUM_TYPE)` and `vector(ENUM_VALUE)`?
There is none. Starts to make sense now?

How about arrays?
`array(ENUM_TYPE)` assigns a number of values at the same time
`array(ENUM_VALUE)` assigns one value at a time.

like

    :::VHDL
    vector <= (ENUM_TYPE  => "0",     ENUM_VALUE => "0");
    vector <= (5 downto 1 => "00000", 0 => "0");


There is something similar for records as well

    record <= (OFFSET => "000", SIZE => "001");

