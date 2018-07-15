#!/usr/bin/perl
#
open(TMP, $ARGV[0]) || die "cant open";
@raw= <TMP>;
close TMP;

$index=0;

while($in = <STDIN>)
{

	@word_tag = split(/ /,$in);
	$utf_in = $raw[$index];
	chomp($utf_in);
	@utf_word = split(/ /,$utf_in);
	
	for($j=0; $j<=$#utf_word; $j++)
	{
		my($my_attr);

		my($word,$tag_attr) = split(/\\/,$word_tag[$j]);	
		($tag,@attr) = split(/\./,$tag_attr);	
		print $j+1,"\t",$utf_word[$j],"\t",$tag;

		for($i=0; $i<=$#attr; $i++)
		{
			$my_attr .=$attr[$i].".";
		}
			$my_attr =~ s/.$//;
 		print "\t$my_attr\n";
	}
	$index++;
	print "\n";	
}
		
		
	
