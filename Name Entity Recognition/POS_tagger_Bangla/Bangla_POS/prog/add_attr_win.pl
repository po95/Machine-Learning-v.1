#!/usr/bin/perl

my(%default_hash);

$default_hash{"NC"} =".0.0.n.n";
$default_hash{"NP"} =".0.0.n.n";
$default_hash{"NV"} =".0.n.n";
$default_hash{"NST"} =".0.n.n";
$default_hash{"VM"} =".3.prs.sim.dcl.fin.n.n.n";
$default_hash{"VAUX"} =".3.prs.sim.dcl.fin.n.n.n";
$default_hash{"PPR"} =".0.3.0.n.n.n.n";
$default_hash{"PRF"} =".0.0.n.n";
$default_hash{"PRC"} =".0.n";
$default_hash{"PRL"} =".0.3.n.n.n.n";
$default_hash{"PWH"} =".0.3.n.n.n.n";
$default_hash{"JJ"} =".n.n";
$default_hash{"JQ"} =".n.n.nnm";
$default_hash{"DAB"} =".0.n";
$default_hash{"DRL"} =".0.n";
$default_hash{"DWH"} =".0.n";
$default_hash{"AMN"} =".0.n.n";
$default_hash{"ALC"} =".0.n.n";
$default_hash{"LV"} =".n";
$default_hash{"LC"} =".n.0";
$default_hash{"PP"} =".0.n";
$default_hash{"CSB"} =".n";
$default_hash{"CCL"} =".n";
$default_hash{"CX"} =".n";

open(TMP, $ARGV[0]) || die "cant open";
while(<TMP>)
{
  chomp($_);
  ($word, $analysis) = split(/\t+/,$_);
  $morph{$word} = $analysis;
}
close TMP;

=c
open(TMP, "<:encoding(utf8)", $ARGV[1]) || die "cant open";
@utf_in = <TMP>;
close TMP;
=cut

#open(OUT,$ARGV[1]) || die "cant open";

#use GDBM_File;
#dbmopen(%morph, $ARGV[0], 0666) || die "cant open";

while($in = <STDIN>)
{

  chomp($in);
  $in =~ s/^\s+//;
#  print OUT $in,"***\n";
  $in =~ s/\s+$//;
#  print OUT $in,"***\n";
  
  @token = split(/\s+/, $in);
 
#  print OUT $#utf_token,"\t",$#token,"\n";

  for($i=0; $i<=$#token; $i++)
  {
    
    ($word, $op_tag) = split(/\\/, $token[$i]);
   # print "@@@@",$word,"@@@@@@\n";
    
    if( $word ne '')
    {      
      $attr = $morph{$word};

	#print "#######",$attr,"######\n";     
      @att_val = &prune_on_tag($op_tag,$attr);
     
#	print "\n\n*********@att_val********\n\n"; 
      if($att_val[0] eq '')
      {
        print $word,"\\",$op_tag;
        print $default_hash{$op_tag};

#	($word_u,$tag_u) = split(/\\/,$utf_token[$i]);
#        
#        $utf_tag = $word_u."\\".$op_tag.$default_hash{$op_tag};
#	#$utf_tag = $utf_token[$i]."\\".$op_tag.$default_hash{$op_tag};
#        push(@utf_sen, $utf_tag);
      
      }
      else
      {
        $tmp = "";
        print $word,"\\",$op_tag;
=c
	($word_u,$tag_u) = split(/\\/,$utf_token[$i]);
        $tmp .= $word_u."\\".$op_tag;
	#$tmp .= $utf_token[$i]."\\".$op_tag;
=cut

        for($j=0; $j<=$#att_val; $j++)
        {
          print "\.$att_val[$j]";
    #      $tmp .= "\.$att_val[$j]";
        }
    #    push(@utf_sen, $tmp);

      }
      print " ";
    }
  }
  
  print "\n";
  print OUT "@utf_sen","\n";
  $my_no++;
}

sub prune_on_tag
{
  ($tag, $attr) = @_;
  @attr = split(/#/,$attr);
  for($k=0; $k<=$#attr; $k++)
  {
    ($root,$cat, @val) = split(/,/,$attr[$k]);
    if( $tag eq $cat)
    {
      return @val;
      last;
    }  
  }
}
