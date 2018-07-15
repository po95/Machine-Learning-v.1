#!/usr/bin/perl


while($in = <STDIN>)
{
	chomp($in);

	@word_tag = split(/ /,$in);
		my($cur_word, $cur_tag,$pre1_word, $pre1_tag,$pre2_word, $pre2_tag,$nxt1_word, $nxt1_tag,$nxt2_word, $nxt2_tag);
	for($i=0; $i<=$#word_tag; $i++)
	{
		my(@char,$cur_word, $cur_tag,$pre1_word, $pre1_tag,$pre2_word, $pre2_tag,$nxt1_word, $nxt1_tag,$nxt2_word, $nxt2_tag);

		($cur_word, $cur_tag) = split(/\\/,$word_tag[$i]);
		($pre1_word, $pre1_tag) = split(/\\/,$word_tag[$i-1]);
		($pre2_word, $pre2_tag) = split(/\\/,$word_tag[$i-2]);
		($nxt1_word, $nxt1_tag) = split(/\\/,$word_tag[$i+1]);
		($nxt2_word, $nxt2_tag) = split(/\\/,$word_tag[$i+2]);
		if($i == 0) 
		{
			$pre1_word = "NULL";
			$pre2_word = "NULL";
			$pre1_tag = "NULL";
			$pre2_tag = "NULL";
		}
		if($i == 1) 
		{
			$pre2_word = "NULL";
			$pre2_tag = "NULL";
		}


		if($i == $#word_tag) 
		{
			$nxt1_word = "NULL";
			$nxt2_word = "NULL";
			$nxt1_tag = "NULL";
			$nxt2_tag = "NULL";
		}
		if($i == $#word_tag-1) 
		{
			$nxt2_word = "NULL";
			$nxt2_tag = "NULL";
		}
		@char ='';
		my(@char) = split(//,$cur_word);

		if($char[0] ne '')
		{
			$pre1=$char[0];
		}
		else
		{
			$pre1 = "NULL";
		}
		if($char[1] ne '')
		{
			$pre2=$char[0].$char[1];
		}
		else
		{
			$pre2 = "NULL";
		}
		if($char[2] ne '')
		{
			$pre3=$char[0].$char[1].$char[2];
		}
		else
		{
			$pre3 = "NULL";
		}
		if($char[3] ne '')
		{
			$pre4=$char[0].$char[1].$char[2].$char[3];
		}
		else
		{
			$pre4 = "NULL";
		}
		if($char[4] ne '')
		{
			$pre5=$char[0].$char[1].$char[2].$char[3].$char[4];
		}
		else
		{
			$pre5 = "NULL";
		}
		if($char[5] ne '')
		{
			$pre6=$char[0].$char[1].$char[2].$char[3].$char[4].$char[5];
		}
		else
		{
			$pre6 = "NULL";
		}
		if($#char >= 0)
		{
			$suf1=$char[$#char];
		}
		else
		{
			$suf1 = "NULL";
		}
		if($#char-1 >= 0)
		{
			$suf2=$char[$#char-1].$char[$#char];
		}
		else
		{
			$suf2 = "NULL";
		}
		if($#char-2 >= 0)
		{
			$suf3=$char[$#char-2].$char[$#char-1].$char[$#char];
		}
		else
		{
			$suf3 = "NULL";
		}
		if($#char-3 >= 0)
		{
			$suf4=$char[$#char-3].$char[$#char-2].$char[$#char-1].$char[$#char];
		}
		else
		{
			$suf4 = "NULL";
		}
		if($#char-4 >= 0)
		{
			$suf5=$char[$#char-4].$char[$#char-3].$char[$#char-2].$char[$#char-1].$char[$#char];
		}
		else
		{
			$suf5 = "NULL";
		}
		if($#char-5 >= 0)
		{
			$suf6=$char[$#char-5].$char[$#char-4].$char[$#char-3].$char[$#char-2].$char[$#char-1].$char[$#char];
		}
		else
		{
			$suf6 = "NULL";
		}

			print $cur_word," ",$pre1," ",$pre2," ",$pre3," ",$pre4," ",$suf1," ",$suf2," ",$suf3," ",$suf4," \n";

}
print "\n";
}

