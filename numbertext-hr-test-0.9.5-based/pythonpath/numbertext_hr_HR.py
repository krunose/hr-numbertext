# -*- encoding: UTF-8 -*-
r"""
#
# Regular number to text transducer for Croatian written in Soros
# Copyright (c) Krunoslav Šebetić <kruno.se@gmx.com> 2017.
#
#
# get newest version of rules from https://www.github.com/krunose/hr-numbertext
#              
# Released under Creative Commons 3.0 Attribution - Share Alike license
# and relicensed under GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Visit http://numbertext.org for more info on Soros language and syntax 
#
# OOo issue 103746: https://bz.apache.org/ooo/show_bug.cgi?id=103746
#


__numbertext__
# (\d+)(([\.][\d]+?)) $(\1\2)
(\d{1,3})[\.](\d{3}) $(\1\2)
(\d{1,3})[\s](\d{3}) $(\1\2)
(\d{1,3})[\.](\d{3}) $(\1\2)
(\d{1,3})[\,](\d{3})[\.](\d{3}) $(\1\2\3)
(\d{1,3})[\s](\d{3})[\s](\d{3}) $(\1\2\3)
(\d{1,3})[\.](\d{3})[\.](\d{3}) $(\1\2\3)
(\d{1,3})[\.](\d{3})[\,](\d{3})[\.](\d{3}) $(\1\2\3\4)
(\d{1,3})[\s](\d{3})[\s](\d{3})[\s](\d{3}) $(\1\2\3\4)
(\d{1,3})[\.](\d{3})[\.](\d{3})[\.](\d{3}) $(\1\2\3\4)
(\d{1,3})[\,](\d{3})[\.](\d{3})[\,](\d{3})[\.](\d{3}) $(\1\2\3\4\5)
(\d{1,3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3}) $(\1\2\3\4\5)
(\d{1,3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3}) $(\1\2\3\4\5)
(\d{1,3})[\.](\d{3})[\,](\d{3})[\.](\d{3})[\,](\d{3})[\.](\d{3}) $(\1\2\3\4\5\6)
(\d{1,3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3}) $(\1\2\3\4\5\6)
(\d{1,3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3}) $(\1\2\3\4\5\6)
(\d{1,3})[\,](\d{3})[\.](\d{3})[\,](\d{3})[\.](\d{3})[\,](\d{3})[\.](\d{3}) $(\1\2\3\4\5\6\7)
(\d{1,3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3}) $(\1\2\3\4\5\6\7)
(\d{1,3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3}) $(\1\2\3\4\5\6\7)
(\d{1,3})[\.](\d{3})[\,](\d{3})[\.](\d{3})[\,](\d{3})[\.](\d{3})[\,](\d{3})[\.](\d{3}) $(\1\2\3\4\5\6\7\8)
(\d{1,3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3}) $(\1\2\3\4\5\6\7\8)
(\d{1,3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3}) $(\1\2\3\4\5\6\7\8)
(\d{1,3})[\,](\d{3})[\.](\d{3})[\,](\d{3})[\.](\d{3})[\,](\d{3})[\.](\d{3})[\,](\d{3})[\.](\d{3}) $(\1\2\3\4\5\6\7\8\9)
(\d{1,3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3}) $(\1\2\3\4\5\6\7\8\9)
(\d{1,3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3}) $(\1\2\3\4\5\6\7\8\9)
(\d{1,3})[\.](\d{3})[\,](\d{3})[\.](\d{3})[\,](\d{3})[\.](\d{3})[\,](\d{3})[\.](\d{3})[\,](\d{3})[\.](\d{3}) $(\1\2\3\4\5\6\7\8\9\10)
(\d{1,3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3}) $(\1\2\3\4\5\6\7\8\9\10)
(\d{1,3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3}) $(\1\2\3\4\5\6\7\8\9\10)
(\d{1,3})[\,](\d{3})[\.](\d{3})[\,](\d{3})[\.](\d{3})[\,](\d{3})[\.](\d{3})[\,](\d{3})[\.](\d{3})[\,](\d{3})[\.](\d{3}) $(\1\2\3\4\5\6\7\8\9\10\11)
(\d{1,3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3}) $(\1\2\3\4\5\6\7\8\9\10\11)
(\d{1,3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3}) $(\1\2\3\4\5\6\7\8\9\10\11)
(\d{1,3})[\.](\d{3})[\,](\d{3})[\.](\d{3})[\,](\d{3})[\.](\d{3})[\,](\d{3})[\.](\d{3})[\,](\d{3})[\.](\d{3})[\,](\d{3})[\.](\d{3}) $(\1\2\3\4\5\6\7\8\9\10\11\12)
(\d{1,3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3}) $(\1\2\3\4\5\6\7\8\9\10\11\12)
(\d{1,3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3}) $(\1\2\3\4\5\6\7\8\9\10\11\12)
(\d{1,3})[\,](\d{3})[\.](\d{3})[\,](\d{3})[\.](\d{3})[\,](\d{3})[\.](\d{3})[\,](\d{3})[\.](\d{3})[\,](\d{3})[\.](\d{3})[\,](\d{3})[\.](\d{3}) $(\1\2\3\4\5\6\7\8\9\10\11\12\13)
(\d{1,3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3}) $(\1\2\3\4\5\6\7\8\9\10\11\12\13)
(\d{1,3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3}) $(\1\2\3\4\5\6\7\8\9\10\11\12\13)
(\d{1,3})[\.](\d{3})[\,](\d{3})[\.](\d{3})[\,](\d{3})[\.](\d{3})[\,](\d{3})[\.](\d{3})[\,](\d{3})[\.](\d{3})[\,](\d{3})[\.](\d{3})[\,](\d{3})[\.](\d{3}) $(\1\2\3\4\5\6\7\8\9\10\11\12\13\14)
(\d{1,3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3}) $(\1\2\3\4\5\6\7\8\9\10\11\12\13\14)
(\d{1,3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3}) $(\1\2\3\4\5\6\7\8\9\10\11\12\13\14)
(\d{1,3})[\,](\d{3})[\.](\d{3})[\,](\d{3})[\.](\d{3})[\,](\d{3})[\.](\d{3})[\,](\d{3})[\.](\d{3})[\,](\d{3})[\.](\d{3})[\,](\d{3})[\.](\d{3})[\,](\d{3})[\.](\d{3}) $(\1\2\3\4\5\6\7\8\9\10\11\12\13\14\15)
(\d{1,3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3}) $(\1\2\3\4\5\6\7\8\9\10\11\12\13\14\15)
(\d{1,3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3}) $(\1\2\3\4\5\6\7\8\9\10\11\12\13\14\15)
(\d{1,3})[\.](\d{3})[\,](\d{3})[\.](\d{3})[\,](\d{3})[\.](\d{3})[\,](\d{3})[\.](\d{3})[\,](\d{3})[\.](\d{3})[\,](\d{3})[\.](\d{3})[\,](\d{3})[\.](\d{3})[\,](\d{3})[\.](\d{3}) $(\1\2\3\4\5\6\7\8\9\10\11\12\13\14\15\16)
(\d{1,3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3}) $(\1\2\3\4\5\6\7\8\9\10\11\12\13\14\15\16)
(\d{1,3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3}) $(\1\2\3\4\5\6\7\8\9\10\11\12\13\14\15\16)
(\d{1,3})[\,](\d{3})[\.](\d{3})[\,](\d{3})[\.](\d{3})[\,](\d{3})[\.](\d{3})[\,](\d{3})[\.](\d{3})[\,](\d{3})[\.](\d{3})[\,](\d{3})[\.](\d{3})[\,](\d{3})[\.](\d{3})[\,](\d{3})[\.](\d{3}) $(\1\2\3\4\5\6\7\8\9\10\11\12\13\14\15\16\17)
(\d{1,3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3}) $(\1\2\3\4\5\6\7\8\9\10\11\12\13\14\15\16\17)
(\d{1,3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3}) $(\1\2\3\4\5\6\7\8\9\10\11\12\13\14\15\16\17)
(\d{1,3})[\.](\d{3})[\,](\d{3})[\.](\d{3})[\,](\d{3})[\.](\d{3})[\,](\d{3})[\.](\d{3})[\,](\d{3})[\.](\d{3})[\,](\d{3})[\.](\d{3})[\,](\d{3})[\.](\d{3})[\,](\d{3})[\.](\d{3})[\,](\d{3})[\.](\d{3}) $(\1\2\3\4\5\6\7\8\9\10\11\12\13\14\15\16\17\18)
(\d{1,3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3}) $(\1\2\3\4\5\6\7\8\9\10\11\12\13\14\15\16\17\18)
(\d{1,3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3}) $(\1\2\3\4\5\6\7\8\9\10\11\12\13\14\15\16\17\18)
(\d{1,3})[\,](\d{3})[\.](\d{3})[\,](\d{3})[\.](\d{3})[\,](\d{3})[\.](\d{3})[\,](\d{3})[\.](\d{3})[\,](\d{3})[\.](\d{3})[\,](\d{3})[\.](\d{3})[\,](\d{3})[\.](\d{3})[\,](\d{3})[\.](\d{3})[\,](\d{3})[\.](\d{3}) $(\1\2\3\4\5\6\7\8\9\10\11\12\13\14\15\16\17\18\19)
(\d{1,3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3}) $(\1\2\3\4\5\6\7\8\9\10\11\12\13\14\15\16\17\18\19)
(\d{1,3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3}) $(\1\2\3\4\5\6\7\8\9\10\11\12\13\14\15\16\17\18\19)
(\d{1,3})[\.](\d{3})[\,](\d{3})[\.](\d{3})[\,](\d{3})[\.](\d{3})[\,](\d{3})[\.](\d{3})[\,](\d{3})[\.](\d{3})[\,](\d{3})[\.](\d{3})[\,](\d{3})[\.](\d{3})[\,](\d{3})[\.](\d{3})[\,](\d{3})[\.](\d{3})[\,](\d{3})[\.](\d{3}) $(\1\2\3\4\5\6\7\8\9\10\11\12\13\14\15\16\17\18\19\20)
(\d{1,3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3}) $(\1\2\3\4\5\6\7\8\9\10\11\12\13\14\15\16\17\18\19\20)
(\d{1,3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3}) $(\1\2\3\4\5\6\7\8\9\10\11\12\13\14\15\16\17\18\19\20)
(\d{1,3})[\,](\d{3})[\.](\d{3})[\,](\d{3})[\.](\d{3})[\,](\d{3})[\.](\d{3})[\,](\d{3})[\.](\d{3})[\,](\d{3})[\.](\d{3})[\,](\d{3})[\.](\d{3})[\,](\d{3})[\.](\d{3})[\,](\d{3})[\.](\d{3})[\,](\d{3})[\.](\d{3})[\,](\d{3})[\.](\d{3}) $(\1\2\3\4\5\6\7\8\9\10\11\12\13\14\15\16\17\18\19\20\21)
(\d{1,3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3}) $(\1\2\3\4\5\6\7\8\9\10\11\12\13\14\15\16\17\18\19\20\21)
(\d{1,3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3}) $(\1\2\3\4\5\6\7\8\9\10\11\12\13\14\15\16\17\18\19\20\21)
(\d{1,3})[\.](\d{3})[\,](\d{3})[\.](\d{3})[\,](\d{3})[\.](\d{3})[\,](\d{3})[\.](\d{3})[\,](\d{3})[\.](\d{3})[\,](\d{3})[\.](\d{3})[\,](\d{3})[\.](\d{3})[\,](\d{3})[\.](\d{3})[\,](\d{3})[\.](\d{3})[\,](\d{3})[\.](\d{3})[\,](\d{3})[\.](\d{3}) $(\1\2\3\4\5\6\7\8\9\10\11\12\13\14\15\16\17\18\19\20\21\22)
(\d{1,3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3}) $(\1\2\3\4\5\6\7\8\9\10\11\12\13\14\15\16\17\18\19\20\21\22)
(\d{1,3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3}) $(\1\2\3\4\5\6\7\8\9\10\11\12\13\14\15\16\17\18\19\20\21\22)
(\d{1,3})[\,](\d{3})[\.](\d{3})[\,](\d{3})[\.](\d{3})[\,](\d{3})[\.](\d{3})[\,](\d{3})[\.](\d{3})[\,](\d{3})[\.](\d{3})[\,](\d{3})[\.](\d{3})[\,](\d{3})[\.](\d{3})[\,](\d{3})[\.](\d{3})[\,](\d{3})[\.](\d{3})[\,](\d{3})[\.](\d{3})[\,](\d{3})[\.](\d{3}) $(\1\2\3\4\5\6\7\8\9\10\11\12\13\14\15\16\17\18\19\20\21\22\23)
(\d{1,3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3}) $(\1\2\3\4\5\6\7\8\9\10\11\12\13\14\15\16\17\18\19\20\21\22\23)
(\d{1,3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3}) $(\1\2\3\4\5\6\7\8\9\10\11\12\13\14\15\16\17\18\19\20\21\22\23)
(\d{1,3})[\.](\d{3})[\,](\d{3})[\.](\d{3})[\,](\d{3})[\.](\d{3})[\,](\d{3})[\.](\d{3})[\,](\d{3})[\.](\d{3})[\,](\d{3})[\.](\d{3})[\,](\d{3})[\.](\d{3})[\,](\d{3})[\.](\d{3})[\,](\d{3})[\.](\d{3})[\,](\d{3})[\.](\d{3})[\,](\d{3})[\.](\d{3})[\,](\d{3})[\.](\d{3}) $(\1\2\3\4\5\6\7\8\9\10\11\12\13\14\15\16\17\18\19\20\21\22\23\24)
(\d{1,3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3}) $(\1\2\3\4\5\6\7\8\9\10\11\12\13\14\15\16\17\18\19\20\21\22\23\24)
(\d{1,3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3}) $(\1\2\3\4\5\6\7\8\9\10\11\12\13\14\15\16\17\18\19\20\21\22\23\24)
(\d{1,3})[\,](\d{3})[\.](\d{3})[\,](\d{3})[\.](\d{3})[\,](\d{3})[\.](\d{3})[\,](\d{3})[\.](\d{3})[\,](\d{3})[\.](\d{3})[\,](\d{3})[\.](\d{3})[\,](\d{3})[\.](\d{3})[\,](\d{3})[\.](\d{3})[\,](\d{3})[\.](\d{3})[\,](\d{3})[\.](\d{3})[\,](\d{3})[\.](\d{3})[\,](\d{3})[\.](\d{3}) $(\1\2\3\4\5\6\7\8\9\10\11\12\13\14\15\16\17\18\19\20\21\22\23\24\25)
(\d{1,3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3}) $(\1\2\3\4\5\6\7\8\9\10\11\12\13\14\15\16\17\18\19\20\21\22\23\24\25)
(\d{1,3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3}) $(\1\2\3\4\5\6\7\8\9\10\11\12\13\14\15\16\17\18\19\20\21\22\23\24\25)
(\d{1,3})[\.](\d{3})[\,](\d{3})[\.](\d{3})[\,](\d{3})[\.](\d{3})[\,](\d{3})[\.](\d{3})[\,](\d{3})[\.](\d{3})[\,](\d{3})[\.](\d{3})[\,](\d{3})[\.](\d{3})[\,](\d{3})[\.](\d{3})[\,](\d{3})[\.](\d{3})[\,](\d{3})[\.](\d{3})[\,](\d{3})[\.](\d{3})[\,](\d{3})[\.](\d{3})[\,](\d{3})[\.](\d{3}) $(\1\2\3\4\5\6\7\8\9\10\11\12\13\14\15\16\17\18\19\20\21\22\23\24\25\26)
(\d{1,3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3}) $(\1\2\3\4\5\6\7\8\9\10\11\12\13\14\15\16\17\18\19\20\21\22\23\24\25\26)
(\d{1,3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3}) $(\1\2\3\4\5\6\7\8\9\10\11\12\13\14\15\16\17\18\19\20\21\22\23\24\25\26)
(\d{1,3})[\,](\d{3})[\.](\d{3})[\,](\d{3})[\.](\d{3})[\,](\d{3})[\.](\d{3})[\,](\d{3})[\.](\d{3})[\,](\d{3})[\.](\d{3})[\,](\d{3})[\.](\d{3})[\,](\d{3})[\.](\d{3})[\,](\d{3})[\.](\d{3})[\,](\d{3})[\.](\d{3})[\,](\d{3})[\.](\d{3})[\,](\d{3})[\.](\d{3})[\,](\d{3})[\.](\d{3})[\,](\d{3})[\.](\d{3}) $(\1\2\3\4\5\6\7\8\9\10\11\12\13\14\15\16\17\18\19\20\21\22\23\24\25\26\27)
(\d{1,3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3})[\s](\d{3}) $(\1\2\3\4\5\6\7\8\9\10\11\12\13\14\15\16\17\18\19\20\21\22\23\24\25\26\27)
(\d{1,3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3})[\.](\d{3}) $(\1\2\3\4\5\6\7\8\9\10\11\12\13\14\15\16\17\18\19\20\21\22\23\24\25\26\27)


## Brojevi

# jednoznamenkasti brojevi

^0 nula
1 jedan
2 dva
3 tri
4 četiri
5 pet
6 šest
7 sedam
8 osam
9 devet


# dvoznamenkasti brojevi

10 deset
11 jedanaest
12 dvanaest
13 trinaest
14 četrnaest
15 petnaes
16 šesnaest
17 sedamnaest
18 osamnaest
19 devetnaest
([2378])0 $1deset
40 četrdeset
50 pedeset
60 šezdeset
90 devedeset
([2378])(\d) $1deset $2
4(\d) četrdeset $1
5(\d) pedeset $1
6(\d) šezdeset $1
9(\d) devedeset $1

# troznamenkasti brojevi

100 sto
200 dvjesto
([34789])00 $1sto
1(\d{2}) sto $1
2(\d{2}) dvjesto $1
([34789])(\d{2}) $1sto $2


# troznamenkasti brojevi

1(\d{2}) sto $1
2(\d{2}) dvjesto $1
([3-57-9])(\d{2}) $1sto $2
6(\d{2}) šesto $1

# tisuću

1(\d{3}) tisuću $1
2(\d{3}) dvije tisuće $1
([34])(\d{3}) $1 tisuće $2
([5-9])(\d{3}) $1 tisuća $2
(1[1-9])(\d{3}) $1 tisuća $2
([1-9]0)(\d{3}) $1 tisuća $2
([2378])1(\d{3}) $1deset jedna tisuća $2
41(\d{3}) četrdeset jedna tisuća $1
51(\d{3}) pedeset jedna tisuća $1
61(\d{3}) šezdeset jedna tisuća $1
91(\d{3}) devedeset jedna tisuća $1
([2378])2(\d{3}) $1deset dvije tisuće $2
42(\d{3}) četrdeset dvije tisuće $2
52(\d{3}) pedeset dvije tisuće $1
62(\d{3}) šezdeset dvije tisuće $1
92(\d{3}) devedeset dvije tisuće $1
([1-9][34])(\d{3}) $1 tisuće $2
([1-9][5-9])(\d{3}) $1 tisuća $2
([1-9]00)(\d{3}) $1 tisuća $2
101(\d{3}) sto jedna tisuća $1
102(\d{3}) sto dvije tisuće $1
201(\d{3}) dvjesto jedna tisuća $1
202(\d{3}) dvjesto dvije tisuće $1
([3-57-9])01(\d{3}) $1sto jedna tisuća $2
([3-57-9])02(\d{3}) $1sto dvije tisuće $2
601(\d{3}) šesto jedna tisuća $1
602(\d{3}) šesto dvije tisuće $1
1(\d{5}) sto $1
2(\d{5}) dvjesto $1
([3-57-9])(\d{5}) $1sto $2
6(\d{5}) šesto $1


# milijun

1(\d{6}) milijun $1
([2-9])(\d{6}) $1 milijuna $2
([1-9]0{1,2})(\d{6}) $1 milijuna $2
([1-9]1)(\d{6}) $1 milijun $2
([1-9][2-9])(\d{6}) $1 milijuna $2
([1-9]{2}1)(\d{6}) $1 milijun $2
([1-9]{2}[0,2-9])(\d{6}) $1 milijuna $2


# milijarda

1(\d{9}) milijarda $1
2(\d{9}) dvije milijarde $1
([34])(\d{9}) $1 milijarde $2
([5-9])(\d{9}) $1 milijardi $2
(1[1-9])(\d{9}) $1 milijardi $2
([1-9]0)(\d{9}) $1 milijardi $2
([2378])1(\d{9}) $1deset jedna milijarda $2
41(\d{9}) četrdeset jedna milijarda $1
51(\d{9}) pedeset jedna milijarda $1
61(\d{9}) šezdeset jedna milijarda $1
91(\d{9}) devedeset jedna milijarda $1
([2378])2(\d{9}) $1deset dvije milijarde $2
42(\d{9}) četrdeset dvije milijarde $2
52(\d{9}) pedeset dvije milijarde $1
62(\d{9}) šezdeset dvije milijarde $1
92(\d{9}) devedeset dvije milijarde $1
([1-9][34])(\d{9}) $1 milijarde $2
([1-9][5-9])(\d{9}) $1 milijardi $2
([1-9]00)(\d{9}) $1 milijardi $2
101(\d{9}) sto jedna milijarda $1
102(\d{9}) sto dvije milijarde $1
201(\d{9}) dvjesto jedna milijarda $1
202(\d{9}) dvjesto dvije milijarde $1
([3-57-9])01(\d{9}) $1sto jedna milijarda $2
([3-57-9])02(\d{9}) $1sto dvije milijarda $2
601(\d{9}) šesto jedna milijarda $1
602(\d{9}) šesto dvije milijarde $1
1(\d{11}) sto $1
2(\d{11}) dvjesto $1
([3-57-9])(\d{11}) $1sto $2
6(\d{11}) šesto $1


# bilijun

1(\d{12}) bilijun $1
([2-9])(\d{12}) $1 bilijuna $2
([1-9]0{1,2})(\d{12}) $1 bilijuna $2
([1-9]1)(\d{12}) $1 bilijun $2
([1-9][2-9])(\d{12}) $1 bilijuna $2
([1-9]{2}1)(\d{12}) $1 bilijun $2
([1-9]{2}[0,2-9])(\d{12}) $1 bilijuna $2


# bilijarda

1(\d{15}) bilijarda $1
2(\d{15}) dvije bilijarde $1
([34])(\d{15}) $1 bilijarde $2
([5-9])(\d{15}) $1 bilijardi $2
(1[1-9])(\d{15}) $1 bilijardi $2
([1-9]0)(\d{15}) $1 bilijardi $2
([2378])1(\d{15}) $1deset jedna bilijarda $2
41(\d{15}) četrdeset jedna bilijarda $1
51(\d{15}) pedeset jedna bilijarda $1
61(\d{15}) šezdeset jedna bilijarda $1
91(\d{15}) devedeset jedna bilijarda $1
([2378])2(\d{15}) $1deset dvije bilijarde $2
42(\d{15}) četrdeset dvije bilijarde $2
52(\d{15}) pedeset dvije bilijarde $1
62(\d{15}) šezdeset dvije bilijarde $1
92(\d{15}) devedeset dvije bilijarde $1
([1-9][34])(\d{15}) $1 bilijarde $2
([1-9][5-9])(\d{15}) $1 bilijardi $2
([1-9]00)(\d{15}) $1 bilijardi $2
101(\d{15}) sto jedna bilijarda $1
102(\d{15}) sto dvije bilijarde $1
201(\d{15}) dvjesto jedna bilijarda $1
202(\d{15}) dvjesto dvije bilijarde $1
([3-57-9])01(\d{15}) $1sto jedna bilijarda $2
([3-57-9])02(\d{15}) $1sto dvije bilijarda $2
601(\d{15}) šesto jedna bilijarda $1
602(\d{15}) šesto dvije bilijarde $1
1(\d{17}) sto $1
2(\d{17}) dvjesto $1
([3-57-9])(\d{17}) $1sto $2
6(\d{17}) šesto $1


# trilijun

1(\d{18}) trilijun $1
([2-9])(\d{18}) $1 trilijuna $2
([1-9]0{1,2})(\d{18}) $1 trilijuna $2
([1-9]1)(\d{18}) $1 trilijun $2
([1-9][2-9])(\d{18}) $1 trilijuna $2
([1-9]{2}1)(\d{18}) $1 trilijun $2
([1-9]{2}[0,2-9])(\d{18}) $1 trilijuna $2


# trilijarda

1(\d{21}) trilijarda $1
2(\d{21}) dvije trilijarde $1
([34])(\d{21}) $1 trilijarde $2
([5-9])(\d{21}) $1 trilijardi $2
(1[1-9])(\d{21}) $1 trilijardi $2
([1-9]0)(\d{21}) $1 trilijardi $2
([2378])1(\d{21}) $1deset jedna trilijarda $2
41(\d{21}) četrdeset jedna trilijarda $1
51(\d{21}) pedeset jedna trilijarda $1
61(\d{21}) šezdeset jedna trilijarda $1
91(\d{21}) devedeset jedna trilijarda $1
([2378])2(\d{21}) $1deset dvije trilijarde $2
42(\d{21}) četrdeset dvije trilijarde $2
52(\d{21}) pedeset dvije trilijarde $1
62(\d{21}) šezdeset dvije trilijarde $1
92(\d{21}) devedeset dvije trilijarde $1
([1-9][34])(\d{21}) $1 trilijarde $2
([1-9][5-9])(\d{21}) $1 trilijardi $2
([1-9]00)(\d{21}) $1 trilijardi $2
101(\d{21}) sto jedna trilijarda $1
102(\d{21}) sto dvije trilijarde $1
201(\d{21}) dvjesto jedna trilijarda $1
202(\d{21}) dvjesto dvije trilijarde $1
([3-57-9])01(\d{21}) $1sto jedna trilijarda $2
([3-57-9])02(\d{21}) $1sto dvije trilijarda $2
601(\d{21}) šesto jedna trilijarda $1
602(\d{21}) šesto dvije trilijarde $1
1(\d{23}) sto $1
2(\d{23}) dvjesto $1
([3-57-9])(\d{23}) $1sto $2
6(\d{23}) šesto $1


# kvadrilijun

1(\d{24}) kvadrilijun $1
([2-9])(\d{24}) $1 kvadrilijuna $2
([1-9]0{1,2})(\d{24}) $1 kvadrilijuna $2
([1-9]1)(\d{24}) $1 kvadrilijun $2
([1-9][2-9])(\d{24}) $1 kvadrilijuna $2
([1-9]{2}1)(\d{24}) $1 kvadrilijun $2
([1-9]{2}[0,2-9])(\d{24}) $1 kvadrilijuna $2


# kvadrilijarda

1(\d{27}) kvadrilijarda $1
2(\d{27}) dvije kvadrilijarde $1
([34])(\d{27}) $1 kvadrilijarde $2
([5-9])(\d{27}) $1 kvadrilijardi $2
(1[1-9])(\d{27}) $1 kvadrilijardi $2
([1-9]0)(\d{27}) $1 kvadrilijardi $2
([2378])1(\d{27}) $1deset jedna kvadrilijarda $2
41(\d{27}) četrdeset jedna kvadrilijarda $1
51(\d{27}) pedeset jedna kvadrilijarda $1
61(\d{27}) šezdeset jedna kvadrilijarda $1
91(\d{27}) devedeset jedna kvadrilijarda $1
([2378])2(\d{27}) $1deset dvije kvadrilijarde $2
42(\d{27}) četrdeset dvije kvadrilijarde $2
52(\d{27}) pedeset dvije kvadrilijarde $1
62(\d{27}) šezdeset dvije kvadrilijarde $1
92(\d{27}) devedeset dvije kvadrilijarde $1
([1-9][34])(\d{27}) $1 kvadrilijarde $2
([1-9][5-9])(\d{27}) $1 kvadrilijardi $2
([1-9]00)(\d{27}) $1 kvadrilijardi $2
101(\d{27}) sto jedna kvadrilijarda $1
102(\d{27}) sto dvije kvadrilijarde $1
201(\d{27}) dvjesto jedna kvadrilijarda $1
202(\d{27}) dvjesto dvije kvadrilijarde $1
([3-57-9])01(\d{27}) $1sto jedna kvadrilijarda $2
([3-57-9])02(\d{27}) $1sto dvije kvadrilijarda $2
601(\d{27}) šesto jedna kvadrilijarda $1
602(\d{27}) šesto dvije kvadrilijarde $1
1(\d{29}) sto $1
2(\d{29}) dvjesto $1
([3-57-9])(\d{29}) $1sto $2
6(\d{29}) šesto $1


# kvintilijun

1(\d{30}) kvintilijun $1
([2-9])(\d{30}) $1 kvintilijuna $2
([1-9]0{1,2})(\d{30}) $1 kvintilijuna $2
([1-9]1)(\d{30}) $1 kvintilijun $2
([1-9][2-9])(\d{30}) $1 kvintilijuna $2
([1-9]{2}1)(\d{30}) $1 kvintilijun $2
([1-9]{2}[0,2-9])(\d{30}) $1 kvintilijuna $2


# kvintilijarda

1(\d{33}) kvintilijarda $1
2(\d{33}) dvije kvintilijarde $1
([34])(\d{33}) $1 kvintilijarde $2
([5-9])(\d{33}) $1 kvintilijardi $2
(1[1-9])(\d{33}) $1 kvintilijardi $2
([1-9]0)(\d{33}) $1 kvintilijardi $2
([2378])1(\d{33}) $1deset jedna kvintilijarda $2
41(\d{33}) četrdeset jedna kvintilijarda $1
51(\d{33}) pedeset jedna kvintilijarda $1
61(\d{33}) šezdeset jedna kvintilijarda $1
91(\d{33}) devedeset jedna kvintilijarda $1
([2378])2(\d{33}) $1deset dvije kvintilijarde $2
42(\d{33}) četrdeset dvije kvintilijarde $2
52(\d{33}) pedeset dvije kvintilijarde $1
62(\d{33}) šezdeset dvije kvintilijarde $1
92(\d{33}) devedeset dvije kvintilijarde $1
([1-9][34])(\d{33}) $1 kvintilijarde $2
([1-9][5-9])(\d{33}) $1 kvintilijardi $2
([1-9]00)(\d{33}) $1 kvintilijardi $2
101(\d{33}) sto jedna kvintilijarda $1
102(\d{33}) sto dvije kvintilijarde $1
201(\d{33}) dvjesto jedna kvintilijarda $1
202(\d{33}) dvjesto dvije kvintilijarde $1
([3-57-9])01(\d{33}) $1sto jedna kvintilijarda $2
([3-57-9])02(\d{33}) $1sto dvije kvintilijarda $2
601(\d{33}) šesto jedna kvintilijarda $1
602(\d{33}) šesto dvije kvintilijarde $1
1(\d{35}) sto $1
2(\d{35}) dvjesto $1
([3-57-9])(\d{35}) $1sto $2
6(\d{35}) šesto $1


# sekstilijun

1(\d{36}) sekstilijun $1
([2-9])(\d{36}) $1 sekstilijuna $2
([1-9]0{1,2})(\d{36}) $1 sekstilijuna $2
([1-9]1)(\d{36}) $1 sekstilijun $2
([1-9][2-9])(\d{36}) $1 sekstilijuna $2
([1-9]{2}1)(\d{36}) $1 sekstilijun $2
([1-9]{2}[0,2-9])(\d{36}) $1 sekstilijuna $2


# sekstilijarda

1(\d{39}) sekstilijarda $1
2(\d{39}) dvije sekstilijarde $1
([34])(\d{39}) $1 sekstilijarde $2
([5-9])(\d{39}) $1 sekstilijardi $2
(1[1-9])(\d{39}) $1 sekstilijardi $2
([1-9]0)(\d{39}) $1 sekstilijardi $2
([2378])1(\d{39}) $1deset jedna sekstilijarda $2
41(\d{39}) četrdeset jedna sekstilijarda $1
51(\d{39}) pedeset jedna sekstilijarda $1
61(\d{39}) šezdeset jedna sekstilijarda $1
91(\d{39}) devedeset jedna sekstilijarda $1
([2378])2(\d{39}) $1deset dvije sekstilijarde $2
42(\d{39}) četrdeset dvije sekstilijarde $2
52(\d{39}) pedeset dvije sekstilijarde $1
62(\d{39}) šezdeset dvije sekstilijarde $1
92(\d{39}) devedeset dvije sekstilijarde $1
([1-9][34])(\d{39}) $1 sekstilijarde $2
([1-9][5-9])(\d{39}) $1 sekstilijardi $2
([1-9]00)(\d{39}) $1 sekstilijardi $2
101(\d{39}) sto jedna sekstilijarda $1
102(\d{39}) sto dvije sekstilijarde $1
201(\d{39}) dvjesto jedna sekstilijarda $1
202(\d{39}) dvjesto dvije sekstilijarde $1
([3-57-9])01(\d{39}) $1sto jedna sekstilijarda $2
([3-57-9])02(\d{39}) $1sto dvije sekstilijarda $2
601(\d{39}) šesto jedna sekstilijarda $1
602(\d{39}) šesto dvije sekstilijarde $1
1(\d{41}) sto $1
2(\d{41}) dvjesto $1
([3-57-9])(\d{41}) $1sto $2
6(\d{41}) šesto $1


# septilijun

1(\d{42}) septilijun $1
([2-9])(\d{42}) $1 septilijuna $2
([1-9]0{1,2})(\d{42}) $1 septilijuna $2
([1-9]1)(\d{42}) $1 septilijun $2
([1-9][2-9])(\d{42}) $1 septilijuna $2
([1-9]{2}1)(\d{42}) $1 septilijun $2
([1-9]{2}[0,2-9])(\d{42}) $1 septilijuna $2


# septilijarda

1(\d{45}) septilijarda $1
2(\d{45}) dvije septilijarde $1
([34])(\d{45}) $1 septilijarde $2
([5-9])(\d{45}) $1 septilijardi $2
(1[1-9])(\d{45}) $1 septilijardi $2
([1-9]0)(\d{45}) $1 septilijardi $2
([2378])1(\d{45}) $1deset jedna septilijarda $2
41(\d{45}) četrdeset jedna septilijarda $1
51(\d{45}) pedeset jedna septilijarda $1
61(\d{45}) šezdeset jedna septilijarda $1
91(\d{45}) devedeset jedna septilijarda $1
([2378])2(\d{45}) $1deset dvije septilijarde $2
42(\d{45}) četrdeset dvije septilijarde $2
52(\d{45}) pedeset dvije septilijarde $1
62(\d{45}) šezdeset dvije septilijarde $1
92(\d{45}) devedeset dvije septilijarde $1
([1-9][34])(\d{45}) $1 septilijarde $2
([1-9][5-9])(\d{45}) $1 septilijardi $2
([1-9]00)(\d{45}) $1 septilijardi $2
101(\d{45}) sto jedna septilijarda $1
102(\d{45}) sto dvije septilijarde $1
201(\d{45}) dvjesto jedna septilijarda $1
202(\d{45}) dvjesto dvije septilijarde $1
([3-57-9])01(\d{45}) $1sto jedna septilijarda $2
([3-57-9])02(\d{45}) $1sto dvije septilijarda $2
601(\d{45}) šesto jedna septilijarda $1
602(\d{45}) šesto dvije septilijarde $1
1(\d{47}) sto $1
2(\d{47}) dvjesto $1
([3-57-9])(\d{47}) $1sto $2
6(\d{47}) šesto $1


# oktilijun

1(\d{48}) oktilijun $1
([2-9])(\d{48}) $1 oktilijuna $2
([1-9]0{1,2})(\d{48}) $1 oktilijuna $2
([1-9]1)(\d{48}) $1 oktilijun $2
([1-9][2-9])(\d{48}) $1 oktilijuna $2
([1-9]{2}1)(\d{48}) $1 oktilijun $2
([1-9]{2}[0,2-9])(\d{48}) $1 oktilijuna $2


# oktilijarda

1(\d{51}) oktilijarda $1
2(\d{51}) dvije oktilijarde $1
([34])(\d{51}) $1 oktilijarde $2
([5-9])(\d{51}) $1 oktilijardi $2
(1[1-9])(\d{51}) $1 oktilijardi $2
([1-9]0)(\d{51}) $1 oktilijardi $2
([2378])1(\d{51}) $1deset jedna oktilijarda $2
41(\d{51}) četrdeset jedna oktilijarda $1
51(\d{51}) pedeset jedna oktilijarda $1
61(\d{51}) šezdeset jedna oktilijarda $1
91(\d{51}) devedeset jedna oktilijarda $1
([2378])2(\d{51}) $1deset dvije oktilijarde $2
42(\d{51}) četrdeset dvije oktilijarde $2
52(\d{51}) pedeset dvije oktilijarde $1
62(\d{51}) šezdeset dvije oktilijarde $1
92(\d{51}) devedeset dvije oktilijarde $1
([1-9][34])(\d{51}) $1 oktilijarde $2
([1-9][5-9])(\d{51}) $1 oktilijardi $2
([1-9]00)(\d{51}) $1 oktilijardi $2
101(\d{51}) sto jedna oktilijarda $1
102(\d{51}) sto dvije oktilijarde $1
201(\d{51}) dvjesto jedna oktilijarda $1
202(\d{51}) dvjesto dvije oktilijarde $1
([3-57-9])01(\d{51}) $1sto jedna oktilijarda $2
([3-57-9])02(\d{51}) $1sto dvije oktilijarda $2
601(\d{51}) šesto jedna oktilijarda $1
602(\d{51}) šesto dvije oktilijarde $1
1(\d{53}) sto $1
2(\d{53}) dvjesto $1
([3-57-9])(\d{53}) $1sto $2
6(\d{53}) šesto $1


# nonilijun

1(\d{54}) nonilijun $1
([2-9])(\d{54}) $1 nonilijuna $2
([1-9]0{1,2})(\d{54}) $1 nonilijuna $2
([1-9]1)(\d{54}) $1 nonilijun $2
([1-9][2-9])(\d{54}) $1 nonilijuna $2
([1-9]{2}1)(\d{54}) $1 nonilijun $2
([1-9]{2}[0,2-9])(\d{54}) $1 nonilijuna $2


# nonilijarda

1(\d{57}) nonilijarda $1
2(\d{57}) dvije nonilijarde $1
([34])(\d{57}) $1 nonilijarde $2
([5-9])(\d{57}) $1 nonilijardi $2
(1[1-9])(\d{57}) $1 nonilijardi $2
([1-9]0)(\d{57}) $1 nonilijardi $2
([2378])1(\d{57}) $1deset jedna nonilijarda $2
41(\d{57}) četrdeset jedna nonilijarda $1
51(\d{57}) pedeset jedna nonilijarda $1
61(\d{57}) šezdeset jedna nonilijarda $1
91(\d{57}) devedeset jedna nonilijarda $1
([2378])2(\d{57}) $1deset dvije nonilijarde $2
42(\d{57}) četrdeset dvije nonilijarde $2
52(\d{57}) pedeset dvije nonilijarde $1
62(\d{57}) šezdeset dvije nonilijarde $1
92(\d{57}) devedeset dvije nonilijarde $1
([1-9][34])(\d{57}) $1 nonilijarde $2
([1-9][5-9])(\d{57}) $1 nonilijardi $2
([1-9]00)(\d{57}) $1 nonilijardi $2
101(\d{57}) sto jedna nonilijarda $1
102(\d{57}) sto dvije nonilijarde $1
201(\d{57}) dvjesto jedna nonilijarda $1
202(\d{57}) dvjesto dvije nonilijarde $1
([3-57-9])01(\d{57}) $1sto jedna nonilijarda $2
([3-57-9])02(\d{57}) $1sto dvije nonilijarda $2
601(\d{57}) šesto jedna nonilijarda $1
602(\d{57}) šesto dvije nonilijarde $1
1(\d{59}) sto $1
2(\d{59}) dvjesto $1
([3-57-9])(\d{59}) $1sto $2
6(\d{59}) šesto $1


# decilijun

1(\d{60}) decilijun $1
([2-9])(\d{60}) $1 decilijuna $2
([1-9]0{1,2})(\d{60}) $1 decilijuna $2
([1-9]1)(\d{60}) $1 decilijun $2
([1-9][2-9])(\d{60}) $1 decilijuna $2
([1-9]{2}1)(\d{60}) $1 decilijun $2
([1-9]{2}[0,2-9])(\d{60}) $1 decilijuna $2


# decilijarda

1(\d{63}) decilijarda $1
2(\d{63}) dvije decilijarde $1
([34])(\d{63}) $1 decilijarde $2
([5-9])(\d{63}) $1 decilijardi $2
(1[1-9])(\d{63}) $1 decilijardi $2
([1-9]0)(\d{63}) $1 decilijardi $2
([2378])1(\d{63}) $1deset jedna decilijarda $2
41(\d{63}) četrdeset jedna decilijarda $1
51(\d{63}) pedeset jedna decilijarda $1
61(\d{63}) šezdeset jedna decilijarda $1
91(\d{63}) devedeset jedna decilijarda $1
([2378])2(\d{63}) $1deset dvije decilijarde $2
42(\d{63}) četrdeset dvije decilijarde $2
52(\d{63}) pedeset dvije decilijarde $1
62(\d{63}) šezdeset dvije decilijarde $1
92(\d{63}) devedeset dvije decilijarde $1
([1-9][34])(\d{63}) $1 decilijarde $2
([1-9][5-9])(\d{63}) $1 decilijardi $2
([1-9]00)(\d{63}) $1 decilijardi $2
101(\d{63}) sto jedna decilijarda $1
102(\d{63}) sto dvije decilijarde $1
201(\d{63}) dvjesto jedna decilijarda $1
202(\d{63}) dvjesto dvije decilijarde $1
([3-57-9])01(\d{63}) $1sto jedna decilijarda $2
([3-57-9])02(\d{63}) $1sto dvije decilijarda $2
601(\d{63}) šesto jedna decilijarda $1
602(\d{63}) šesto dvije decilijarde $1
1(\d{65}) sto $1
2(\d{65}) dvjesto $1
([3-57-9])(\d{65}) $1sto $2
6(\d{65}) šesto $1


# undecilijun

1(\d{66}) undecilijun $1
([2-9])(\d{66}) $1 undecilijuna $2
([1-9]0{1,2})(\d{66}) $1 undecilijuna $2
([1-9]1)(\d{66}) $1 undecilijun $2
([1-9][2-9])(\d{66}) $1 undecilijuna $2
([1-9]{2}1)(\d{66}) $1 undecilijun $2
([1-9]{2}[0,2-9])(\d{66}) $1 undecilijuna $2


# undecilijarda

1(\d{69}) undecilijarda $1
2(\d{69}) dvije undecilijarde $1
([34])(\d{69}) $1 undecilijarde $2
([5-9])(\d{69}) $1 undecilijardi $2
(1[1-9])(\d{69}) $1 undecilijardi $2
([1-9]0)(\d{69}) $1 undecilijardi $2
([2378])1(\d{69}) $1deset jedna undecilijarda $2
41(\d{69}) četrdeset jedna undecilijarda $1
51(\d{69}) pedeset jedna undecilijarda $1
61(\d{69}) šezdeset jedna undecilijarda $1
91(\d{69}) devedeset jedna undecilijarda $1
([2378])2(\d{69}) $1deset dvije undecilijarde $2
42(\d{69}) četrdeset dvije undecilijarde $2
52(\d{69}) pedeset dvije undecilijarde $1
62(\d{69}) šezdeset dvije undecilijarde $1
92(\d{69}) devedeset dvije undecilijarde $1
([1-9][34])(\d{69}) $1 undecilijarde $2
([1-9][5-9])(\d{69}) $1 undecilijardi $2
([1-9]00)(\d{69}) $1 undecilijardi $2
101(\d{69}) sto jedna undecilijarda $1
102(\d{69}) sto dvije undecilijarde $1
201(\d{69}) dvjesto jedna undecilijarda $1
202(\d{69}) dvjesto dvije undecilijarde $1
([3-57-9])01(\d{69}) $1sto jedna undecilijarda $2
([3-57-9])02(\d{69}) $1sto dvije undecilijarda $2
601(\d{69}) šesto jedna undecilijarda $1
602(\d{69}) šesto dvije undecilijarde $1
1(\d{71}) sto $1
2(\d{71}) dvjesto $1
([3-57-9])(\d{71}) $1sto $2
6(\d{71}) šesto $1


# duodecilijun

1(\d{72}) duodecilijun $1
([2-9])(\d{72}) $1 duodecilijuna $2
([1-9]0{1,2})(\d{72}) $1 duodecilijuna $2
([1-9]1)(\d{72}) $1 duodecilijun $2
([1-9][2-9])(\d{72}) $1 duodecilijuna $2
([1-9]{2}1)(\d{72}) $1 duodecilijun $2
([1-9]{2}[0,2-9])(\d{72}) $1 duodecilijuna $2


# duodecilijarda

1(\d{75}) duodecilijarda $1
2(\d{75}) dvije duodecilijarde $1
([34])(\d{75}) $1 duodecilijarde $2
([5-9])(\d{75}) $1 duodecilijardi $2
(1[1-9])(\d{75}) $1 duodecilijardi $2
([1-9]0)(\d{75}) $1 duodecilijardi $2
([2378])1(\d{75}) $1deset jedna duodecilijarda $2
41(\d{75}) četrdeset jedna duodecilijarda $1
51(\d{75}) pedeset jedna duodecilijarda $1
61(\d{75}) šezdeset jedna duodecilijarda $1
91(\d{75}) devedeset jedna duodecilijarda $1
([2378])2(\d{75}) $1deset dvije duodecilijarde $2
42(\d{75}) četrdeset dvije duodecilijarde $2
52(\d{75}) pedeset dvije duodecilijarde $1
62(\d{75}) šezdeset dvije duodecilijarde $1
92(\d{75}) devedeset dvije duodecilijarde $1
([1-9][34])(\d{75}) $1 duodecilijarde $2
([1-9][5-9])(\d{75}) $1 duodecilijardi $2
([1-9]00)(\d{75}) $1 duodecilijardi $2
101(\d{75}) sto jedna duodecilijarda $1
102(\d{75}) sto dvije duodecilijarde $1
201(\d{75}) dvjesto jedna duodecilijarda $1
202(\d{75}) dvjesto dvije duodecilijarde $1
([3-57-9])01(\d{75}) $1sto jedna duodecilijarda $2
([3-57-9])02(\d{75}) $1sto dvije duodecilijarda $2
601(\d{75}) šesto jedna duodecilijarda $1
602(\d{75}) šesto dvije duodecilijarde $1
1(\d{77}) sto $1
2(\d{77}) dvjesto $1
([3-57-9])(\d{77}) $1sto $2
6(\d{77}) šesto $1


# tridecilijun

1(\d{78}) tridecilijun $1
([2-9])(\d{78}) $1 tridecilijuna $2
([1-9]0{1,2})(\d{78}) $1 tridecilijuna $2
([1-9]1)(\d{78}) $1 tridecilijun $2
([1-9][2-9])(\d{78}) $1 tridecilijuna $2
([1-9]{2}1)(\d{78}) $1 tridecilijun $2
([1-9]{2}[0,2-9])(\d{78}) $1 tridecilijuna $2


# tridecilijarda

1(\d{81}) tridecilijarda $1
2(\d{81}) dvije tridecilijarde $1
([34])(\d{81}) $1 tridecilijarde $2
([5-9])(\d{81}) $1 tridecilijardi $2
(1[1-9])(\d{81}) $1 tridecilijardi $2
([1-9]0)(\d{81}) $1 tridecilijardi $2
([2378])1(\d{81}) $1deset jedna tridecilijarda $2
41(\d{81}) četrdeset jedna tridecilijarda $1
51(\d{81}) pedeset jedna tridecilijarda $1
61(\d{81}) šezdeset jedna tridecilijarda $1
91(\d{81}) devedeset jedna tridecilijarda $1
([2378])2(\d{81}) $1deset dvije tridecilijarde $2
42(\d{81}) četrdeset dvije tridecilijarde $2
52(\d{81}) pedeset dvije tridecilijarde $1
62(\d{81}) šezdeset dvije tridecilijarde $1
92(\d{81}) devedeset dvije tridecilijarde $1
([1-9][34])(\d{81}) $1 tridecilijarde $2
([1-9][5-9])(\d{81}) $1 tridecilijardi $2
([1-9]00)(\d{81}) $1 tridecilijardi $2
101(\d{81}) sto jedna tridecilijarda $1
102(\d{81}) sto dvije tridecilijarde $1
201(\d{81}) dvjesto jedna tridecilijarda $1
202(\d{81}) dvjesto dvije tridecilijarde $1
([3-57-9])01(\d{81}) $1sto jedna tridecilijarda $2
([3-57-9])02(\d{81}) $1sto dvije tridecilijarda $2
601(\d{81}) šesto jedna tridecilijarda $1
602(\d{81}) šesto dvije tridecilijarde $1
1(\d{83}) sto $1
2(\d{83}) dvjesto $1
([3-57-9])(\d{83}) $1sto $2
6(\d{83}) šesto $1


# negativni brojevi

[-–][\s]?(\d+) minus $1



## redni brojevi do (i uključujući) devetsto devedeset devet milijuna devetsto devedeset devet tisuća devetsto devedeset deveti

^0[\.]$ nulti
1[\.] prvi
2[\.] drugi
3[\.] treći
4[\.] četvrti
5[\.] peti
6[\.] šesti
7[\.] sedmi
8[\.] osmi
9[\.] deveti
(10)[\.] $1i
(1\d)[\.] $1i
([2378])0[\.] $1deseti
40[\.] četrdeseti
50[\.] pedeseti
60[\.] šezdeseti
90[\.] devedeseti
([2378])(\d[\.]) $1deset $2
4(\d[\.]) četrdeset $1
5(\d[\.]) pedeset $1
6(\d[\.]) šezdeset $1
9(\d[\.]) devedeset $1
100[\.] stoti
10(\d[\.]) sto $1
1(\d{2}[\.]) sto $1
(200)[\.] dvjestoti
20(\d[\.]) dvjesto $1
2(\d{2}[\.]) dvjesto $1
([3-57-9])00[\.] $1stoti
600[\.] šestoti
([3-57-9])0(\d[\.]) $1sto $2
60(\d[\.]) šesto $1
([3-57-9])(\d{2}[\.]) $1sto $2
6(\d{2}[\.]) šesto $1



9([3-9])000[\.] devedeset$1tisućiti
(6[3-9])000[\.] $1tisućiti
(5[3-9])000[\.] $1tisućiti
(4[3-9])000[\.] $1tisućiti
([2378][3-9])000[\.] $1tisućiti
92000[\.] devedesetdvijetisućiti
62000[\.] šezdesetdvijetisućiti
52000[\.] pedesetdvijetisućiti
42000[\.] četrdesetdvijetisućiti
([2378])2000[\.] $1desetjednutisućiti
91000[\.] devedesetjednutisućiti
61000[\.] šezdesetjednutisućiti
51000[\.] pedesetjednutisućiti
41000[\.] četrdesetjednutisućiti
([2378])1000[\.] $1desetjednutisućiti
([2-9]0)000[\.] $1desettisućiti
(1\d)000[\.] $1tisućiti
([1-9]\d)000[\.] $1tisućiti
([3-9])000[\.] $1tisućiti
2000[\.] dvijetisućiti
1000[\.] tisućiti

100(\d[\.]) tisuću $1
10(\d{2}[\.]) tisuću $1
1(\d{3}[\.]) tisuću $1

200(\d[\.]) dvije tisuće $1
20(\d{2}[\.]) tisuću $1
2(\d{3}[\.]) tisuću $1

([3-9])00(\d[\.]) $1 tisuće $2
([3-9])0(\d{2}[\.]) $1 tisuće $2
([3-9])(\d{3}[\.]) $1 tisuće $2

(1\d)00(\d[\.]) $1 tisuća $2
(1\d)0(\d{2}[\.]) $1 tisuća $2
(1\d)(\d{3}[\.]) $1 tisuća $2

([2-9]0)00(\d[\.]) $1deset tisuća $2
([2-9]0)0(\d{2}[\.]) $1deset tisuća $2
([2-9]0)(\d{3}[\.]) $1deset tisuća $2

([2378])100(\d[\.]) $1deset jednu tisuću $2
([2378])10(\d{2}[\.]) $1deset jednu tisuću $2
([2378])1(\d{3}[\.]) $1deset jednu tisuću $2

4100(\d[\.]) četrdeset jednu tisuću $1
410(\d{2}[\.]) četrdeset jednu tisuću $1
41(\d{3}[\.]) četrdeset jednu tisuću $1

5100(\d[\.]) pedeset jednu tisuću $1
510(\d{2}[\.]) pedeset jednu tisuću $1
51(\d{3}[\.]) pedeset jednu tisuću $1

6100(\d[\.]) žezdeset jednu tisuću $1
610(\d{2}[\.]) šezdeset jednu tisuću $1
61(\d{3}[\.]) šezdeset jednu tisuću $1

9100(\d[\.]) devedeset jednu tisuću $1
910(\d{2}[\.]) devedeset jednu tisuću $1
91(\d{3}[\.]) devedeset jednu tisuću $1

([2378])200(\d[\.]) $1deset dvije tisuće $2
([2378])20(\d{2}[\.]) $1deset dvije tisuće $2
([2378])2(\d{3}[\.]) $1deset dvije tisuće $2

4200(\d[\.]) četrdeset dvije tisuće $1
420(\d{2}[\.]) četrdeset dvije tisuće $1
42(\d{3}[\.]) četrdeset dvije tisuće $1

5200(\d[\.]) pedeset dvije tisuće $1
520(\d{2}[\.]) pedeset dvije tisuće $1
52(\d{3}[\.]) pedeset dvije tisuće $1

6200(\d[\.]) šezdeset dvije tisuće $1
620(\d{2}[\.]) šezdeset dvije tisuće $1
62(\d{3}[\.]) šezdeset dvije tisuće $1

9200(\d[\.]) devedeset dvije tisuće $1
920(\d{2}[\.]) devedeset dvije tisuće $1
92(\d{3}[\.]) devedeset dvije tisuće $1

([2378])([3-9])00(\d[\.]) $1deset $2 tisuće $3
([2378])([3-9])0(\d{2}[\.]) $1deset $2 tisuće $3
([2378])([3-9])(\d{3}[\.]) $1deset $2 tisuće $3

4([3-9])00(\d[\.]) četrdeset $1 tisuće $2
4([3-9])0(\d{2}[\.]) četrdeset $1 tisuće $2
4([3-9])(\d{3}[\.]) četrdeset $1 tisuće $2

5([3-9])00(\d[\.]) pedeset $1 tisuće $2
5([3-9])0(\d{2}[\.]) pedeset $1 tisuće $2
5([3-9])(\d{3}[\.]) pedeset $1 tisuće $2

6([3-9])00(\d[\.]) šezdeset $1 tisuće $2
6([3-9])0(\d{2}[\.]) šezdeset $1 tisuće $2
6([3-9])(\d{3}[\.]) šezdeset $1 tisuće $2

9([3-9])00(\d[\.]) devedeset $1 tisuće $2
9([3-9])0(\d{2}[\.]) devedeset $1 tisuće $2
9([3-9])(\d{3}[\.]) devedeset $1 tisuće $2


100000[\.] stotisućiti
10000(\d[\.]) sto tisuća $1
1000(\d{2}[\.]) sto tisuća $1
100(\d{3}[\.]) sto tisuća $1
10(\d{4}[\.]) sto tisuća $1
1(\d{5}[\.]) sto $1
200000[\.] dvjestotisućiti
20000(\d[\.]) dvjesto tisuća $1
2000(\d{2}[\.]) dvjesto tisuća $1
200(\d{2}[\.]) dvjesto tisuća $1
20(\d{4}[\.]) dvjesto tisuća $1
2(\d{5}[\.]) dvjesto $1
([3-57-9])00000[\.] $1stotisućiti
([3-57-9])0000(\d[\.]) $1sto tisuća $2
([3-57-9])000(\d{2}[\.]) $1sto tisuća $2
([3-57-9])00(\d{3}[\.]) $1sto tisuća $2
([3-57-9])0(\d{4}[\.]) $1sto tisuća $2
([3-57-9])(\d{5}[\.]) $1sto $2
600000[\.] šestotisućiti
60000(\d[\.]) šesto tisuća $2
6000(\d{2}[\.]) šesto tisuća $2
600(\d{3}[\.]) šesto tisuća $2
60(\d{4}[\.]) šest tisuća $2
6(\d{5}[\.]) šesto $2
1000000[\.] milijunti
100000(\d[\.]) milijun $1
1000(\d{2}[\.]) milijun $1
100(\d{3}[\.]) milijun $1
10(\d{4}[\.]) milijun $1
1(\d{5}[\.]) milijun $1
([2-9])000000[\.] $1milijunti
([2-9])00000(\d[\.]) $1 milijuna $2
([2-9])0000(\d{2}[\.]) $1 milijuna $2
([2-9])000(\d{3}[\.]) $1 milijuna $2
([2-9])00(\d{4}[\.]) $1 milijuna $2
([2-9])0(\d{5}[\.]) $1 milijuna $2
([2-9])(\d{6}[\.]) $1 milijuna $2
(1[0-9])000000[\.] $1milijunti
(1[0-9])00000(\d[\.]) $1 milijuna $2
(1[0-9])0000(\d{2}[\.]) $1 milijuna $2
(1[0-9])000(\d{3}[\.]) $1 milijuna $2
(1[0-9])00(\d{4}[\.]) $1 milijuna $2
(1[0-9])0(\d{5}[\.]) $1 milijuna $2
(1[0-9])(\d{6}[\.]) $1 milijuna $2
([2-478])0000000[\.] $1desetmilijunti
50000000[\.] pedesetmilijunti
60000000[\.] šezdesetmilijunti
90000000[\.] devedesetmilijunti
([2-478])000000(\d[\.]) $1deset milijuna $2
5000000(\d[\.]) pedeset milijuna $1
6000000(\d[\.]) šezdeset milijuna $1
9000000(\d[\.]) devedeset milijuna $1
([2-478])00000(\d{2}[\.]) $1deset milijuna $2
500000(\d{2}[\.]) pedeset milijuna $1
600000(\d{2}[\.]) šezdeset milijuna $1
900000(\d{2}[\.]) devedeset milijuna $1
([2-478])0000(\d{3}[\.]) $1deset milijuna $2
50000(\d{3}[\.]) pedeset milijuna $1
60000(\d{3}[\.]) šezdeset milijuna $1
90000(\d{3}[\.]) devedeset milijuna $1
([2-478])000(\d{4}[\.]) $1deset milijuna $2
5000(\d{4}[\.]) pedeset milijuna $1
6000(\d{4}[\.]) šezdeset milijuna $1
9000(\d{4}[\.]) devedeset milijuna $1
([2-478])00(\d{5}[\.]) $1deset milijuna $2
500(\d{5}[\.]) pedeset milijuna $1
600(\d{5}[\.]) šezdeset milijuna $1
900(\d{5}[\.]) devedeset milijuna $1
([2-478])0(\d{6}[\.]) $1deset milijuna $2
50(\d{6}[\.]) pedeset milijuna $1
60(\d{6}[\.]) šezdeset milijuna $1
90(\d{6}[\.]) devedeset milijuna $1
([2-478])1000000[\.] $1desetjedanmilijunti
51000000[\.] pedesetjedanmilijunti
61000000[\.] šezdesetjedanmilijunti
91000000[\.] devedesetjedanmilijunti
([2-478])100000(\d[\.]) $1deset jedan milijun $2
5100000(\d[\.]) pedeset jedan milijun $1
6100000(\d[\.]) šezdeset jedan milijun $1
9100000(\d[\.]) devedeset jedan milijun $1
([2-478])10000(\d{2}[\.]) $1deset jedan milijun $2
510000(\d{2}[\.]) pedeset jedan milijun $1
610000(\d{2}[\.]) šezdeset jedan milijun $1
910000(\d{2}[\.]) devedeset jedan milijun $1
([2-478])1000(\d{3}[\.]) $1deset jedan milijun $2
51000(\d{3}[\.]) pedeset jedan milijun $1
61000(\d{3}[\.]) šezdeset jedan milijun $1
91000(\d{3}[\.]) devedeset jedan milijun $1
([2-478])100(\d{4}[\.]) $1deset jedan milijun $2
5100(\d{4}[\.]) pedeset jedan milijun $1
6100(\d{4}[\.]) šezdeset jedan milijun $1
9100(\d{4}[\.]) devedeset jedan milijun $1
([2-478])10(\d{5}[\.]) $1deset jedan milijun $2
510(\d{5}[\.]) pedeset jedan milijun $1
610(\d{5}[\.]) šezdeset jedan milijun $1
910(\d{5}[\.]) devedeset jedan milijun $1
([2-478])1(\d{6}[\.]) $1deset jedan milijun $2
51(\d{6}[\.]) pedeset jedan milijun $1
61(\d{6}[\.]) šezdeset jedan milijun $1
91(\d{6}[\.]) devedeset jedan milijun $1
([2-9])([2-9])000000[\.] $1deset$2milijunti
5([2-9])000000[\.] pedeset$1milijunti
6([2-9])000000[\.] šezdeset1milijunti
9([2-9])000000[\.] devedeset1milijunti
([2-9])([2-9])00000(\d[\.]) $1deset $2 milijuna $3
5([2-9])00000(\d[\.]) pedeset $1 milijuna $2
6([2-9])00000(\d[\.]) šezdeset $1 milijuna $2
9([2-9])00000(\d[\.]) devedeset $1 milijuna $2
([2-9])([2-9])0000(\d{2}[\.]) $1deset $2 milijuna $3
5([2-9])0000(\d{2}[\.]) pedeset $1 milijuna $2
6([2-9])0000(\d{2}[\.]) šezdeset $1 milijuna $2
9([2-9])0000(\d{2}[\.]) devedeset $1 milijuna $2
([2-9])([2-9])000(\d{3}[\.]) $1deset $2 milijuna $3
5([2-9])000(\d{3}[\.]) pedeset $1 milijuna $2
6([2-9])000(\d{3}[\.]) šezdeset $1 milijuna $2
9([2-9])000(\d{3}[\.]) devedeset $1 milijuna $2
([2-9])([2-9])00(\d{}[\.]) $1deset $2 milijuna $3
5([2-9])00(\d{4}[\.]) pedeset $1 milijuna $2
6([2-9])00(\d{4}[\.]) šezdeset $1 milijuna $2
9([2-9])00(\d{4}[\.]) devedeset $1 milijuna $2
([2-9])([2-9])0(\d{5}[\.]) $1deset $2 milijuna $3
5([2-9])0(\d{5}[\.]) pedeset $1 milijuna $2
6([2-9])0(\d{5}[\.]) šezdeset $1 milijuna $2
9([2-9])0(\d{5}[\.]) devedeset $1 milijuna $2
([2-9])([2-9])(\d{6}[\.]) $1deset $2 milijuna $3
5([2-9])(\d{6}[\.]) pedeset $1 milijuna $2
6([2-9])(\d{6}[\.]) šezdeset $1 milijuna $2
9([2-9])(\d{6}[\.]) devedeset $1 milijuna $2
100000000[\.] stomilijunti
200000000[\.] dvjestomilijunti
([3478])00000000[\.] $1stomilijunti
500000000[\.] petstomilijunti
600000000[\.] šestomilijunti
900000000[\.] devetstomilijunti
10000000(\d[\.]) sto milijuna $1
1000000(\d{2}[\.]) sto milijuna $1
100000(\d{3}[\.]) sto milijuna $1
10000(\d{4}[\.]) sto milijuna $1
1000(\d{5}[\.]) sto milijuna $1
100(\d{6}[\.]) sto milijuna $1
20000000(\d[\.]) dvjesto milijuna $1
2000000(\d{2}[\.]) dvjesto milijuna $1
200000(\d{3}[\.]) dvjesto milijuna $1
20000(\d{4}[\.]) dvjesto milijuna $1
2000(\d{5}[\.]) dvjesto milijuna $1
200(\d{6}[\.]) dvjesto milijuna $1
([3478])0000000(\d[\.]) $1sto milijuna $2
([3478])000000(\d{2}[\.]) dvjesto milijuna $2
([3478])00000(\d{3}[\.]) dvjesto milijuna $2
([3478])0000(\d{4}[\.]) dvjesto milijuna $2
([3478])000(\d{5}[\.]) dvjesto milijuna $2
([3478])00(\d{6}[\.]) dvjesto milijuna $2
50000000(\d[\.]) petsto milijuna $1
5000000(\d{2}[\.]) petsto milijuna $1
500000(\d{3}[\.]) petsto milijuna $1
50000(\d{4}[\.]) petsto milijuna $1
5000(\d{5}[\.]) petsto milijuna $1
500(\d{6}[\.]) petsto milijuna $1
60000000(\d[\.]) šesto milijuna $1
6000000(\d{2}[\.]) šesto milijuna $1
600000(\d{3}[\.]) šesto milijuna $1
60000(\d{4}[\.]) šesto milijuna $1
6000(\d{5}[\.]) šesto milijuna $1
600(\d{6}[\.]) šesto milijuna $1
90000000(\d[\.]) devetsto milijuna $1
9000000(\d{2}[\.]) devetsto milijuna $1
900000(\d{3}[\.]) devetsto milijuna $1
90000(\d{4}[\.]) devetsto milijuna $1
9000(\d{5}[\.]) devetsto milijuna $1
900(\d{6}[\.]) devetsto milijuna $1
10000000(\d[\.]) sto milijuna $1
1000000(\d{2}[\.]) sto milijuna $1
100000(\d{3}[\.]) sto milijuna $1
10000(\d{4}[\.]) sto milijuna $1
1000(\d{5}[\.]) sto milijuna $1
100(\d{6}[\.]) sto milijuna $1
10100000(\d[\.]) sto jedan milijun $1
1010000(\d{2}[\.]) sto jedan milijun $1
101000(\d{3}[\.]) sto jedan milijun $1
10100(\d{4}[\.]) sto jedan milijun $1
1010(\d{5}[\.]) sto jedan milijun $1
101(\d{6}[\.]) sto jedan milijun $1
10([2-9])00000(\d[\.]) sto $1 milijuna $2
10([2-9])0000(\d{2}[\.]) sto $1 milijuna $2
10([2-9])000(\d{3}[\.]) sto $1 milijuna $2
10([2-9])00(\d{4}[\.]) sto $1 milijuna $2
10([2-9])0(\d{5}[\.]) sto $1 milijuna $2
10([2-9])(\d{6}[\.]) sto $1 milijuna $2
1([1-9]1)00000(\d[\.]) sto $1 milijun $2
1([1-9]1)0000(\d{2}[\.]) sto $1 milijun $2
1([1-9]1)000(\d{3}[\.]) sto $1 milijun $2
1([1-9]1)00(\d{4}[\.]) sto $1 milijun $2
1([1-9]1)0(\d{5}[\.]) sto $1 milijun $2
1([1-9]1)(\d{6}[\.]) sto $1 milijun $2
1([1-9][2-9])00000(\d[\.]) sto $1 milijuna $2
1([1-9][2-9])0000(\d{2}[\.]) sto $1 milijuna $2
1([1-9][2-9])000(\d{3}[\.]) sto $1 milijuna $2
1([1-9][2-9])00(\d{4}[\.]) sto $1 milijuna $2
1([1-9][2-9])0(\d{5}[\.]) sto $1 milijuna $2
1([1-9][2-9])(\d{6}[\.]) sto $1 milijuna $2
20000000(\d[\.]) dvjesto milijuna $1
2000000(\d{2}[\.]) dvjesto milijuna $1
200000(\d{3}[\.]) dvjesto milijuna $1
20000(\d{4}[\.]) dvjesto milijuna $1
2000(\d{5}[\.]) dvjesto milijuna $1
200(\d{6}[\.]) dvjesto milijuna $1
20100000(\d[\.]) dvjesto jedan milijun $1
2010000(\d{2}[\.]) dvjesto jedan milijun $1
201000(\d{3}[\.]) dvjesto jedan milijun $1
20100(\d{4}[\.]) dvjesto jedan milijun $1
2010(\d{5}[\.]) dvjesto jedan milijun $1
201(\d{6}[\.]) dvjesto jedan milijun $1
20([2-9])00000(\d[\.]) dvjesto $1 milijuna $2
20([2-9])0000(\d{2}[\.]) dvjesto $1 milijuna $2
20([2-9])000(\d{3}[\.]) dvjesto $1 milijuna $2
20([2-9])00(\d{4}[\.]) dvjesto $1 milijuna $2
20([2-9])0(\d{5}[\.]) dvjesto $1 milijuna $2
20([2-9])(\d{6}[\.]) dvjesto $1 milijuna $2
2([1-9]1)00000(\d[\.]) dvjesto $1 milijun $2
2([1-9]1)0000(\d{2}[\.]) dvjesto $1 milijun $2
2([1-9]1)000(\d{3}[\.]) dvjesto $1 milijun $2
2([1-9]1)00(\d{4}[\.]) dvjesto $1 milijun $2
2([1-9]1)0(\d{5}[\.]) dvjesto $1 milijun $2
2([1-9]1)(\d{6}[\.]) dvjesto $1 milijun $2
2([1-9][2-9])00000(\d[\.]) dvjesto $1 milijuna $2
2([1-9][2-9])0000(\d{2}[\.]) dvjesto $1 milijuna $2
2([1-9][2-9])000(\d{3}[\.]) dvjesto $1 milijuna $2
2([1-9][2-9])00(\d{4}[\.]) dvjesto $1 milijuna $2
2([1-9][2-9])0(\d{5}[\.]) dvjesto $1 milijuna $2
2([1-9][2-9])(\d{6}[\.]) dvjesto $1 milijuna $2
([3478])0000000(\d[\.]) $1sto milijuna $2
([3478])000000(\d{2}[\.]) $1sto milijuna $2
([3478])00000(\d{3}[\.]) $1sto milijuna $2
([3478])0000(\d{4}[\.]) $1sto milijuna $2
([3478])000(\d{5}[\.]) $1sto milijuna $2
([3478])00(\d{6}[\.]) $1sto milijuna $2
([3478])0100000(\d[\.]) $1sto jedan milijun $1
([3478])010000(\d{2}[\.]) $1sto jedan milijun $1
([3478])01000(\d{3}[\.]) $1sto jedan milijun $1
([3478])0100(\d{4}[\.]) $1sto jedan milijun $1
([3478])010(\d{5}[\.]) $1sto jedan milijun $1
([3478])01(\d{6}[\.]) $1sto jedan milijun $1
([3478])0([2-9])00000(\d[\.]) $1sto $1 milijuna $2
([3478])0([2-9])0000(\d{2}[\.]) $1sto $1 milijuna $2
([3478])0([2-9])000(\d{3}[\.]) $1sto $1 milijuna $2
([3478])0([2-9])00(\d{4}[\.]) $1sto $1 milijuna $2
([3478])0([2-9])0(\d{5}[\.]) $1sto $1 milijuna $2
([3478])0([2-9])(\d{6}[\.]) $1sto $1 milijuna $2
([3478])([1-9]1)00000(\d[\.]) $1sto $1 milijun $2
([3478])([1-9]1)0000(\d{2}[\.]) $1sto $1 milijun $2
([3478])([1-9]1)000(\d{3}[\.]) $1sto $1 milijun $2
([3478])([1-9]1)00(\d{4}[\.]) $1sto $1 milijun $2
([3478])([1-9]1)0(\d{5}[\.]) $1sto $1 milijun $2
([3478])([1-9]1)(\d{6}[\.]) $1sto $1 milijun $2
([3478])([1-9][2-9])00000(\d[\.]) $1sto $1 milijuna $2
([3478])([1-9][2-9])0000(\d{2}[\.]) $1sto $1 milijuna $2
([3478])([1-9][2-9])000(\d{3}[\.]) $1sto $1 milijuna $2
([3478])([1-9][2-9])00(\d{4}[\.]) $1sto $1 milijuna $2
([3478])([1-9][2-9])0(\d{5}[\.]) $1sto $1 milijuna $2
([3478])([1-9][2-9])(\d{6}[\.]) $1sto $1 milijuna $2
50000000(\d[\.]) petsto milijuna $1
5000000(\d{2}[\.]) petsto milijuna $1
500000(\d{3}[\.]) petsto milijuna $1
50000(\d{4}[\.]) petsto milijuna $1
5000(\d{5}[\.]) petsto milijuna $1
500(\d{6}[\.]) petsto milijuna $1
50100000(\d[\.]) petsto jedan milijun $1
5010000(\d{2}[\.]) petsto jedan milijun $1
501000(\d{3}[\.]) petsto jedan milijun $1
50100(\d{4}[\.]) petsto jedan milijun $1
5010(\d{5}[\.]) petsto jedan milijun $1
501(\d{6}[\.]) petsto jedan milijun $1
50([2-9])00000(\d[\.]) petsto $1 milijuna $2
50([2-9])0000(\d{2}[\.]) petsto $1 milijuna $2
50([2-9])000(\d{3}[\.]) petsto $1 milijuna $2
50([2-9])00(\d{4}[\.]) petsto $1 milijuna $2
50([2-9])0(\d{5}[\.]) petsto $1 milijuna $2
50([2-9])(\d{6}[\.]) petsto $1 milijuna $2
5([1-9]1)00000(\d[\.]) petsto $1 milijun $2
5([1-9]1)0000(\d{2}[\.]) petsto $1 milijun $2
5([1-9]1)000(\d{3}[\.]) petsto $1 milijun $2
5([1-9]1)00(\d{4}[\.]) petsto $1 milijun $2
5([1-9]1)0(\d{5}[\.]) petsto $1 milijun $2
5([1-9]1)(\d{6}[\.]) petsto $1 milijun $2
5([1-9][2-9])00000(\d[\.]) petsto $1 milijuna $2
5([1-9][2-9])0000(\d{2}[\.]) petsto $1 milijuna $2
5([1-9][2-9])000(\d{3}[\.]) petsto $1 milijuna $2
5([1-9][2-9])00(\d{4}[\.]) petsto $1 milijuna $2
5([1-9][2-9])0(\d{5}[\.]) petsto $1 milijuna $2
5([1-9][2-9])(\d{6}[\.]) petsto $1 milijuna $2
60000000(\d[\.]) šesto milijuna $1
6000000(\d{2}[\.]) šesto milijuna $1
600000(\d{3}[\.]) šesto milijuna $1
60000(\d{4}[\.]) šesto milijuna $1
6000(\d{5}[\.]) šesto milijuna $1
600(\d{6}[\.]) šesto milijuna $1
60100000(\d[\.]) šesto jedan milijun $1
6010000(\d{2}[\.]) šesto jedan milijun $1
601000(\d{3}[\.]) šesto jedan milijun $1
60100(\d{4}[\.]) šesto jedan milijun $1
6010(\d{5}[\.]) šesto jedan milijun $1
601(\d{6}[\.]) šesto jedan milijun $1
60([2-9])00000(\d[\.]) šesto $1 milijuna $2
60([2-9])0000(\d{2}[\.]) šesto $1 milijuna $2
60([2-9])000(\d{3}[\.]) šesto $1 milijuna $2
60([2-9])00(\d{4}[\.]) šesto $1 milijuna $2
60([2-9])0(\d{5}[\.]) šesto $1 milijuna $2
60([2-9])(\d{6}[\.]) šesto $1 milijuna $2
6([1-9]1)00000(\d[\.]) šesto $1 milijun $2
6([1-9]1)0000(\d{2}[\.]) šesto $1 milijun $2
6([1-9]1)000(\d{3}[\.]) šesto $1 milijun $2
6([1-9]1)00(\d{4}[\.]) šesto $1 milijun $2
6([1-9]1)0(\d{5}[\.]) šesto $1 milijun $2
6([1-9]1)(\d{6}[\.]) šesto $1 milijun $2
6([1-9][2-9])00000(\d[\.]) šesto $1 milijuna $2
6([1-9][2-9])0000(\d{2}[\.]) šesto $1 milijuna $2
6([1-9][2-9])000(\d{3}[\.]) šesto $1 milijuna $2
6([1-9][2-9])00(\d{4}[\.]) šesto $1 milijuna $2
6([1-9][2-9])0(\d{5}[\.]) šesto $1 milijuna $2
6([1-9][2-9])(\d{6}[\.]) šesto $1 milijuna $2
90000000(\d[\.]) devetsto milijuna $1
9000000(\d{2}[\.]) devetsto milijuna $1
900000(\d{3}[\.]) devetsto milijuna $1
90000(\d{4}[\.]) devetsto milijuna $1
9000(\d{5}[\.]) devetsto milijuna $1
900(\d{6}[\.]) devetsto milijuna $1
90100000(\d[\.]) devetsto jedan milijun $1
9010000(\d{2}[\.]) devetsto jedan milijun $1
901000(\d{3}[\.]) devetsto jedan milijun $1
90100(\d{4}[\.]) devetsto jedan milijun $1
9010(\d{5}[\.]) devetsto jedan milijun $1
901(\d{6}[\.]) devetsto jedan milijun $1
90([2-9])00000(\d[\.]) devetsto $1 milijuna $2
90([2-9])0000(\d{2}[\.]) devetsto $1 milijuna $2
90([2-9])000(\d{3}[\.]) devetsto $1 milijuna $2
90([2-9])00(\d{4}[\.]) devetsto $1 milijuna $2
90([2-9])0(\d{5}[\.]) devetsto $1 milijuna $2
90([2-9])(\d{6}[\.]) devetsto $1 milijuna $2
9([1-9]1)00000(\d[\.]) devetsto $1 milijun $2
9([1-9]1)0000(\d{2}[\.]) devetsto $1 milijun $2
9([1-9]1)000(\d{3}[\.]) devetsto $1 milijun $2
9([1-9]1)00(\d{4}[\.]) devetsto $1 milijun $2
9([1-9]1)0(\d{5}[\.]) devetsto $1 milijun $2
9([1-9]1)(\d{6}[\.]) devetsto $1 milijun $2
9([1-9][2-9])00000(\d[\.]) devetsto $1 milijuna $2
9([1-9][2-9])0000(\d{2}[\.]) devetsto $1 milijuna $2
9([1-9][2-9])000(\d{3}[\.]) devetsto $1 milijuna $2
9([1-9][2-9])00(\d{4}[\.]) devetsto $1 milijuna $2
9([1-9][2-9])0(\d{5}[\.]) devetsto $1 milijuna $2
9([1-9][2-9])(\d{6}[\.]) devetsto $1 milijuna $2

1000000000[\.] milijarditi
100000000(\d[\.])  milijardu $1
10000000(\d{2}[\.])  milijardu $1
1000000(\d{3}[\.])  milijardu $1
100000(\d{4}[\.]) milijardu $1
10000(\d{5}[\.]) milijardu $1
1000(\d{6}[\.]) milijardu $1
100(\d{7}[\.]) milijardu $1
10(\d{8}[\.]) milijardu $1
1(\d{9}[\.]) milijardu $1
2000000000[\.] dvijemilijarditi
200000000(\d[\.])  dvije milijarde $1
20000000(\d{2}[\.])  dvije milijarde $1
2000000(\d{3}[\.])  dvije milijarde $1
200000(\d{4}[\.])  dvije milijarde $1
20000(\d{5}[\.])  dvije milijarde $1
2000(\d{6}[\.])  dvije milijarde $1
200(\d{7}[\.])  dvije milijarde $1
20(\d{8}[\.])  dvije milijarde $1
2(\d{9}[\.])  dvije milijarde $1
([34])000000000[\.] $1milijarditi
([34])00000000(\d[\.])  $1 milijarde $2
([34])0000000(\d{2}[\.])  $1 milijarde $2
([34])000000(\d{3}[\.])  $1 milijarde $2
([34])00000(\d{4}[\.])  $1 milijarde $2
([34])0000(\d{5}[\.])  $1 milijarde $2
([34])000(\d{6}[\.])  $1 milijarde $2
([34])00(\d{7}[\.])  $1 milijarde $2
([34])0(\d{8}[\.])  $1 milijarde $2
([34])(\d{9}[\.])  $1 milijarde $2
([5-9])000000000[\.] $1milijarditi
([5-9])00000000(\d[\.])  $1 milijardi $2
([5-9])0000000(\d{2}[\.])  $1 milijardi $2
([5-9])000000(\d{3}[\.])  $1 milijardi $2
([5-9])00000(\d{4}[\.])  $1 milijardi $2
([5-9])0000(\d{5}[\.])  $1 milijardi $2
([5-9])000(\d{6}[\.])  $1 milijardi $2
([5-9])00(\d{7}[\.])  $1 milijardi $2
([5-9])0(\d{8}[\.])  $1 milijardi $2
([5-9])(\d{9}[\.])  $1 milijardi $2
(1[0-9])000000000[\.] $1milijarditi
(1[0-9])00000000(\d[\.]) $1 milijardi $2
(1[0-9])0000000(\d{2}[\.]) $1 milijardi $2
(1[0-9])000000(\d{3}[\.]) $1 milijardi $2
(1[0-9])00000(\d{4}[\.]) $1 milijardi $2
(1[0-9])0000(\d{5}[\.]) $1 milijardi $2
(1[0-9])000(\d{6}[\.]) $1 milijardi $2
(1[0-9])00(\d{7}[\.]) $1 milijardi $2
(1[0-9])0(\d{8}[\.]) $1 milijardi $2
(1[0-9])(\d{9}[\.]) $1 milijardi $2
([2378])0000000000[\.] $1desetmilijarditi
40000000000[\.] četrdesetmilijarditi
50000000000[\.] pedesetmilijarditi
60000000000[\.] šezdesetmilijarditi
90000000000[\.] devedesetmilijarditi
([2-9]0)00000000(\d[\.]) $1 milijardi $2
([2-9]0)0000000(\d{2}[\.]) $1 milijardi $2
([2-9]0)000000(\d{3}[\.]) $1 milijardi $2
([2-9]0)00000(\d{4}[\.]) $1 milijardi $2
([2-9]0)0000(\d{5}[\.]) $1 milijardi $2
([2-9]0)000(\d{6}[\.]) $1 milijardi $2
([2-9]0)00(\d{7}[\.]) $1 milijardi $2
([2-9]0)0(\d{8}[\.]) $1 milijardi $2
([2-9]0)(\d{9}[\.]) $1 milijardi $2
([2378])1000000000[\.] $1desetjednumilijarditi
41000000000[\.] četrdesetjednumilijarditi
51000000000[\.] pedesetjednumilijarditi
61000000000[\.] šezdesetjednumilijarditi
91000000000[\.] devedesetjednumilijarditi
([2378])100000000(\d[\.]) $1deset jednu milijardu $2
4100000000(\d[\.]) četrdeset jednu milijardu $1
5100000000(\d[\.]) pedeset jednu milijardu $1
6100000000(\d[\.]) šezdeset milijardu $1
9100000000(\d[\.]) devedeset jednu milijardu $1
([2378])10000000(\d{2}[\.]) $1deset jednu milijardu $2
410000000(\d{2}[\.]) četrdeset jednu milijardu $1
510000000(\d{2}[\.]) pedeset jednu milijardu $1
610000000(\d{2}[\.]) šezdeset jednu milijardu $1
910000000(\d{2}[\.]) devedeset jednu milijardu $1
([2378])1000000(\d{3}[\.]) $1deset jednu milijardu $2
41000000(\d{3}[\.]) četrdeset jednu milijardu $1
51000000(\d{3}[\.]) pedeset jednu milijardu $1
61000000(\d{3}[\.]) šezdeset jednu milijardu $1
91000000(\d{3}[\.]) devedeset jednu milijardu $1
([2378])100000(\d{4}[\.]) $1deset jednu milijardu $2
4100000(\d{4}[\.]) četrdeset jednu milijardu $1
5100000(\d{4}[\.]) pedeset jednu milijardu $1
6100000(\d{4}[\.]) šezdeset jednu milijardu $1
9100000(\d{4}[\.]) devedeset jednu milijardu $1
([2378])10000(\d{5}[\.]) $1deset jednu milijardu $2
410000(\d{5}[\.]) četrdeset jednu milijardu $1
510000(\d{5}[\.]) pedeset jednu milijardu $1
610000(\d{5}[\.]) šezdeset jednu milijardu $1
910000(\d{5}[\.]) devedeset jednu milijardu $1
([2378])1000(\d{6}[\.]) $1deset jednu milijardu $2
41000(\d{6}[\.]) četrdeset jednu milijardu $1
51000(\d{6}[\.]) pedeset jednu milijardu $1
61000(\d{6}[\.]) šezdeset jednu milijardu $1
91000(\d{6}[\.]) devedeset jednu milijardu $1
([2378])100(\d{7}[\.]) $1deset jednu milijardu $2
4100(\d{7}[\.]) četrdeset jednu milijardu $1
5100(\d{7}[\.]) pedeset jednu milijardu $1
6100(\d{7}[\.]) šezdeset jednu milijardu $1
9100(\d{7}[\.]) devedeset jednu milijardu $1
([2378])10(\d{8}[\.]) $1deset jednu milijardu $2
410(\d{8}[\.]) četrdeset jednu milijardu $1
510(\d{8}[\.]) pedeset jednu milijardu $1
610(\d{8}[\.]) šezdeset jednu milijardu $1
910(\d{8}[\.]) devedeset jednu milijardu $1
([2378])1(\d{9}[\.]) $1deset jednu milijardu $2
41(\d{9}[\.]) četrdeset jednu milijardu $1
51(\d{9}[\.]) pedeset jednu milijardu $1
61(\d{9}[\.]) šezdeset jednu milijardu $1
91(\d{9}[\.]) devedeset jednu milijardu $1
([2378])2000000000[\.] $1desetdvijemilijarditi
42000000000[\.] četrdesetdvijemilijarditi
52000000000[\.] pedesetdvijemilijarditi
62000000000[\.] šezdesetdvijemilijarditi
92000000000[\.] devedesetdvijemilijarditi
([2378])200000000(\d[\.]) $1deset dvije milijarde $2
4200000000(\d[\.]) četrdeset dvije milijarde $1
5200000000(\d[\.]) pedeset dvije milijarde $1
6200000000(\d[\.]) šezdeset dvije milijarde $1
9200000000(\d[\.]) devedeset dvije milijarde $1
([2378])20000000(\d{2}[\.]) $1deset dvije milijarde $2
420000000(\d{2}[\.]) četrdeset dvije milijarde $1
520000000(\d{2}[\.]) pedeset dvije milijarde $1
620000000(\d{2}[\.]) šezdeset dvije milijarde $1
920000000(\d{2}[\.]) devedeset dvije milijarde $1
([2378])2000000(\d{3}[\.]) $1deset dvije milijarde $2
42000000(\d{3}[\.]) četrdeset dvije milijarde $1
52000000(\d{3}[\.]) pedeset dvije milijarde $1
62000000(\d{3}[\.]) šezdeset dvije milijarde $1
92000000(\d{3}[\.]) devedeset dvije milijarde $1
([2378])200000(\d{4}[\.]) $1deset dvije milijarde $2
4200000(\d{4}[\.]) četrdeset dvije milijarde $1
5200000(\d{4}[\.]) pedeset dvije milijarde $1
6200000(\d{4}[\.]) šezdeset dvije milijarde $1
9200000(\d{4}[\.]) devedeset dvije milijarde $1
([2378])20000(\d{5}[\.]) $1deset dvije milijarde $2
420000(\d{5}[\.]) četrdeset dvije milijarde $1
520000(\d{5}[\.]) pedeset dvije milijarde $1
620000(\d{5}[\.]) šezdeset dvije milijarde $1
920000(\d{5}[\.]) devedeset dvije milijarde $1
([2378])2000(\d{6}[\.]) $1deset dvije milijarde $2
42000(\d{6}[\.]) četrdeset dvije milijarde $1
52000(\d{6}[\.]) pedeset dvije milijarde $1
62000(\d{6}[\.]) šezdeset dvije milijarde $1
92000(\d{6}[\.]) devedeset dvije milijarde $1
([2378])200(\d{7}[\.]) $1deset dvije milijarde $2
4200(\d{7}[\.]) četrdeset dvije milijarde $1
5200(\d{7}[\.]) pedeset dvije milijarde $1
6200(\d{7}[\.]) šezdeset dvije milijarde $1
9200(\d{7}[\.]) devedeset dvije milijarde $1
([2378])20(\d{8}[\.]) $1deset dvije milijarde $2
420(\d{8}[\.]) četrdeset dvije milijarde $1
520(\d{8}[\.]) pedeset dvije milijarde $1
620(\d{8}[\.]) šezdeset dvije milijarde $1
920(\d{8}[\.]) devedeset dvije milijarde $1
([2378])2(\d{9}[\.]) $1deset dvije milijarde $2
42(\d{9}[\.]) četrdeset dvije milijarde $1
52(\d{9}[\.]) pedeset dvije milijarde $1
62(\d{9}[\.]) šezdeset dvije milijarde $1
92(\d{9}[\.]) devedeset dvije milijarde $1
([2378])([34])000000000[\.] $1deset$2milijarditi
4([34])000000000[\.] četrdeset$2milijarditi
5([34])000000000[\.] pedeset$2milijarditi
6([34])000000000[\.] šezdeset$2milijarditi
9([34])000000000[\.] devedeset$2milijarditi
([2378])([34])00000000(\d[\.]) $1deset $2 milijarde $3
4([34])00000000(\d[\.]) četrdeset $1 milijarde $2
5([34])00000000(\d[\.]) pedeset $1 milijarde $2
6([34])00000000(\d[\.]) šezdeset $1 milijarde $2
9([34])00000000(\d[\.]) devedeset $1 milijarde $2
([2378])([34])0000000(\d{2}[\.]) $1deset $2 milijarde $3
4([34])0000000(\d{2}[\.]) četrdeset $1 milijarde $2
5([34])0000000(\d{2}[\.]) pedeset $1 milijarde $2
6([34])0000000(\d{2}[\.]) šezdeset $1 milijarde $2
9([34])0000000(\d{2}[\.]) devedeset $1 milijarde $2
([2378])([34])000000(\d{3}[\.]) $1deset $2 milijarde $3
4([34])000000(\d{3}[\.]) četrdeset $1 milijarde $2
5([34])000000(\d{3}[\.]) pedeset $1 milijarde $2
6([34])000000(\d{3}[\.]) šezdeset $1 milijarde $2
9([34])000000(\d{3}[\.]) devedeset $1 milijarde $2
([2378])([34])00000(\d{4}[\.]) $1deset $2 milijarde $3
4([34])00000(\d{4}[\.]) četrdeset $1 milijarde $2
5([34])00000(\d{4}[\.]) pedeset $1 milijarde $2
6([34])00000(\d{4}[\.]) šezdeset $1 milijarde $2
9([34])00000(\d{4}[\.]) devedeset $1 milijarde $2
([2378])([34])0000(\d{5}[\.]) $1deset $2 milijarde $3
4([34])0000(\d{5}[\.]) četrdeset $1 milijarde $2
5([34])0000(\d{5}[\.]) pedeset $1 milijarde $2
6([34])0000(\d{5}[\.]) šezdeset $1 milijarde $2
9([34])0000(\d{5}[\.]) devedeset $1 milijarde $2
([2378])([34])000(\d{6}[\.]) $1deset $2 milijarde $3
4([34])000(\d{6}[\.]) četrdeset $1 milijarde $2
5([34])000(\d{6}[\.]) pedeset $1 milijarde $2
6([34])000(\d{6}[\.]) šezdeset $1 milijarde $2
9([34])000(\d{6}[\.]) devedeset $1 milijarde $2
([2378])([34])00(\d{7}[\.]) $1deset $2 milijarde $3
4([34])00(\d{7}[\.]) četrdeset $1 milijarde $2
5([34])00(\d{7}[\.]) pedeset $1 milijarde $2
6([34])00(\d{7}[\.]) šezdeset $1 milijarde $2
9([34])00(\d{7}[\.]) devedeset $1 milijarde $2
([2378])([34])0(\d{8}[\.]) $1deset $2 milijarde $3
4([34])0(\d{8}[\.]) četrdeset $1 milijarde $2
5([34])0(\d{8}[\.]) pedeset $1 milijarde $2
6([34])0(\d{8}[\.]) šezdeset $1 milijarde $2
9([34])0(\d{8}[\.]) devedeset $1 milijarde $2
([2378])([34])(\d{9}[\.]) $1deset $2 milijarde $3
4([34])(\d{9}[\.]) četrdeset $1 milijarde $2
5([34])(\d{9}[\.]) pedeset $1 milijarde $2
6([34])(\d{9}[\.]) šezdeset $1 milijarde $2
9([34])(\d{9}[\.]) devedeset $1 milijarde $2
([2378])([5-9])000000000[\.] $1deset$2milijarditi
4([5-9])000000000[\.] četrdeset$2milijarditi
5([5-9])000000000[\.] pedeset$2milijarditi
6([5-9])000000000[\.] šezdeset$2milijarditi
9([5-9])000000000[\.] devedeset$2milijarditi
([2378])([5-9])00000000(\d[\.]) $1deset $2 milijardi $3
4([5-9])00000000(\d[\.]) četrdeset $1 milijardi $2
5([5-9])00000000(\d[\.]) pedeset $1 milijardi $2
6([5-9])00000000(\d[\.]) šezdeset $1 milijardi $2
9([5-9])00000000(\d[\.]) devedeset $1 milijardi $2
([2378])([5-9])0000000(\d{2}[\.]) $1deset $2 milijardi $3
4([5-9])0000000(\d{2}[\.]) četrdeset $1 milijardi $2
5([5-9])0000000(\d{2}[\.]) pedeset $1 milijardi $2
6([5-9])0000000(\d{2}[\.]) šezdeset $1 milijardi $2
9([5-9])0000000(\d{2}[\.]) devedeset $1 milijardi $2
([2378])([5-9])000000(\d{3}[\.]) $1deset $2 milijardi $3
4([5-9])000000(\d{3}[\.]) četrdeset $1 milijardi $2
5([5-9])000000(\d{3}[\.]) pedeset $1 milijardi $2
6([5-9])000000(\d{3}[\.]) šezdeset $1 milijardi $2
9([5-9])000000(\d{3}[\.]) devedeset $1 milijardi $2
([2378])([5-9])00000(\d{4}[\.]) $1deset $2 milijardi $3
4([5-9])00000(\d{4}[\.]) četrdeset $1 milijardi $2
5([5-9])00000(\d{4}[\.]) pedeset $1 milijardi $2
6([5-9])00000(\d{4}[\.]) šezdeset $1 milijardi $2
9([5-9])00000(\d{4}[\.]) devedeset $1 milijardi $2
([2378])([5-9])0000(\d{5}[\.]) $1deset $2 milijardi $3
4([5-9])0000(\d{5}[\.]) četrdeset $1 milijardi $2
5([5-9])0000(\d{5}[\.]) pedeset $1 milijardi $2
6([5-9])0000(\d{5}[\.]) šezdeset $1 milijardi $2
9([5-9])0000(\d{5}[\.]) devedeset $1 milijardi $2
([2378])([5-9])000(\d{6}[\.]) $1deset $2 milijardi $3
4([5-9])000(\d{6}[\.]) četrdeset $1 milijardi $2
5([5-9])000(\d{6}[\.]) pedeset $1 milijardi $2
6([5-9])000(\d{6}[\.]) šezdeset $1 milijardi $2
9([5-9])000(\d{6}[\.]) devedeset $1 milijardi $2
([2378])([5-9])00(\d{7}[\.]) $1deset $2 milijardi $3
4([5-9])00(\d{7}[\.]) četrdeset $1 milijardi $2
5([5-9])00(\d{7}[\.]) pedeset $1 milijardi $2
6([5-9])00(\d{7}[\.]) šezdeset $1 milijardi $2
9([5-9])00(\d{7}[\.]) devedeset $1 milijardi $2
([2378])([5-9])0(\d{8}[\.]) $1deset $2 milijardi $3
4([5-9])0(\d{8}[\.]) četrdeset $1 milijardi $2
5([5-9])0(\d{8}[\.]) pedeset $1 milijardi $2
6([5-9])0(\d{8}[\.]) šezdeset $1 milijardi $2
9([5-9])0(\d{8}[\.]) devedeset $1 milijardi $2
([2378])([5-9])(\d{9}[\.]) $1deset $2 milijardi $3
4([5-9])(\d{9}[\.]) četrdeset $1 milijardi $2
5([5-9])(\d{9}[\.]) pedeset $1 milijardi $2
6([5-9])(\d{9}[\.]) šezdeset $1 milijardi $2
9([5-9])(\d{9}[\.]) devedeset $1 milijardi $2
100000000000[\.] stomilijarditi
10000000000(\d{1}[\.]) sto milijardi $1
1000000000(\d{2}[\.]) sto milijardi $1
100000000(\d{3}[\.]) sto milijardi $1
10000000(\d{4}[\.]) sto milijardi $1
1000000(\d{5}[\.]) sto milijardi $1
100000(\d{6}[\.]) sto milijardi $1
10000(\d{7}[\.]) sto milijardi $1
1000(\d{8}[\.]) sto milijardi $1
100(\d{9}[\.]) sto milijardi $1
10(\d{10}[\.]) sto milijardi $1
1(\d{11}[\.]) sto milijardi $1
200000000000[\.] dvjestomilijarditi
20000000000(\d{1}[\.]) dvjesto milijardi $1
2000000000(\d{2}[\.]) dvjesto milijardi $1
200000000(\d{3}[\.]) dvjesto milijardi $1
20000000(\d{4}[\.]) dvjesto milijardi $1
2000000(\d{5}[\.]) dvjesto milijardi $1
200000(\d{6}[\.]) dvjesto milijardi $1
20000(\d{7}[\.]) dvjesto milijardi $1
2000(\d{8}[\.]) dvjesto milijardi $1
200(\d{9}[\.]) dvjesto milijardi $1
20(\d{10}[\.]) dvjesto milijardi $1
2(\d{11}[\.]) dvjesto milijardi $1
([3-57-9])00000000000[\.] $1stomilijarditi
([3-57-9])0000000000(\d{1}[\.]) $1 milijardi $2
([3-57-9])000000000(\d{2}[\.]) $1 milijardi $2
([3-57-9])00000000(\d{3}[\.]) $1 milijardi $2
([3-57-9])0000000(\d{4}[\.]) $1 milijardi $2
([3-57-9])000000(\d{5}[\.]) $1 milijardi $2
([3-57-9])00000(\d{6}[\.]) $1 milijardi $2
([3-57-9])0000(\d{7}[\.]) $1 milijardi $2
([3-57-9])000(\d{8}[\.]) $1 milijardi $2
([3-57-9])00(\d{9}[\.]) $1 milijardi $2
([3-57-9])0(\d{10}[\.]) $1 milijardi $2
([3-57-9])(\d{11}[\.]) $1 milijardi $2
600000000000[\.] šestomilijarditi
60000000000(\d{1}[\.]) šesto milijardi $1
6000000000(\d{2}[\.]) šesto milijardi $1
600000000(\d{3}[\.]) šesto milijardi $1
60000000(\d{4}[\.]) šesto milijardi $1
6000000(\d{5}[\.]) šesto milijardi $1
600000(\d{6}[\.]) šesto milijardi $1
60000(\d{7}[\.]) šesto milijardi $1
6000(\d{8}[\.]) šesto milijardi $1
600(\d{9}[\.]) šesto milijardi $1
60(\d{10}[\.]) šesto milijardi $1
6(\d{11}[\.]) šesto milijardi $1

"""