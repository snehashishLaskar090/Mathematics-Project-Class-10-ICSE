# Creating a class term

from variable1 import equation as equ

# A function to calcultate lcm of two numbers
def Lcm(x, y):
    greater = max(x,y)

    while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1

    return lcm


# A class Term To represent every term in an equation
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
        self.constant = float(str(self.sign) + str(self.num_coef))
        self.rep = self.sign + str(self.num_coef) + self.variable

    def changeSign(self):
        if self.sign == "+":
            self.sign = "-"

        elif self.sign == "-":
            self.sign = "+"

    def __str__(self):
        self.rep = self.sign + str(self.num_coef) + self.variable
        return self.rep


# A class to represent every equation
class Equation:

    def __init__(self, LHS: list, RHS: list):
        self.LHS = LHS
        self.RHS = RHS

        self.eqaution = f"{[i.rep for i in LHS]} = {[j.rep for j in RHS]}"

    def factorize(self):

        print("\n","---------------Solution----------------", "\n")

        if len(self.RHS) != 0:

            for i in self.RHS:

                self.RHS.remove(i)
                i.changeSign()
                i.rep = i.sign + str(i.num_coef) + i.variable
                self.LHS.append(i)
                self.eqaution = f"{[i.rep for i in self.LHS]} = {[j.rep for j in self.RHS]}"
                
        # return self.eqaution
        print("=>" ,self.eqaution, "\n")

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
    
            else:
                previous_var = i.variable
       

        # Main Core Of Algorithm

        product = int(self.LHS[0].constant * self.LHS[-1].constant)
        middle = self.LHS[1].constant
        mid_var = self.LHS[1].variable

        num1 = 0
        num2 = 0

        
        if product < 0:
            
            for i in range(product, -product):
                for j in range(product, -product):
                    if i + j == middle or  i-j == middle:
                        if i*j == product:
                            num1 = i
                            num2 = j

        elif product > 0:

            
            for i in range(product):
                for j in range(product):
                    if i + j == -middle:
                        if i*j == product:
                            num1 = -i
                            num2 = -j
 

        if num1 - num2 == middle:

            sign = "+"
            if num1 < 0:
                sign = "-"

            sign2 = "+"
            if num2 > num1:
                sign2 = "-"

            term = Term(str(num1), mid_var, sign)
            term2 = Term(str(num2), mid_var, sign2)

            self.LHS.remove(self.LHS[1])
            
            prev = self.LHS[-1]
            self.LHS.remove(self.LHS[-1])

            self.LHS.append(term)
            self.LHS.append(term2)
            self.LHS.append(prev)


            left_constant1 = int(self.LHS[0].constant)
            left_constant2 = int(self.LHS[1].constant)
            right_constant1 = int(self.LHS[2].constant)
            right_constant2 = int(self.LHS[3].constant)

            
            def compute_hcf(num1, num2):
                def gcf(x, y):
                # choose the smaller number
                    smaller = 0
                    hcf = 0
                    if x > y:
                        smaller = y
                    else:
                        smaller = x
                    for i in range(1, smaller+1):
                        if((x % i == 0) and (y % i == 0)):
                            hcf = i 
                    return hcf

                if num1 < 0 and num2 < 0:
                    # maxim = max(num1, num2)
                    num1 = -num1
                    num2 = -num2
                    ans = gcf(num1, num2)
                    result = -ans
                    return result

                elif num1> 0 and num2> 0:
                    return gcf(num1, num2)

            # left_common = compute_hcf(left_constant1, left_constant2)
            # right_common = -compute_hcf(-right_constant1, right_constant2)
            left_common = compute_hcf(left_constant1, left_constant2)

    
            if left_constant1 < 0 and left_constant2 > 0:

                left_common = compute_hcf(-left_constant1, left_constant2)

            elif left_constant1 > 0 and left_constant2 < 0:
                left_common = compute_hcf(left_constant1, -left_constant2)

            if right_constant1 < 0 and right_constant2 < 0:
                right_common = compute_hcf(right_constant1, right_constant2)

            elif right_constant1 < 0 and right_constant2 > 0:
                right_common = -compute_hcf(-right_constant1, right_constant2)

            elif right_constant1 > 0 and right_constant2 < 0:
                right_common = -compute_hcf(right_constant1, -right_constant2)

            left_side = [self.LHS[0], self.LHS[1]]
            right_side = [self.LHS[2], self.LHS[3]] 

            left_var = ""
            right_var = ""
      
            
            for i in left_side:
                i.constant = int(i.constant)
                i.constant /= left_common
                if "^2" in left_side[0].variable:

                    left_sign = "+"
                    if left_common < 0:
                        left_sign = "-"
                        new_left_common = -left_common
                    else:
                        new_left_common =left_common


                    left_side[0].variable = left_side[1].variable
                    left_side[1].variable = ""
                    left_var = Term(str(new_left_common), left_side[0].variable, left_sign)
                    
                i.rep = str(i.constant)+i.variable


            for i in right_side:
                i.constant = int(i.constant)

                i.constant /= right_common

        
                i.rep = str(i.constant)+ i.variable

                right_sign = "+"
                if right_common < 0:
                    right_sign = "-"
                    new_right_common = -right_common
                right_var = Term(str(new_right_common), right_side[-1].variable, right_sign)
      

            equation1 = [i.rep for i in left_side]
            equation2 = [i.rep for i in right_side]

            factor_equa = [left_var, right_var]
            if equation1 == equation2:

                root1 = equ(left_side, [])
                root1.factorize()
                ans1 = root1.Solve()

                root2 = equ(factor_equa, [])
                root2.factorize()
                ans2 = root2.Solve()
                
          
            else:
                print("error")


        elif num1 + num2 == middle:

            sign = "+"
            if num1 < 0:
                sign = "-"
                num1 = -num1

            sign2 = "+"
            if num2 < 0:
                sign2 = "-"
                num2 = -num2
            
            term = Term(str(num1), mid_var, sign)
            term2 = Term(str(num2), mid_var, sign2)

            self.LHS.remove(self.LHS[1])
            
            prev = self.LHS[-1]
            self.LHS.remove(self.LHS[-1])

            self.LHS.append(term)
            self.LHS.append(term2)
            self.LHS.append(prev)
            self.eqaution = f"{[i.rep for i in self.LHS]} = {[j.rep for j in self.RHS]}"

            print("=>" ,self.eqaution, "\n")
            left_constant1 = int(self.LHS[0].constant)
            left_constant2 = int(self.LHS[1].constant)
            right_constant1 = int(self.LHS[2].constant)
            right_constant2 = int(self.LHS[3].constant)

            
            def compute_hcf(num1, num2):
                def gcf(x, y):
                # choose the smaller number
                    smaller = 0
                    hcf = 0
                    if x > y:
                        smaller = y
                    else:
                        smaller = x
                    for i in range(1, smaller+1):
                        if((x % i == 0) and (y % i == 0)):
                            hcf = i 
                    return hcf

                if num1 < 0 and num2 < 0:
                    # maxim = max(num1, num2)
                    num1 = -num1
                    num2 = -num2
                    ans = gcf(num1, num2)
                    result = -ans
                    return result

                elif num1> 0 and num2> 0:
                    return gcf(num1, num2)

            left_common = compute_hcf(left_constant1, left_constant2)

    
            if left_constant1 < 0 and left_constant2 > 0:

                left_common = compute_hcf(-left_constant1, left_constant2)

            elif left_constant1 > 0 and left_constant2 < 0:
                left_common = compute_hcf(left_constant1, -left_constant2)

            if right_constant1 < 0 and right_constant2 < 0:
                right_common = compute_hcf(right_constant1, right_constant2)

            elif right_constant1 < 0 and right_constant2 > 0:
                right_common = -compute_hcf(-right_constant1, right_constant2)

            elif right_constant1 > 0 and right_constant2 < 0:
                right_common = -compute_hcf(right_constant1, -right_constant2)
           
            
                       

            left_side = [self.LHS[0], self.LHS[1]]
            right_side = [self.LHS[2], self.LHS[3]] 
            
            left_var = ""
            right_var = ""
      
            
            for i in left_side:
                i.constant = int(i.constant)
                i.constant /= left_common
                if "^2" in left_side[0].variable:

                    left_sign = "+"
                    if left_common < 0:
                        left_sign = "-"
                        new_left_common = -left_common
                    else:
                        new_left_common =left_common


                    left_side[0].variable = left_side[1].variable
                    left_side[1].variable = ""
                    left_var = Term(str(new_left_common), left_side[0].variable, left_sign)
                    
                i.rep = str(i.constant)+i.variable


            for i in right_side:
                i.constant = int(i.constant)

                i.constant /= right_common

        
                i.rep = str(i.constant)+ i.variable

                right_sign = "+"
                if right_common < 0:
                    right_sign = "-"
                    new_right_common = -right_common
                right_var = Term(str(new_right_common), right_side[-1].variable, right_sign)
      

            equation1 = [i.rep for i in left_side]
            equation2 = [i.rep for i in right_side]
            print("=>",left_var.rep ,equation1, right_var.rep, equation2, " = []\n")
            factor_equa = [left_var, right_var]

            if equation1 == equation2:
                print("=>",[i.rep for i in factor_equa], equation1, " = []\n")
                root1 = equ(left_side, [])
                root1.factorize()
                ans1 = root1.Solve()

                root2 = equ(factor_equa, [])
                root2.factorize()
                ans2 = root2.Solve()
                print(f"=> roots to your equation are {ans1} and {ans2}\n")
          
            else:
                print(equation1, equation2)

# equa = Equation([Term("1", "x^2", "+"), Term("2", "x", "-"), Term("15", "", "-")], [])
# equa.factorize()

lhs = []
rhs = []
mystring = input("""
Enter A Valid Quadratic Equation Below\n
Pls enter the equation in the format ax^2 + bx + c = 0\n
""") 
string = mystring.split("=")[0]
string2 = mystring.split("=")[1]
split = string.split()
right_split = string2.split()



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

equa = Equation(lhs, rhs)
equa.factorize()









    















































































































