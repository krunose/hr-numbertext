# -*- encoding: UTF-8 -*-
r"""
__numbertext__
^0 零
1 一
2 二
3 三
4 四
5 五
6 六
7 七
8 八
9 九
1(\d) 十$1
(\d)(\d) $1十$2
1(\d\d) 百$1
(\d)(\d\d) $1百$2
1(\d\d\d) 千$1
(\d)(\d\d\d) $1千$2
(\d{1,4})(\d{4}) $1万$2
(\d{1,4})(\d{8}) $1億$2
(\d{1,4})(\d{12}) $1兆$2
(\d{1,4})(\d{16}) $1京$2
(\d{1,4})(\d{20}) $1垓$2
(\d{1,4})(\d{24}) $1秭$2
(\d{1,4})(\d{28}) $1穣$2
(\d{1,4})(\d{32}) $1溝$2
(\d{1,4})(\d{36}) $1澗$2
(\d{1,4})(\d{40}) $1正$2
(\d{1,4})(\d{44}) $1載$2

# negative numbers?

[-−](\d+) 负|$1

# decimals?

"([-−]?\d+)[.,]" "$1・"
"([-−]?\d+[.,]\d*)(\d)" $1||$2

# currency

# unit/subunit singular/plural

JPY 円

"([A-Z]{3}) ([-−]?\d+([.,]\d+)?)" $2$1

"""
from __future__ import unicode_literals
