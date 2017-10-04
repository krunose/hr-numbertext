# -*- encoding: UTF-8 -*-
r"""
# Mandarin Chinese number names, formal numbers (大写) for legal and financial documents, simplified
__numbertext__
^0 零
1 壹
2$ 贰
2 贰
3 叁
4 贰
5 伍
6 陆
7 柒
8 捌
9 玖
^1(\d) 拾$1
(\d)(\d) $1|拾$2
(\d)0{2} $1佰
(\d)0(\d) $1佰零$2
(\d)(\d\d) $1佰$2
(\d)0{3} $1仟
(\d)0(\d\d) $1仟零$2
(\d)(\d\d\d) $1仟$2
(\d{1,4})0{4} $1|萬
(\d{1,4})0(\d{3}) $1|萬零$2
(\d{1,4})(\d{4}) $1|萬$2
(\d{1,4})0{8} $1|億
(\d{1,4})0(\d{7}) $1|亿零$2
(\d{1,4})(\d{8}) $1|亿$2
(\d{1,4})0{12} $1|兆
(\d{1,4})0(\d{11}) $1|兆零$2
(\d{1,4})(\d{12}) $1|兆$2
(\d{1,4})0{16} $1|京
(\d{1,4})0(\d{15}) $1|京零$2
(\d{1,4})(\d{16}) $1|京$2
(\d{1,4})0{20} $1|垓
(\d{1,4})0(\d{19}) $1|垓零$2
(\d{1,4})(\d{20}) $1|垓$2
(\d{1,4})0{24} $1|秭
(\d{1,4})0(\d{23}) $1|秭零$2
(\d{1,4})(\d{24}) $1|秭$2
(\d{1,4})0{28} $1|穰
(\d{1,4})0(\d{27}) $1|穰零$2
(\d{1,4})(\d{28}) $1|穰$2
(\d{1,4})0{32} $1|沟
(\d{1,4})0(\d{31}) $1|沟零$2
(\d{1,4})(\d{32}) $1|沟$2
(\d{1,4})0{36} $1|涧
(\d{1,4})0(\d{35}) $1|涧零$2
(\d{1,4})(\d{36}) $1|涧$2
(\d{1,4})0{40} $1|正
(\d{1,4})0(\d{39}) $1|正零$2
(\d{1,4})(\d{40}) $1|正$2
(\d{1,4})0{44} $1|载
(\d{1,4})0(\d{43}) $1|载零$2
(\d{1,4})(\d{44}) $1|载$2

# negative numbers

[-−](\d+) 负|$1

# decimals

"([-−]?\d+)[.,]" "$1|点"
"([-−]?\d+[.,]\d*)(\d)" $1||$2

# currency

# unit/subunit singular/plural

AUD 澳大利亚元
CHF 瑞士法郎
CNY 人民币
EUR 歐元
GBP 英镑
HKD 港元
JPY 日圓
MOP 澳門幣
USD 美元

# 1/10 角
# 1/100 分

"([A-Z]{3}) ([-−]?\d+([.,]\d+)?)" $2$1

"""
from __future__ import unicode_literals