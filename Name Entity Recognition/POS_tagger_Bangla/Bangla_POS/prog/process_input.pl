#!/usr/bin/perl

while($in = <STDIN>)
{
  chomp($in);
  
  @token = split(/\s+/,$in);
  
  for($i=0; $i<=$#token; $i++)
  {
    ($wrd, $tag_all) = split(/\\/,$token[$i]);
    @attr = split(/\./, $tag_all);
    $tag = $attr[0];
	$tag =~ s/|$//;

	if( $wrd ne '' && $tag ne '')
	{
    	print $wrd,"\\",$tag," ";
	}
    
  }
  print "\n";
}
