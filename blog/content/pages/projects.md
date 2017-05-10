Title: Projects
Date: 2017-05-03


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
This was a major learning and `exploratory` phase for me as I learnt how and where to look for help!

##### VP6 Boolcoder
This is the arithmetic decode part of the `VP6` codec. The main challenge in this block was the placement of registers to achieve timing closure.
I worked on the RTL design, functional verification, synthesis, and linting of the block.
This was a fairly small project, but I started getting accustomed to more complex test methods.

##### Decoder Performance Metrics
This has been more of an ongoing project, and has undergone various modifications over time. The main intention of this has been to be able to count various metrics in the decoder, and extract them while running on an emulator or FPGA.
At times the finicky Perl script has been the `bane` of my existence and I am hoping to re-write and restructure it in Python one of these days. I've done most of the groundwork, now just need to allocate some time to automate the performance testing!

##### VP8 Bitstream Parser
I was responsible for the specification, design, testing and delivery of the VP8 Bitstream parser. After the design, I had to go back to improve performance and optimize the parser in order to achieve 50 Mbps at an operating frequency of 150 MHz.
The tree structure decoding was quite interesting (and limiting for static timing). I kept the code pretty tidy though. I occasionally go back and look at the code to make me feel better when I feel sad.

##### H264 Lossless Mode implementation
This feature implementation required the modification of many existing modules in order to enable lossless mode. I had to update the specifications, and the RTL code. This also involved a lot of system level debug as I was the only person working on this feature.

Since it spanned so many blocks and involved some control loops, it was quite fun to do, and I probably used too many coding styles while destroying some previous ones.

The real `learning` point though was about project planning, forecasting, and tracking as I realized how I should have looked at the dependencies of tasks and resources.

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

I re-designed the `system cross-bars`, as we were seeing issues when switching from a single crossbar to multiple hierarchies of crossbars. I identified heavily trafficked paths, and separated buses, in order to reduce stalling on interfaces and ensure a smooth decode path. This also reduced and fixed a large number of race condition issues.

##### HEVC Hi Profile Decoder
There were a number of projects that involved adding more features from the HEVC specification in order to support other chroma formats and other features that the HEVC higher profiles support.
There were also a number of projects that involved some customer-specific work.

I was involved in the specification, design, and debug of the full system level, and also overseeing what other engineers were implementing (some of this work, I had to take over).

I did similar work as in the previous projects, but also looked at the usage of new tools and their features, and also worked on improving the current workflow.

##### VP9 Decoder
Eventually this project got canned citing a lack of interest from customers and a lack of possible revenue from video IP. This was a strange decision considering that the decoder team had never run out of customer-driven projects until now.

I was working on the `VP9` decode pipeline, responsible for the EntropyPipe block that involved multiple modules.

I worked on a part called the ParamsManager which was in in-memory buffer manager designed to store and retrieve certain parameters (above/left contexts) required in the VP9 bitstream decode whilst hiding memory latency.
I had some great members in my design team, who produced some very clever ideas to save area/power and increase performance. He brought some nice ideas in order to decode 2 bins/clk and we further developed those ideas.

One of the designers was constantly breaking simulation compile/synthesis and integration in a back and forth manner. I had to spend a lot of time trying to work out what was broken, so I eventually set up a Jenkins job, to track compile, synthesis and run my own static code analyzer to report code health. I really liked
automating this part and being able to see the reports as a trend was great.

Sadly this was the first project I worked on that wasn't completed.

Also quite sad to see the codec developers complete disregard of HW engineers! So much bitstream heavy dependencies, there is nowhere to run!

##### Vision Project: Implementation of a CNN in hardware

I was brought on the initial development of a CNN hardware accelerator. At this stage the project was in its infancy and a lot of feature and product decisions were unclear. 
This was also quite a departure from most of the previous designs I had worked on. The accelerator worked on much wider and deeper datasets and was memory bandwidth limited for how much data it could process in one pass. 
I worked on the back-end functions like buffering, pooling and normalization.
The challenges of designing and architecting these blocks was that there was too many degrees of freedom and to make sure that we could optimize for storage and
throughput in all operating modes was quite difficult. Many a time I took a line of thinking that I had to discard later.

Right after the specification review our whole team was moved permanently to another division.
We handed over our specs to the next team taking over and I would hope some remnants of my spec went into the hardware.

##### Flow Team

Seeing my active interest over the past few years in automation, scripting, methodologies and workflows I was placed into the GPU Flow team.

When I got here, the project's flow work had mostly already been re-done and was mostly brand new and ready to use.
I was expected to do handovers, maintenance and adding new features. 
In addtion to dealing with user tickets, helping them understand the flow, and fix bugs and expectations.

First major job was setting up Spyglass Clock domain crossing flow. I read through the tutorials and documentation and with some back and forth help with Synopsys I managed to implement CDC for the project without being too invasive.

Next was emulator bring up. I had to modify some build scripts and suggest RTL coding style changes to appease the emulator compiler tools. I have more outstanding work I would like to do on this when i have the time.

###### JTAG tests integration

JTAG tests came from the microprocessor team that supply the processor inside the GPU.
The tests were made to run on their testbench, and I had to create an automated way to port their tests to our GPU testbench. This included some minor TB changes, and an algorithm to map the registers to our TB registers whilst still keeping them sane.

######  Name server

We have a regression system that creates a webserver as the primary interface for the user and runs tests in the background.
Occasionally the link to this server (which is dynamically generated) gets lost in the logs or requires a lot of clicks to reach on Jenkins.
The purpose of the name server, was to collect all of the running regressions in one place so a user can see and control all of his regressions.
This is still a work in progress with a lot of scope to become a centralized dashboard or command centre.
I wrote this in Flask/SQL-Alchemy with an SQLite database.

I'm pretty sure using an SQLite database on a network file system was a mistake, and on high traffic days I sometimes see database locking issues.


Other work i was involved in Emulator/RTL TB unification, performance telemetry, ATPG, Certitude debug, Spyglass waiver TCL comment stripper. 


##### Other interesting EDA related projects?
I have a lot of ideas incubating in my mind to improve EDA design or debug flow, but never really the time to get those to fruiton.

There are some interesting scripts I am working on hoping to get some automatic debug ready one day.
Some of them are Python TCL generators to do extract information from simulations, and similarly scripts to extract values from waveforms.


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
