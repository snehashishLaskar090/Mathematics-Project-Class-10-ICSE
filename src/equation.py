# Author: Snehashish Laskar
# Date of Creation : 29/3/22
# Project Subject: Maths
# Project Topic: How mathematics can be simulated with computer science


# Creating a class term
from ast import excepthandler
from operator import eq
from turtle import right


class Term:
    """
    Every term in the given equation is passed a Term class
    in this program. Basically Each Term has a numerical coefficient,
    and a sign. There are variables and constants. In constants the variable
    value  = "", but in variable terms, the variable has a variable letter.
    When humans solve equations, we do something change side change sign. Where we move a term
    from LHS to RHS or from RHS to LHS. When we do that the sign of the term. The changeSign function
    takes care of that.
    """
    def __init__(self, num_coef, variable, sign) -> None:
        self.num_coef = num_coef
        self.variable = variable
        self.sign = sign
        self.rep = self.sign + str(self.num_coef) + self.variable

    def changeSign(self):
        if self.sign == "+":
            self.sign = "-"
            self.rep = self.sign + str(self.num_coef) + self.variable


        elif self.sign == "-":
            self.sign = "+"
            self.rep = self.sign + str(self.num_coef) + self.variable


    def __str__(self):
        self.rep = self.sign + str(self.num_coef) + self.variable
        return self.rep


class equation:

    def __init__(self, LHS: list, RHS: list):
        self.LHS = LHS
        self.RHS = RHS

        self.eqaution = f"{[i.rep for i in LHS]} = {[j.rep for j in RHS]}"

    def factorize(self):

        print("\n----------------------SOLUTION----------------------\n")
        print("=>",[i.rep for i in self.LHS ], "=", [i.rep for i in self.RHS ], "\n")
        for i in self.LHS:
            if i.variable == "":
                self.LHS.remove(i)
                i.changeSign()
                self.RHS.append(i)
                i.rep = i.sign + str(i.num_coef) + i.variable



        for j in self.RHS:
            if j.variable != "":
                self.RHS.remove(j)
                j.changeSign()
                self.LHS.append(j)
                i.rep = i.sign + str(i.num_coef) + i.variable

        self.eqaution = f"{[i.rep for i in self.LHS]} = {[j.rep for j in self.RHS]}"

        print("=>", self.eqaution, "\n")

    def Solve(self):
        sum = 0
        for i in self.RHS:
            sum += float(i.sign + i.num_coef)

        variable = None

        sum2 = 0
        for i in self.LHS:
            sum2 += float(i.sign + str(i.num_coef))
            variable = i.variable
        print("=> ['"+ str(int(sum2)) + variable + "']","=", "['" + str(int(sum)) + "']\n")
        print( "=>", variable, "=",sum/sum2, "\n")

# Here the equation given is 2x + 5 = 10 + 1x
# Answer using human mind  = 5
# Run the program and see if the result is the same :)


lhs = []
rhs = []
mystring = input("""
Enter A Valid Quadratic Equation Below\n
""") 
string = mystring.split("=")[0]
string2 = mystring.split("=")[1]
split = string.split()
right_split = string2.split()

for i in right_split:
    try:
        int(i)
        if right_split[0] == i:
            term = Term(str(i), "", "+")
            rhs.append(term)
        else:
            sign = right_split[right_split.index(i)-1]
            term = Term(str(i), "", sign)
            rhs.append(term)

    except:
        num = ""
        var = ""
        print(right_split)
        if "+" != i and "-" != i:
    
            split2 = [j for j in i ]

            last = right_split[right_split.index(i)-1]
            for j in split2:
                try:
                    int(j)
                    num = j
                    
                    var = i.split(j)[1]
                    break
                    
                except:
                
                    break
        
            term = Term(str(num), var, last )
            print(term.rep)
            rhs.append(term)

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
                    var = i.split(j)[1]
                except:

                    break

            sign = "+"
            if i  == split[1]:
                sign = "+"

            elif i != split[0]:
                sign = split[split.index(i)-1]
            
            term = Term(num, var, sign)

            lhs.append(term)

equa = equation(lhs, rhs)
equa.factorize()
equa.Solve()