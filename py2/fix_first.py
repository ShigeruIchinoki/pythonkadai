#!/usr/bin/python
def fix_first(s):
   top = s[0]
   nokori = s[1:]
   nokori = nokori.replace(top, '*')
   ret = top + nokori
   return ret

print fix_first("goohihiihle")

