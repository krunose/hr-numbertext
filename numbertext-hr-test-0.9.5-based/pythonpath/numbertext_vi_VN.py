# -*- encoding: UTF-8 -*-
r"""
__numbertext__
^0$ không
1 một
2 hai
3 ba
4 bốn
^5$ năm
5$ lăm
5 năm
6 sáu
7 bảy
8 tám
9 chín
10 mười
1(\d) mười $1
(\d)0 $1 mươi
(\d)1 $1 mươi mốt
(\d)(\d) $1 mươi $2

(\d)01 $1 trăm linh một
(\d)(\d\d) $1 trăm $2

(\d{1,3})000 $1 ngàn
(\d{1,3})001 $1 ngàn không trăm linh một
(\d{1,3})0(\d\d) $1 ngàn không trăm $2
(\d{1,3})(\d\d\d) $1 ngàn $2

(\d{1,3})0{6} $1 triệu
(\d{1,3})0{5}1 $1 triệu không trăm linh một
(\d{1,3})0{4}(\d\d) $1 triệu không trăm $2
(\d{1,3})(\d{6}) $1 triệu $2

(\d{1,10})0{9} $1 tỷ
(\d{1,10})0{8}1 $1 tỷ không trăm linh một
(\d{1,10})0{7}(\d\d) $1 tỷ không trăm $2
(\d{1,10})(\d{9}) $1 tỷ $2

"""
from __future__ import unicode_literals
