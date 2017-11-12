#!/bin/bash
mecab lyric.txt -o mecab.txt
cat mecab.txt | egrep -v 'EOS|助動詞|助詞|記号|非自立|サ変|接尾|特殊' | cut -f 1 | sort | uniq -c | sort | awk 'BEGIN{print "id, value"}{print $2", "$1}' > result.csv
