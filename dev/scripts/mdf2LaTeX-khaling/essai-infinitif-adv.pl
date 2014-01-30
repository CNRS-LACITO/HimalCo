	use strict;
use warnings;

use utf8;
 

 	 my $variable = "dfsdf \(ghle\) dd";
	  my $var2 = $variable;
	$variable =~ s/(\(.*\))//;
	$var2 =~ s/.*\((.*)\).*/$1/;
	
	print $variable."\n";
	print $var2;