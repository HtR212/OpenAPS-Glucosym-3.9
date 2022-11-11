from subprocess import call

p = [7,8,5,6]
for i in range(len(p)):
    call(["python","updated_ct_script_iob_based (closed loop).py",f"{p[i]}"])