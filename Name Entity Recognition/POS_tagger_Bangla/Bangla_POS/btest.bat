perl prog\convert.pl %1 data\mapping_utf_itr >input.itr

perl prog\feature_select1.pl <input.itr >input.crf

..\crf_test -m model input.crf >out.crf

perl prog\fmt.pl <out.crf >output_itr

perl prog\add_attr_win.pl data\Morph_modi.txt <output_itr >output_attr

perl prog\fmt_op.pl %1 <output_attr >pos_op

del input.itr input.crf out.crf output_attr output_itr