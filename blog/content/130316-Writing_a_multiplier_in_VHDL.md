Title: Writing a 2x2 Matrix Multiplier in VHDL
Date: 2016-03-13
Category: VHDL
Authors: habeebq

There probably isnt a lot to write about in a simple 2x2 matrix multiplier, but I thougt I'd like to post something basic and then explore its various aspects like verification and coding style etc.

In this post (which I am writing in markdown), I am not going to go to the effort of writing matrix notation so I will try to describe what I can in basic text form.

A simple 2x2 matrix contains just 4 elements in the form of:

    a(i,j) | where i=0,1 and j=0,1


### Data structure

In order to represent this in VHDL we need to create a data structure.

The usual way I prefer to do this is in two steps:

    :::vhdl
    type t_1d_array is array(integer range 0 to 1) of std_logic_vector(7 downto 0);
    type t_2d_array is array(integer range 0 to 1) of t_1d_array;

The alternative is to declare a 2D array directly:

    :::vhdl
    type t2_2d_array is array(integer range 0 to 1, integer range 0 to 1) of std_logic_vector(7 downto 0);

There isnt a real difference between declaring the arrays either way.
In terms of hardware synthesized there *could* be a difference(timing, prioritized paths), depending on how you access or assign the arrays (row-wise or column-wise operations).
However for a matrix multiplier where each element is assigned/accessed in the same way, it makes no difference.
It is an abstract distinction, especially when declaring look-up-tables, how you partition your arrays.

The slight difference in accessing the elements of the array will be:

    :::vhdl
    signal a : t_2d_array;
    a(x)(y) <= value;

while for the second declaration:

    :::vhdl
    signal a : t2_2d_array;
    a(x,y) <= value;
    
Now lets define our entity and ports. We need two input matrices of type `t_2d_array` and one output matrix also of `t_2d_array`.

    :::vhdl
    entity mult_2x2 is
        port (
        in_matrix1 : in  t_2d_array;
        in_matrix2 : in  t_2d_array;
        out_matrix : out t_2d_array
        );
    end mult_2x2;

Now lets define the matrix operation.
A matrix multiplication is a simple row-to-column wise multiplication and addition
i.e the row elements of the first matrix are multiplied the the column elements of the second matrix, and added up.

    c(i) = sum[ a(x) * b(y) ] where x=0 to i, y=0 to j

In VHDL we can write each individual element as,

    :::vhdl
    out_matrix(0)(0) <= std_logic_vector(
                           signed(in_matrix1(0)(0)) * signed(in_matrix2(0)(0)) +
                           signed(in_matrix1(0)(1)) * signed(in_matrix2(1)(0)));
    out_matrix(0)(1) <= std_logic_vector(
                           signed(in_matrix1(0)(0)) * signed(in_matrix2(0)(1)) +
                           signed(in_matrix1(0)(1)) * signed(in_matrix2(1)(1)));
    out_matrix(1)(0) <= std_logic_vector(
                           signed(in_matrix1(1)(0)) * signed(in_matrix2(0)(0)) +
                           signed(in_matrix1(1)(1)) * signed(in_matrix2(1)(0)));
    out_matrix(1)(1) <= std_logic_vector(
                           signed(in_matrix1(1)(0)) * signed(in_matrix2(0)(1)) +
                           signed(in_matrix1(1)(1)) * signed(in_matrix2(1)(1)));


Now there are a couple of things to consider in the above lines of code.

1. You can see an insane amount of typecasting going on here. This is the result of VHDL's strongly type nature.
VHDL forces you to define the nature of numbers before performing an operation on them.
Since we chose to store them as `std_logic_vector`, we now need to cast them as `signed` before every operation, and then cast them
back to `std_logic_vector` before assigning them.

2. Bitwidths. Usually most hardware is done as fixed-point arithment unless floating point is absolutely needed.
In our case we defined each element of the matrix as an 8-bit (signed) number. Multiplying two 8-bit numbers results in a
16-bit result, and a further addition means due to the carry bit, the result of each index is now 17-bits.
However, we insist on storing this into a 8-bit vector again!
How is this possible? It is not, without a loss of either precision or range.
Imagine our two inputs to be an 8-bit number but the decimal point at the 4-bit mark i.e. a 4-bit number with 4 fractional bits.
In this case our result of 8-bit can be considered a full 8-bit number but with zero fractional bits.
However, if we consider our initial inputs to be full 8-bit integers then, to store our final result into 8-bits means we
need to either truncate it, or quantize it by dropping the lower or upper bits respectively.
As this is a theoretical exercise, we wont worry about it too much, but the representation of numbers is quite important in general.

But this is pretty basic VHDL, can we further compact it using loops?

    :::vhdl
    for i in 0 to 1 loop
        for j in 0 to 1 loop
            out_matrix(i)(j) <= std_logic_vector(
                                         signed(in_matrix1(i)(j)) * signed(in_matrix2(j)(i)) +
                                         signed(in_matrix1(i)(j)) * signed(in_matrix2(j)(i)));
         end loop;
    end loop;

That looks quite a bit compacted! Less chances for typos and errors, once you get it right.
The hardware synthesis tool will unroll it into the initial version though in order to try and optimize it.

Here is the full code for the multiplier.

### Entity and Architecture

    :::vhdl
    -- ---------------------------------------------------------------------------------------------------------------------------------
    -- Name: mult_2x2
    -- Purpose: This is a matrix multiplier for 2 2x2 arrays of 8-bit signed numbers
    -- ---------------------------------------------------------------------------------------------------------------------------------

    library ieee;
    use ieee.std_logic_1164.all;
    use ieee.numeric_std.all;

    library work;
    use work.mult_2x2_pack.all;

    entity mult_2x2 is
        port (
            in_matrix1 : in  t_2d_array;
            in_matrix2 : in  t_2d_array;
            out_matrix : out t_2d_array
            );
    end mult_2x2;

    architecture rtl of mult_2x2 is

    begin

       for i in 0 to 1 loop
           for j in 0 to 1 loop
               out_matrix(i)(j) <= std_logic_vector(
                                         signed(in_matrix1(i)(j)) * signed(in_matrix2(j)(i)) +
                                         signed(in_matrix1(i)(j)) * signed(in_matrix2(j)(i)));
           end loop;
       end loop;

    end rtl;

### Package

And here is the code for the `mult_2x2_pack.vhd` file:

    :::vhdl
    -- ---------------------------------------------------------------------------------------------------------------------------------
    -- Name: mult_2x2_pack
    -- Purpose: Package contains data structures used to hold a 2x2 matrix
    -- ---------------------------------------------------------------------------------------------------------------------------------
    library ieee;
    use ieee.std_logic_1164.all;
    use ieee.numeric_std.all;

    package mult_2x2_pack is

       type t_1d_array is array(integer range 0 to 1) of std_logic_vector(7 downto 0);
       type t_2d_array is array(integer range 0 to 1) of t_1d_array;

    end  mult_2x2_pack;

### Testbench

Further more, here is a very rudimentary testbench:

    :::vhdl
    -- ---------------------------------------------------------------------------------------------------------------------------------
    -- Name: mult_2x2_tb
    -- Purpose: Testbench for a 2x2 combinatorial matrix multiplier
    -- ---------------------------------------------------------------------------------------------------------------------------------
    library ieee;
    use ieee.std_logic_1164.all;
    use ieee.numeric_std.all;
    
    library work;
    use work.mult_2x2_pack.all;
    
    entity mult_2x2_tb is
    end mult_2x2_tb;
    
    architecture tb of mult_2x2_tb is
    
       signal a : t_2d_array;
       signal b : t_2d_array;
    
    begin
    
       process
       begin
          wait for 10 ns;
          a <= ((std_logic_vector(to_signed(3,8)),std_logic_vector(to_signed(3,8))),
                (std_logic_vector(to_signed(3,8)),std_logic_vector(to_signed(3,8))));
          b <= ((std_logic_vector(to_signed(1,8)),std_logic_vector(to_signed(0,8))),
                (std_logic_vector(to_signed(0,8)),std_logic_vector(to_signed(1,8))));
          wait for 10 ns;
          assert FALSE report "end of test vectors" severity error;
       end process;
    
    end tb;
    

