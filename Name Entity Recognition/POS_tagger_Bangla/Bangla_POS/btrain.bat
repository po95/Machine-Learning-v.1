perl prog\convert.pl %1 data\mapping_utf_itr >data\train.data1
perl prog\process_input.pl <data\train.data1 >data\train.data2
perl prog\fr_for_tr.pl <data\train.data2 >data\train.data
..\crf_learn -c 4.0 template data\train.data model
del data\train.data1 data\train.data2 data\train.data