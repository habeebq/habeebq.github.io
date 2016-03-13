Title: A tale of storage benchmarks
Date: 2015-12-31
Category: Storage
Authors: habeebq

When I received a new SSD I decided to benchmark all of my drives before I connected it to see how it would far and whether anything would change.

I built my PC a number of years ago, based on Sandy Bridge and it has served me pretty well so far. The motherboard is a Gigabyte H67-M-UD2H-B3 which has 2 SATA3 ports and 4 SATA2 ports. The processor is a humble Core i3-2100 chugging along its 65W of coolness. Its not a high profile build but its a very smooth and balanced one.

So the drives that I have are:

| Drive | Capactity | Connection | Other |
| ----- | --------- | ---------- | ----- |
| Samsung EVO 840   | 120GB | SATA-3 | FW: ?? |
| Samsung Spinpoint F3  | 500GB | SATA-3 | |
| Seagate ST350041 | 500GB | SATA-2 | |
| Sandisk SSD Plus | 240 GB | SATA-2| |

##### Few notes before you read through 
- I dont really believe benchmarks are a good indicator for general every performance. However, they can be a good indicator that something has gone wrong, if the benchmarks change after a configuration change. This was the reason I was benchmarking to see if adding an additional drive would change the scores. Spoiler alert: they didnt.
- A note on the Samsung EVO 840 drive. I bought this last christmas to boost the performance of the system. While I did see better boot times, i didnt see enough boost in everyday usage, and later I realized while this drive will do great benchmarks I dont think it really performs as spectacularly as I expected. In fact I now feel the slower Sandisk SSD Plus performs better.

# Programs Used to benchmark

I used [HDTach](http://www.majorgeeks.com/files/details/hdtach.html) in the past, however I couldnt export the results very cleanly.

So I found two other reliable programs.

* [CrystalDiskMark](http://crystalmark.info/software/CrystalDiskMark/index-e.html)
* [HDTune Free edition](http://www.hdtune.com/download.html) There is a free version on their dowloads page, keep your eye peeled

## The first bench

This where I realized the EVO 840 was crapping out, so I had to re-optimized the drive and run the benchmarks again.
In the follownig benchmarks you can see the average transfer speed gonig from 100 Mbps to 300 Mbps.
However, the minimum transfer rate dropped to 1 Mbps, not sure what the implications of that are.

### Before Optimization (FW upgrade)


### After optimization
  
    HD Tune: Samsung SSD 840 EVO 120G Benchmark
    Transfer Rate Minimum : 1.0 MB/sec
    Transfer Rate Maximum : 449.1 MB/sec
    Transfer Rate Average : 308.1 MB/sec
    Access Time           : 0.4 ms
    Burst Rate            : 196.7 MB/sec
    CPU Usage             : 27.2%

    CrystalDiskMark 5.1.0 x64 (C) 2007-2015 hiyohiyo
    Sequential Read (Q= 32,T= 1)   :   554.872 MB/s
    Sequential Write (Q= 32,T= 1)  :   500.100 MB/s
    Random Read 4KiB (Q= 32,T= 1)  :   281.610 MB/s [ 68752.4 IOPS]
    Random Write 4KiB (Q= 32,T= 1) :   237.549 MB/s [ 57995.4 IOPS]
    Sequential Read (T= 1)         :   532.327 MB/s
    Sequential Write (T= 1)        :   486.142 MB/s
    Random Read 4KiB (Q= 1,T= 1)   :    39.854 MB/s [  9730.0 IOPS]
    Random Write 4KiB (Q= 1,T= 1)  :   106.855 MB/s [ 26087.6 IOPS]

## Benchmarking the other drives

    HD Tune: SAMSUNG HD502HJ Benchmark
    Transfer Rate Minimum : 72.0 MB/sec
    Transfer Rate Maximum : 136.4 MB/sec
    Transfer Rate Average : 113.4 MB/sec
    Access Time           : 13.6 ms
    Burst Rate            : 176.3 MB/sec
    CPU Usage             : 26.4%

    CrystalDiskMark 5.1.0 x64 
    Sequential Read (Q= 32,T= 1)   :   123.125 MB/s
    Sequential Write (Q= 32,T= 1)  :   120.259 MB/s
    Random Read 4KiB (Q= 32,T= 1)  :     0.844 MB/s [   206.1 IOPS]
    Random Write 4KiB (Q= 32,T= 1) :     1.000 MB/s [   244.1 IOPS]
    Sequential Read (T= 1)         :   121.431 MB/s
    Sequential Write (T= 1)        :    99.610 MB/s
    Random Read 4KiB (Q= 1,T= 1)   :     0.433 MB/s [   105.7 IOPS]
    Random Write 4KiB (Q= 1,T= 1)  :     0.882 MB/s [   215.3 IOPS]
  
    HD Tune: ST350041ST3500418AS Benchmark
    Transfer Rate Minimum : 66.0 MB/sec
    Transfer Rate Maximum : 123.7 MB/sec
    Transfer Rate Average : 100.0 MB/sec
    Access Time           : 14.2 ms
    Burst Rate            : 134.9 MB/sec
    CPU Usage             : 26.4%

    CrystalDiskMark 5.1.0 x64 (C) 2007-2015 hiyohiyo
    Sequential Read (Q= 32,T= 1)   :   125.418 MB/s
    Sequential Write (Q= 32,T= 1)  :   105.855 MB/s
    Random Read 4KiB (Q= 32,T= 1)  :     1.874 MB/s [   457.5 IOPS]
    Random Write 4KiB (Q= 32,T= 1) :     0.613 MB/s [   149.7 IOPS]
    Sequential Read (T= 1)         :   125.202 MB/s
    Sequential Write (T= 1)        :   122.893 MB/s
    Random Read 4KiB (Q= 1,T= 1)   :     0.681 MB/s [   166.3 IOPS]
    Random Write 4KiB (Q= 1,T= 1)  :     0.623 MB/s [   152.1 IOPS]

    HD Tune: SanDisk SDSSDA240G Benchmark
    Transfer Rate Minimum : 180.2 MB/sec
    Transfer Rate Maximum : 235.4 MB/sec
    Transfer Rate Average : 223.6 MB/sec
    Access Time           : 0.0 ms
    Burst Rate            : 72.8 MB/sec
    CPU Usage             : 1.5%

    CrystalDiskMark 5.1.0 x64 (C) 2007-2015 hiyohiyo
    Sequential Read (Q= 32,T= 1)   :   285.102 MB/s
    Sequential Write (Q= 32,T= 1)  :   223.626 MB/s
    Random Read 4KiB (Q= 32,T= 1)  :   159.216 MB/s [ 38871.1 IOPS]
    Random Write 4KiB (Q= 32,T= 1) :   193.717 MB/s [ 47294.2 IOPS]
    Sequential Read (T= 1)         :   276.234 MB/s
    Sequential Write (T= 1)        :   205.731 MB/s
    Random Read 4KiB (Q= 1,T= 1)   :    22.391 MB/s [  5466.6 IOPS]
    Random Write 4KiB (Q= 1,T= 1)  :    62.000 MB/s [ 15136.7 IOPS]
  
  
###  Running both SSD drives together

I tried to see how benchmarking two SSDs together would affect the speed, and the SATA controller handles them nicely and there are no conflicts, both can reach their peak speeds.

| Metric | SanDisk SDSSDA240G | Samsung 840 EVO 120G  |
| ------ | ------------------ | --------------------- |
| Transfer Rate Minimum | 194.8 MB/sec | 389.2 MB/sec |
| Transfer Rate Maximum | 233.9 MB/sec | 402.9 MB/sec |
| Transfer Rate Average | 232.8 MB/sec | 397.1 MB/sec |
| Access Time           | 0.0 ms       | 0.1 ms       |
| Burst Rate            | 86.2 MB/sec  | 163.3 MB/sec |
| CPU Usage             | 2.8%         | 2.8%         |


### Running all 4 drives!

I ran HD Tune on all drives simultaneously to see if they could possibly saturate the SATA bus and there was a bottleneck somewhere in the controller.
But they ran well :)

| Metric | SanDisk SDSSDA240G | Samsung SSD 840 EVO 120G |SAMSUNG HD502HJ| ST350041ST3500418AS|
| ------ | ------------------ | ------------------------ | ------------- | ------------------ |
| Transfer Rate Minimum | 203.1 MB/sec| 381.5 MB/sec  | 72.0 MB/sec      | 66.0 MB/sec    |
| Transfer Rate Maximum | 235.7 MB/sec| 401.3 MB/sec  | 136.4 MB/sec     | 123.7 MB/sec   |
| Transfer Rate Average | 229.6 MB/sec| 390.0 MB/sec  | 113.5 MB/sec     | 100.0 MB/sec   |
| Access Time           | 0.0 ms      | 0.1 ms        | 13.7 ms          | 14.3 ms        |
| Burst Rate            | 85.9 MB/sec | 162.9 MB/sec  | 162.4 MB/sec     | 130.7 MB/sec   |
| CPU Usage             | 4.0%        | 4.0%          | 3.9%             | 3.8%           |



