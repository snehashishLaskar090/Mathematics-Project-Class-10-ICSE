# Creating a class term


def Lcm(x, y):
    greater = max(x,y)

    while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1

    return lcm

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

        self.eqaution = f"{[i.rep for i in LHS]} = {[j.rep for j in RHS]}"

    def factorize(self):

        if len(self.RHS) != 0:

            for i in self.RHS:

                self.RHS.remove(i)
                i.changeSign()
                self.LHS.append(i)
            

        self.eqaution = f"{[i.rep for i in self.LHS]} = {[j.rep for j in self.RHS]}"

        return self.eqaution



    def Solve(self):

        for i in self.LHS:

            if i != self.LHS[-1] and i.variable == self.LHS[self.LHS.index(i) + 1]:

                i.num_coef = str(int(i.num_coef) + int(self.LHS[self.LHS.index(i) + 1].num_coef))
                self.LHS.remove(self.LHS[self.LHS.index(i) + 1])


            if len(self.LHS) == 3:

                print("3")
                
                x = int(self.LHS[0].num_coef)
                y = int(self.LHS[-1].num_coef)

                lcm = Lcm(x,y)

                val1  = 0
                val2 = 0

                for x in range(lcm):
                    for j in range(lcm):

                        if x + j == lcm:
                            val1 = x
                            val2 = j

                        elif max(x,j) - min(x,j) == lcm:
                            val1 = x
                            val2 = j

                new = self.LHS[-1]
                self.LHS.remove(self.LHS[-1])
                sign1 = "+"
                if val1 < 0:
                    sign1 = "-"
                self.LHS.append(Term(str(val1), i.variable,sign1 ))
                sign2 = "+"
                if val2 < 0:
                    sign2 = "-"
                self.LHS.append(Term(str(val2), i.variable,sign2) )

                self.LHS.append(new)


        return self.eqaution


equa = Equation([Term("2", "x^2", "+"), Term("6", "x", "-"), Term("8", "", "+")], [])
equa.factorize()
print(equa.Solve())




            






    


