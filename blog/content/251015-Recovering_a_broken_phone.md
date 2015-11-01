Title: Recovering a phone with a broken screen
Date: 2015-10-25
Category: Android
Authors: habeebq

I broke the screen of my two-and-a-half year old Galaxy S3. Frustrated by the battery life, and the finicky microusb port, that just wouldnt charge the dying phone, I flung it across the room. I was a bit disappointed to break the screen in a single attempt, I was hoping I would get to bash it a bit more, but while the screen broke completely, the rest of the phone remained alive. It can still charge (oh, the irony) and turn on.

In the moment later, I started to think what useful data can I get from the phone. While its easy enough to copy photos from the phone, and my contacts are all backed up to google, the only other thing I could think of was my FuelIO logs (mileage and fillup reports).

Android 4.0 and later, come with some extra adb commands (backup and restore), that will let you backup and restore a particular apps data, or even the full system.

`adb` is the `Android Debug Bridge`, which is a command-line platform tool provided by google. It is run on the development host i.e. a windows/linux/mac machine, to which the android device is tethered, and you can send commands interactively to the device with this tool. I have used this in the past, and I remembered I was able to navigate the full file system of the phone, however it seems that in later versions there is more security and I cannot access system or data partitions anymore. So I really wondered how am I going to get the app's internal data without full root access to the file system.

A bit of googling, and while I couldnt get full access, I figured out how to get a particular apps data:

	:::
	adb backup -f <filename.ab> <packagename>

Where the `.ab` file is an android backup file (just a glorified tar file). You can get the apps package name from the play store, just search for it, and in the url you will see the package name in the id parameter, something like id=com.kajda.fuelio. So this becomes:

	:::
	adb backup -f fuelio-data.ab com.kajda.fuelio

It does mention that it will display a prompt on the screen where you can enter an encryption password, but luckily for me it didnt and it just went through. I'm not sure if it is because I had USB Debugging enabled by default. Once you have the backup file, plug in your other phone, install the app, and restore it by:

	:::
	adb restore fuelio-data.ab

Here it will prompt you on the phone if you do want to restore. Now when you open the app, you should see all the new data there.

In the meantime just-in-case, I'd do a full backup of the phone to make sure I have anything I might need later.

What if you want to check whether the backup does contain any files or not? Well, we need to convert the `ab` file into a `tar` file. There may be other methods, but I used this particular tool `abe` aka `android-backup-extractor`. After that even 7-zip can read `tar` files so you should be able to verify the contents.

For reference here are some useful links:

-   [Guide to adb backup](http://forum.xda-developers.com/google-nexus-5/general/guide-backup-data-root-t2824790)
-   [Information on the Android backup format and tools to backup/restore](http://android.stackexchange.com/questions/28481/how-do-you-extract-an-apps-data-from-a-full-backup-made-through-adb-backup)
-   [GUIDE on How to extract, create or edit android adb backups](http://forum.xda-developers.com/showthread.php?t=2011811)
-   [Backing up and restoring all app data](http://www.less-broken.com/blog/2012/04/transferring-apps-and-data-from-one.html)

Another thought, if you are in a predicament like me, you can try to use some screen mirroring software, to see what is going on. I'll try DroidExplorer or something like that later.
