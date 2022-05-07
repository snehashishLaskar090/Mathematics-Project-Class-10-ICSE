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


class equation:

    def __init__(self, LHS: list, RHS: list):
        self.LHS = LHS
        self.RHS = RHS

        self.eqaution = f"{[i.rep for i in LHS]} = {[j.rep for j in RHS]}"

    def factorize(self):

        for i in self.LHS:
            if i.variable == "":
                self.LHS.remove(i)
                i.changeSign()
                self.RHS.append(i)


        for j in self.RHS:
            if j.variable != "":
                self.RHS.remove(j)
                j.changeSign()
                self.LHS.append(j)

        self.eqaution = f"{[i.rep for i in self.LHS]} = {[j.rep for j in self.RHS]}"

        return self.eqaution

    def Solve(self):
        sum = 0
        for i in self.RHS:
            sum += float(i.sign + i.num_coef)

        variable = None
        sum2 = 0
        for i in self.LHS:
            sum2 += float(i.sign + str(i.num_coef))
            variable = i.variable

        return sum/sum2
# Here the equation given is 2x + 5 = 10 + x
# Answer using human mind  = 5
# Run the program and see if the result is the same :)

firstEqua = equation([Term("1", "x", "+"), Term("17.5", "x", "-")], [Term("63", "", "-"), Term("11","", "-")])


