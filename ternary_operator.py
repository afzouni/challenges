def operator(cond, st_true, st_false): 
    return ((not not cond) * st_true + (not cond) * st_false) 

x = 15
res = operator(x >10, "true", "false") 
print(res)

x = 5
res = operator(x >10, "true", "false") 
print(res)