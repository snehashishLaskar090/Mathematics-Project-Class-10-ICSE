# Creating a class term


from email.contentmanager import raw_data_manager


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
        self.constant = int(str(self.sign) + str(self.num_coef))
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
                i.rep = i.sign + str(i.num_coef) + i.variable
                self.LHS.append(i)
                self.eqaution = f"{[i.rep for i in self.LHS]} = {[j.rep for j in self.RHS]}"
                
        # return self.eqaution

        previous_var = ""
        for i in self.LHS:

            if self.LHS.index(i) == 0:
                previous_var = i

            elif i.variable == previous_var:

                present_index = self.LHS.index(i)
                previous_term = self.LHS[present_index-1]

                constant  = int(previous_term.sign + previous_term.num_coef)
                present_constant = int(i.sign + i.num_coef)

                new_constant = constant + present_constant

                sign = "+"

                if new_constant < 0:
                    sign = "-"

                new_term = Term(str(new_constant*1), i.variable, sign)
                
                self.LHS.remove(self.LHS[present_index])
                self.LHS[present_index-1] = new_term

                self.eqaution = f"{[i.rep for i in self.LHS]} = {[j.rep for j in self.RHS]}"
                print(self.eqaution)

            else:
                previous_var = i.variable
       

        # Main Core Of Algorithm

        product = self.LHS[0].constant * self.LHS[-1].constant
        middle = self.LHS[1].constant
        print(middle)
        mid_var = self.LHS[1].variable

        num1 = 0
        num2 = 0


        for i in range(product):
            for j in range(product):
                if i + j == middle or i - j == middle:
                    if i != 0 and j != 0:
                        num1 = i
                        num2 = j

                        break

        print(num1, num2)

        if num1 - num2 == middle:

            sign = "+"
            if num1 < 0:
                sign = "-"

            term = Term(str(num1), mid_var, sign)
            term2 = Term(str(num2), mid_var, "-")
            print(term)
            print(term2)
            self.LHS.remove(self.LHS[1])
            
            prev = self.LHS[-1]
            self.LHS.remove(self.LHS[-1])

            self.LHS.append(term)
            self.LHS.append(term2)
            self.LHS.append(prev)

            print([i.rep for i in self.LHS])

        elif num1 + num2 == middle:

            sign = "+"
            if num1 < 0:
                sign = "-"

            term = Term(str(num1), mid_var, sign)
            term2 = Term(str(num2), mid_var, "+")

            self.LHS.remove(self.LHS[1])
            
            prev = self.LHS[-1]
            self.LHS.remove(self.LHS[-1])

            self.LHS.append(term)
            self.LHS.append(term2)
            self.LHS.append(prev)

            print([i for i in self.LHS])

        
equa = Equation([Term("1", "x^2", "+"), Term("3", "x", "-"), Term("2", "", "+")], [])
equa.factorize()




            






    


