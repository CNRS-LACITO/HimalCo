use strict;
use warnings;

use utf8;

my $variable1 = "bonjour";
my $variable2 = substr($variable1,1,4);
print $variable2."\n";

if ($variable2 !~  /on/) 
	{
		print "oui \n";
	}