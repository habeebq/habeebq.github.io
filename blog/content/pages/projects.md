Title: Projects
Date: 2015-10-12


### Video compression
Implementation of parts of codecs.

* `H264` Lossless mode
* `H264` 10-bit modes
* `VP8` bitstream parsing
* `HEVC` bitstream parsing
* `VP9` bitstream parsing
* Performance analysis of a video decoder - Identifying Bandwidth, Bitrate throttling

### Digital Design
* Digital design for ASICs on low power profiles
* Designs proven on production-level devices

### EDA Projects / Video compression work

##### FRC - Frame Rate Conversion, upscaling the frame rate in the display pipeline
As a rookie, on my first project I worked on the RTL design and debug of Motion Interpolation block and the debug of the Frame Analysis block.
I'll admit at this point I had no idea what I was doing, so I am grateful to our accomplished architect who pretty much spelled everything out in the specifications!
I learnt to use Cadence NCSIM for simulation, Synopsys Design Compiler for synthesis.
This was a major learning and exploratory phase for me as I learnt how and where to look for help!

##### VP6 Boolcoder
This is the arithmetic decode part of the codec. The main challenge in this block was the placement of registers to achieve timing closure.
I worked on the RTL design, functional verification, synthesis, and linting of the block.
This was a fairly small project, but I started getting accustomed to more complex test methods.

##### Decoder Performance Metrics
This has been more or less an ongoing project, and has undergone various modifications over time. The main intention of this has been to be able to count various metrics in the decoder, and extract them while running on an emulator or FPGA.
At times the finicky Perl script has been the `bane` of my existence and I am hoping to re-write and restructure it in Python one of these days. I've done most of the groundwork, now just need to allocate some time to automate the performance testing!

##### VP8 Bitstream Parser
I was responsible for the specification, design, testing and delivery of the VP8 Bitstream parser. After the design, I had to go back to improve performance and optimize the parser in order to achieve 50 Mbps at an operating frequency of 150 MHz.
The tree structure decoding was quite interesting (and limiting for static timing). I kept the code pretty tidy though. I occasionally go back and look at the code to make me feel better when I feel sad.

##### H264 Lossless Mode implementation
This feature implementation required the modification of many existing modules in order to enable lossless mode. I had to update the specifications, and the RTL code. This also involved a lot of system level debug as I was the only person working on this feature.

Since it spanned so many blocks and involved some control loops, it was quite fun to do, and I probably used too many coding styles while destroying some previous ones.

The real learning point though was about project planning, forecasting, and tracking as I realized how I should have looked at the dependencies of tasks and resources.

##### H264 High Profile implementation
The profile we were targetting was 10-bit, 444 chroma format.
This was a major feature for the decoder and required both high level design changes and very detailed and delicate design changes as it touched every datapath in the decoder.
It was more of a `painstaking` project than interesting one, although there were certainly some interesting bugs and debugs.

I worked as a team on various parts including CAVLC, inverse quantisation, inverse transform among other parts.

A large part of this project was system level testing as it was a significant change. I also worked on performance measurements and gate level simulation.

##### HEVC Decoder and a new architecture
This project required a major architecture change of the full decoder as well as adding the `HEVC` codec. This architecture is scalable and allowed multiple decoder pipelines to achieve higher bitrates or frame rates.
We also switched to `28nm` technologies from 40nm and the target frequency became 400 MHz from 150 MHz. This was a very big project and my involvement was in a large number of areas in this project.
I designed and developed the `HEVC` Bitstream Parser. (Specification, RTL Code, Functional Verification, Feature Coverage, Gate-level simulation, Performance analysis).

I took ownership of the Entropy Pipe, which included integration of certain blocks besides the HEVC bitstream parser. At the RTL level, this meant working with clock gating, integration, interfacing, monitoring and debug code.

By this point, due to my position in the team, I took active interest in pretty much everything.
I was also heavily involved in system level debug, and blocks I was not directly responsible for. I took active part in the integration of all the blocks to ensure that the system worked as a whole.

I was involved in firmware and driver debug and dealt with interacting code. That was quite fun. I guess at this point I was pretty much at ease with debugging anything in the system.

I re-designed the system cross-bars, as we were seeing issues when switching from a single crossbar to multiple hierarchies of crossbars. I identified heavily trafficked paths, and separated buses, in order to reduce stalling on interfaces and ensure a smooth decode path. This also reduced and fixed a large number of race condition issues.

##### HEVC Hi Profile Decoder
There were a number of projects that involved adding more features from the HEVC specification in order to support other chroma formats and other features that the HEVC higher profiles support.
There were also a number of projects that involved some customer-specific work like capturing metrics at various stages in the decode pipeline.
I was involved in the specification, design, and debug of the full system level, and also overseeing what other engineers were implementing (some of this work, I had to take over).
I did similar work as in the previous projects, but also looked at the usage of new tools and their features, and also worked on improving the current workflow.

##### VP9 Decoder
I am currently working on the `VP9` decode pipeline, responsible for the EntropyPipe block that involved multiple modules.

I am responsible for delivering this module, and am overlooking a variable number of engineers (3-4).
I am heavily invovled in all the design decisions, those concerning performance, power and area, while all engineers are responsible for their own blocks.

I am also working on the specification and design of the VP9 Bitstream parser, parameter storage block. 


### Other projects, hobbycraft and hackwork
#### Android development using Basic4Android and Java
* [Cloudpipes](https://cloudpipes.wordpress.com/) Asynchronous file transfer to/from Dropbox. Plugin support, also supports Tasker.
* [Weather4Cast](https://play.google.com/store/apps/details?id=com.maximussoft.simpleweather) Weatherfeed
* [PhoneBackup](https://play.google.com/store/apps/details?id=com.maximussoft.backup) Back up phone logs, messages, call logs to a CSV file. Plugin support, integration into Cloudpipes.
* [Timepiece](https://play.google.com/store/apps/details?id=com.maximussoft.timepiece&hl=en) Random floating clock!
* [PicturePuzzle](https://play.google.com/store/apps/details?id=com.maximussoft.picpuzzle) Interesting way to use a dynamic grid.
* Porting and wrapping various Java libraries into the Basic4Android framework
* Chromecast hackery - creating a remote control
* Android resource floating window (displays CPU/RAM usage)

#### Emacs hacking
I do this to make my workflow easier and better. Nothing major, just using tiny bit of elisp and other packages to help prevent RSI and minimize keystrokes.

My current emacs setup is on github [here](https://github.com/habeebq/dot-emacs).

#### Python
Most of my glue logic.

* LGenerator - Generate android jar libraries
* RGenerator - Generate R files by parsing source
* Code invertor - An angle on literate programming. Generate documentation from source code
* Other scalable DevOps
* Deeper Integration into EDATools for e.g. TCL generation, Trace export etc
* Shell based configuration/workspace manager (csh with aliases that change based on context)

#### Projects incubating in my mind
* termspace - improved shell workspace manager
* repl-i-cant - Fast shell scripting in Python with some templating
