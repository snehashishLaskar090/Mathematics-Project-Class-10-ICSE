# Author: Snehashish Laskar
# Date of Creation : 29/3/22
# Project Subject: Maths
# Project Topic: How mathematics can be simulated with computer science

from variable1 import *
# Creating a class term
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

        elif self.sign == "-":
            self.sign = "+"
        self.rep = self.sign + str(self.num_coef) + self.variable
    def __str__(self):
        self.rep = self.sign + str(self.num_coef) + self.variable
        return self.rep

class Equation:

    def __init__(self, LHS: list, RHS: list):
        self.LHS = LHS
        self.RHS = RHS
        self.variable = None
        self.eqaution = f"{[i.rep for i in LHS]} = {[j.rep for j in RHS]}"

    def factorize(self):
        for i in self.LHS:
            if i.variable == "":
                self.LHS.remove(i)
                i.changeSign()
                self.RHS.append(i)

        for i in self.RHS:
            if i.variable != "":
                self.RHS.remove(i)
                i.changeSign()
                self.LHS.append(i)

    def factorize1(self):
        self.setVariable()
        for i in self.LHS:
            if i.variable != self.variable:
                self.LHS.remove(i)
                i.changeSign()
                self.RHS.append(i)

        if len(self.LHS) != 1:
            Sum = 0
            for i in self.LHS:
                Sum += int(i.num_coef)
                self.LHS.remove(i)

        return [i.rep for i in self.LHS], [i.rep for i in self.RHS]

    def factorize2(self):
        

        for i in self.LHS:
            if self.LHS[-1] != i:
                next = self.LHS[self.LHS.index(i)+1]
                if i.variable == next:
                    next = self.LHS[self.LHS.index(i)+1]
                    self.LHS.remove(i)
                    next.num_coef = str(int(next.num_coef) + int(i.num_coef))

        for i in self.RHS:
            if self.RHS[-1] != i:
                next = self.RHS[self.RHS.index(i)+1]
                if i.variable == next:
                    next = self.RHS[self.RHS.index(i)+1]
                    self.RHS.remove(i)
                    next.num_coef = str(int(next.num_coef) + int(i.num_coef))

        
        return [i.rep for i in self.LHS], [i.rep for i in self.RHS]


    def setVariable(self):
        for i in self.LHS:
            if i.variable != "":
                self.variable = i.variable
                break

    def __str__(self):
        return f"{[i.rep for i in self.LHS]} = {[i.rep for i in self.RHS]}"

equation1 = Equation([Term("1", "x", "+"), Term("7", "y", "-")], [Term("11", "", "-")])
equation2 = Equation([Term("5", "x", "+"), Term("2", "y", "+")], [Term("18", "", "-")])


def solveEquas(equa1, equa2):

    original1 = equa1
    original2 = equa2

    equa1.factorize()
    equa2.factorize()

    print(equa1)
    print(equa2)

    print("\n")

    equa1.setVariable()
    equa2.setVariable()

    equa1.factorize1()
    
    for i in equa2.LHS:
        if i.variable == equa1.variable:
            equa2.LHS.remove(i)
            i.changeSign
            equa2.RHS.append(i)

    var  = equa2.LHS[0].variable
    num = 0
    num_coef = int(equa2.LHS[0].num_coef)

    for i in equa2.RHS:
        i.num_coef = str(float(i.num_coef) / num_coef)
        i.rep  = i.sign + str(i.num_coef) + i.variable

    for i in equa1.RHS:
        if i.variable == var:
            num = int(i.num_coef)
            for i in equa2.RHS:
                i.num_coef = str(float(i.num_coef) * num)
                equa1.RHS.append(i)

            
    for i in equa1.RHS:
        if i.variable == var:
            equa1.RHS.remove(i)

    
    for i in equa1.RHS:
        if i.variable == equa1.LHS[0].variable:
            equa1.RHS.remove(i)
            equa1.LHS.append(i)

    print([i.sign + i.num_coef + i.variable for i in equa1.LHS], " = ",[i.sign + i.num_coef + i.variable for i in equa1.RHS])
    
    # var = equa1.LHS[0].variable
    # sum = 0
    # for i in equa1.LHS:
    #     if i.variable == var:
    #         sum += int(i.num_coef)
    #         equa1.LHS.remove(i)
            
    # sign = "+"
    # if sum < 0:
    #     sign = "-"
    #     sum = -sum
    # print(sum)
    # equa1.LHS.append(Term(var, str(sum), sign ))

    equan = equation(equa1.LHS, equa1.RHS)

    varr1 = equan.Solve()

    myequation = original1
    myequation.factorize()
    for i in myequation.LHS:
        if float(i.num_coef) < 0:
            i.sign = "-"
        else:
            i.sign = "+"

        
        i.num_coef = str(float(i.num_coef) * varr1)


    print([i.sign + i.num_coef + i.variable for i in myequation.LHS], " = ",[i.sign + i.num_coef + i.variable for i in myequation.RHS])
   

 

solveEquas(equation1, equation2)
       

