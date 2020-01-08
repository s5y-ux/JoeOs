#!/usr/bin/perl
use warnings;

#Perl script made by pmiccich1 (https://www.youtube.com/user/pmiccich1)
#You are free to use and modify this program in whatever way you wish.

$jarFileName = "craftbukkit.jar"; #Change this value if you wish to use a .jar file with a different name
$minMem = 1024; #Minimum amount of memory your server can run off of in MB (Should be at least 1024)

$break = 0;
while($break == 0)
{
	print "Enter how much memory you want your server to use: "; chomp ($memMax = <>);
	
	if ($memMax < $minMem)
	{
		print "\nYou need to deticate at least 1GB (1024MB) of memory to the server to be able to run it!\n\n";
	}
	
	elsif ($memMax >= $minMem)
	{
		$break = 1;
	}
}
$jstr = "java -Xmx" . $memMax . "M -jar " . $jarFileName . " -o true";

system($jstr);