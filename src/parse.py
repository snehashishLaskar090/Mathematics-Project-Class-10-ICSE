from quadratic import Term, Equation

lhs = []
rhs = []
mystring = "2x^2 + 2x - 1 = 0" 
string = mystring.split("=")[0]
string2 = mystring.split("=")[1]
if string2 != ["0"]:
    rhs = []
    
split = string.split()
for i in split:
    try:
        int(i)
        sign = split[split.index(i)-1]

        term = Term(str(i), "",sign)
        lhs.append(term)
    except:
        num = ""
        var = ""
        if "+" != i and i != "-":
            split2 = [j for j in i ]


            for j in split2:
                
                try:
                    int(j)
                    num += j

                except:

                    i:j
                    var = i
                    break
            sign = "+"
            if i  == split[0]:
                sign = "+"

            elif i != split[0]:
                sign = split[split.index(i)-1]
            term = Term(num, var, sign)

            lhs.append(term)

print([i.rep for i in lhs])

