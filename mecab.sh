#!/bin/bash
mecab lyric.txt -o mecab.txt
cat  mecab.txt | grep -v EOS | grep -v 助動詞 | grep -v 助詞 | grep -v 記号 | grep -v 非自立 | grep -v サ変 | grep -v 接尾 | grep -v 特殊 | cut -f 1 | sort | uniq -c | sort > result.txt

