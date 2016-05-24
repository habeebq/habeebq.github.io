Title: Continous Integration for ASIC Design
Date: 2016-04-17
Category: CI
Authors: habeebq

Software development these days is taking a lot of advantage of working in a continous flow. There are a lot of buzzwords going around like *continuous integration*, *continuous deployment*, *continuous delivery*.

These terms make a lot of sense for fast moving software designs, but do they make sense for the slow lugged ASIC design process?

Lets talk a bit about continous integration first.

Here is what is really recommended for CI and what are the benefits to be reaped off it.

Good practices are:

- Commit frequently: To a central repository (atleast daily or more if possible)
- Build automatically
- Self-test the Build
- Build fast: Have a lean and fast build time
- Test in a clean environment
- Dont check in broken or untested code
- Version control all test scripts, config files, CI scripts

This allows you to:

- Avoid large integrations, and trying to sort out the merge clutter
- Build automatically as often as possible, and find failures, instead of spending time manually running tests
- Less tracking to see what went wrong
- Gives you more confidence, as your tools will catch problems
- No more waiting, and more focus on actual coding and designing

Now lets talk about how each of these practices apply to an ASIC Design flow.

### Commit Frequently ###
ASIC Designers tend to be a bit slower when commiting especially if the mainline is building ok, they would think twice before commiting.
When using a software flow, it is easy to use `feature flags` and other `disable flags` to make sure the code does not run.
In hardware however, since all the processes are concurrent, they are all running at the same time. Whilst it may be possible to gate
some features with configuration constants, it is certainly be harder than software. There are more things to worry about
like signal or interface connections, and vector/array size mismatches. This is why it requires more validation before the code can be checked in.

There are methodologies that can be used however so this doesnt remain a problem anymore.
If two features are being developed simultaneously or even one feature is being developed, it best to do it in a separate
branch where you can enable it, without disrupting the mainline but also make check-ins to the mainline to make sure it integrates
but the feature remains disabled.

A lot of times (in VHDL) we would use configuration constants and generics to remove instances completely, or gate processes/registers/signals.

Many of the tools behave differently (by virtue of purpose), and for e.g. synthesis tools would optimize the hardware away if they are gated off,
this means they are not tested at all. For this reason we want a separate branch where we can enable the features and thus actually run
the hardware through the tools to see any problems.

### Build automatically ###
ASIC designers do not have sophisticated build tools like Gradle or Ant. Instead our tools are very vendor specific and this causes some issues to
automate the builds in a vendor-agnostic way.

Also in terms of builds, we want to decide what we would like to automate:
- The level (top-level, block level)
- The tests (self-tests, basic tests, acceptance tests, UVM tests)
- Synthesis tests (check STA, Area)
- Syntax and linting (simulation compile, code linting)

There can be a lot of things to run at various levels and the policy needs to decide what needs to be included in the build.
Alternatively you can have multiple builds running in parallel making different checks. (or the same build multiprocessing)

### Self-test the Build ###

Functional testing of the build can be divided in a number of ways. In ASIC design we usually have module level testbenches,
which we can run faster than system level tests.

One strategy could be to kick of all module level and top level tests in parallel, and see which fails first.

Running tests at top level can be however quite slow, and you may need to decide on the frequency at which you run them. For e.g.
maybe run the shorter tests (designed to cover more features) on every check-in but run longer tests once every few hours.

### Build Fast ###

This can be one of the major bottlenecks in using CI effectively in ASIC design. The build turnaround time is just too high for it
to detect a failure fast enough, and let the team know so they can fix it before commiting any more new code.

Simply `compiling-for-simulation` can take anywhere between 5 minutes to an hour on larger projects. How could you test such a large system.
And while its possible to break certain operations into smaller parts, sometimes your integration builds just require a top-down operation for e.g.
you may want to run system level synthesis in one go (as opposed to breaking it down into smaller libraries).

There are a number of things we can do to alleviate it, but we have to accept that some kinds of builds are just impossible to run within a reasonable
timeframe.

- Break down testing into module level tests
- Run as much as you can in parallel
- Write better tests to ensure 90% of the integration/features is covered with a smaller testset
- Reduce file i/o (reduce logging, use buffered output)
- Turn off debug features, or high effort on the tools
- Focus on bottlenecks, find out what is taking the longest
- Break down the builds into smaller builds (for e.g. each running a different tool). Some CI tools allow you to build a pipeline this way.
- Run on more powerful machines, faster storage
- Fail fast, fail as soon as something is wrong instead of running all the way through
- Tune the workspace, dont check-out files that your build does not require, maybe keep static files or tests somewhere
- Use the fastest tools that give you the result you need (for e.g. does VCS run faster on your code or INCISIVE?)
- Tuning the tools settings to minimize access scope can improve runtime speed (for e.g. if you do not need to look at signals)
- Profile the RTL code, occasionally we have seen unneeded file handles open, or processes running too many times generating delta cycles
- Turn off unnecessary file i/o from RTL tests like ensuring waves are not on, or only writing CRCs to file instead of full data transactions
- Synthesize in blocks in a bottom-up approach allows you to fail fast


### Test in a clean environment ###

It is important to test the build in a clean workspace in case there are remnants of the previous build that cause issues.
Having a dedicated VCS build server is useful, in order to handle the load of builds, and not slow down interactive VCS people are using.

### Dont check in broken or untested code ###

This should be avoided, otherwise your builds will simply be wasting CPU cycles. It is not expected that all the tests are run (that is the job of 
CI), but some basic testing should have been done, so that the builds can go on.

### Version control all test scripts, config files, CI scripts ###

This is something I like to do. Make sure all the scripts are self-contained in the version control system. Some CI tools dont easily support version controlling
their job configs, but I think that should be the way forward. I also prefer to decouple the test scripts from the CI tool, and try to keep it agnostic
so they can be ported to another tool (or another instance) if required. Having the job configs in VCS is also very useful to know why a job failed due
to a config change (and what the person was trying to do when he changed it). Track everything.
