# Author: Snehashish Laskar
# Date of Creation : 29/3/22
# Project Subject: Maths
# Project Topic: How mathematics can be simulated with computer science


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

    def setVariable(self):
        for i in self.LHS:
            if i.variable != "":
                self.variable = i.variable
                break

    def __str__(self):
        return f"{[i.rep for i in self.LHS]} = {[i.rep for i in self.RHS]}"

equation1 = Equation([Term("1", "x", "+"), Term("7", "y", "-")], [Term("11", "", "-")])
equation2 = Equation([Term("5", "x", "+"), Term("2", "y", "+")], [Term("18", "", "-")])

def SolveTwoEquas(equa1:Equation, equa2:Equation):
    equa1.factorize()
    equa2.setVariable()
    variable = equa1.variable
    print(variable)
    print(equa2.variable)
    if equa1.variable == equa2.variable:
        print("yes")
        for i in equa2.LHS:
            if i.variable != variable and i.variable != "":
                equa2.variable = i.variable
                print(equa2.variable)
                # equa2.factorize()


        for i in equa2.LHS:
            print("yes")
            if i.variable == equa1.variable:
                print("Yes")
                equa2.LHS[equa2.LHS.index(i)].variable = equa1.RHS
                print([i.rep for i in equa2.LHS[equa2.LHS.index(i)].variable])
                num = equa2.LHS[equa2.LHS.index(i)].num_coef

                for i in equa2.LHS[equa2.LHS.index(i)].variable:
                    i.num_coef = str(int(i.num_coef) * int(num))
                    print(i.rep)
    print([i.rep for i in equa2.LHS])


SolveTwoEquas(equation1, equation2)





