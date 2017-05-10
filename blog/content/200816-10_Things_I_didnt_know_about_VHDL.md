Title: A few Things I didnt know about VHDL
Date: 2016-08-20
Category: VHDL, Digital Design
Authors: habeebq

I know the title sounds like a Buzzfeed article...and number 7 will blow your mind!

The more I read code, the more I see interesting ways people write code.
Some are good, some are bad, but mostly you come across these because some tool fails
to parse or synthesize the code. Tools are getting better as we report bugs, and vendors
are indeed improving things, but the VHDL LRM certainly allows for a lot of ambiguity.

### 1. Generate statements

This is simple, but a lot of people dont know about generate statements even though they are also present in  Verilog.

There are two main kinds of generate constructs: the if generate, and the for generate.

if-generate statements are greate to rip out unneeded logic based on a feature etc. Dont forget to add the converse generate statement
to assign signals for both cases.

	:::vhdl
	g_generate : if FEATURE = true generate
		inst_A : moduleA (input, output);
	end generate g_generate;

	g_no_generate : if FEATURE = false generate
		output <= input;
	end generate g_no_generate;

for-generate statements are just unrolling loops. They can be used to instantiate a variable (at compile) number of instances
or just to assign signal values over a vector.

	:::vhdl
	g_generate : for i in 0 to 7 generate
		inst_A : moduleA(input(i), output(i));
		a_vector(8*(i+1)-1 downto i) <= b_array(i);
	end generate g_generate;

  
  

### 2. Declarations within Generate statements

You can also declare signals within the scope of a generate statement. This allows them to not even be defined in the case the generate
isnt true.

	:::vhdl
	g_generate_signals : if FEATURE = true generate
		signal feature_option   : std_logic;
		signal feature_option_2 : std_logic;
		begin
			feature_option <= derive_feature(A,B,C);
	end generate g_generate_signals;


### 3. Optional parameters in functions

VHDL functions allo optional parameters. I really wouldnt recommend using this unless it is a straight forward use case because some tools
will definitely choke on this.


### 4. User Defined Attributes

VHDL supports User Defined Attributes as well. They can be useful are preprocessor arguments for Tools to know what to do with particular symbols.
The only place I have come across it is to tell emulator tools how to synthesize certain registers (RAMs or Registers). FPGA tools may use them as well.
Apart from that, I guess you can use them if you want to write your own tool and pass some obscure information to it.

	:::vhdl
	attribute attribute_name: type;                              -- attribute declaration
	attribute attribute_name of item : item_class is expression; -- attribute specification

Example:

	:::vhdl
	attribute signal_desc : String;
	signal the_signal : std_logic_vector(5 dowto 0);
	attribute signal_desc of signal : std_logic_vector is "The description of the signal";

Now you can write your own VHDL analyzer to pass this information to a document generator!

