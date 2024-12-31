from re import findall
a, b, c, *prog = [int(n) for n in findall("(\d+)", open("day_17.in").read())]

def run(prog, a):
    ip, b, c, out = 0, 0, 0, []
    while ip>=0 and ip<len(prog):
        lit, combo = prog[ip+1], [0,1,2,3,a,b,c,99999][prog[ip+1]]
        match prog[ip]:
            case 0: a = int(a / 2**combo)
            case 1: b = b ^ lit          
            case 2: b = combo % 8        
            case 3: ip = ip if a==0 else lit-2 
            case 4: b = b ^ c                  
            case 5: out.append(combo % 8)      
            case 6: b = int(a / 2**combo)      
            case 7: c = int(a / 2**combo)      
        ip+=2
    return out
print(",".join(str(n) for n in run(prog, a)))
