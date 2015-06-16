#!/usr/bin/python
def not_bad(s):
    if s.find("not")<s.find("bad"):
       s = s.replace("not", "good")
       ret = s.replace(s[s.find("good"):s.find("bad")+3], "good")
    else:
       ret = s    
    return ret
    
print not_bad("moono is not s bad www.")
print not_bad("bad is not so") 
print not_bad("moono bad is not so") 
print not_bad("moono is not so ffff badee.")
