# -*- encoding: UTF-8 -*-
r"""
# Szekler-Hungarian Rovásírás (Old Hungarian, ISO 15924: Hung)
__numbertext__
1:(.*):(.*) \1
2:(.*):(.*) \1\1
3:(.*):(.*) \1\1\1
4:(.*):(.*) \1\1\1\1
5:(.*):(.*) \2
6:(.*):(.*) \2\1
7:(.*):(.*) \2\1\1
8:(.*):(.*) \2\1\1\1
9:(.*):(.*) \2\1\1\1\1

(\d) $(\1:𐳺:𐳻)
(\d)(\d) $(\1:𐳼:𐳽)$2
1(\d\d) 𐳾$1
(\d)(\d\d) $1𐳾$2
1(\d\d\d)$ 𐳿$1
(\d{1,3})(\d\d\d) $1𐳿$2
1(\d{6})$ 𐳿𐳿$1
(\d{1,3})(\d{6}) $1𐳿𐳿$2
1(\d{9})$ 𐳿𐳿𐳿$1
(\d{1,3})(\d{9}) $1𐳿𐳿𐳿$2
"""
from __future__ import unicode_literals
