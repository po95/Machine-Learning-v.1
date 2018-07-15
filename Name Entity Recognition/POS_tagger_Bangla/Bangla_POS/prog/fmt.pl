#!/usr/bin/perl
#
=c
open(TMP, $ARGV[0]) || die "cant open";
@raw= <TMP>;
close TMP;
=cut
while($in = <STDIN>)
{
	chomp($in);
	if($in =~ /^$/)
	{
		print "\n";
	}
	else
	{
		($wrd,@entry) = split(/\t/,$in);
		$tag = $entry[$#entry];
		print $wrd,"\\",$tag," ";
	}

}
		
		
	
