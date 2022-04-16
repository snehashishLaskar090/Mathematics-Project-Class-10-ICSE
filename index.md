# Maths Project

### In this project I will be exploring how Mathematical Thinking can be simulated with Computer Science. In this Maths Project I will not be dvelving very deep into Mathematics. I will just be simultaing Mathematical think using python code. This Project will look into:
#
1. Simulating how humans solve linear equations in one variable

2. Simulating how humans can solve linear equations in two variables

3. Simulating how humans can solve Quadratic equations in one variable

4. How code can be used for commercial Mathematics

5. How code can be used for statistics


#
## Simulating Linear Equations in one variable :
#
### First we start by Defining an Object called Term. Each term in an equation is represented using this speceifc Object. A term has: (a) sign, (b) numerical co-efficient and (C) a variable In terms where the term is not a vaiable value, the variable is left empty. This how humans represent each term of a Equation. Here is code for the object Term:
```python
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
        
        self.num_coef = num_coef # Numerical Co-eficient of the term
        self.variable = variable # Variable value of the term
        self.sign = sign # Sign of the Term

        self.rep = self.sign + str(self.num_coef) + self.variable # A way to bring all these Values into 1. Eg: -5x 

    # A function to change the sign of the term when we bring the term from
    # The LHS to the RHS
    def changeSign(self):
        if self.sign == "+":
            self.sign = "-"

        elif self.sign == "-":
            self.sign = "+"

    def __str__(self):
        self.rep = self.sign + str(self.num_coef) + self.variable
        return self.rep



```

### Next we define a way to represent each eqution. This object of represenation of an equation takes in two parameters. It takes in an LHS which is a list / array of the Term objects we defined before. This Eqution object can represent an equation and can also 




```python
class Equation:

    def __init__(self, LHS: list, RHS: list):
        self.LHS = LHS # L.H.S of the Equation
        self.RHS = RHS# R.H.S of the Equatio
        
        # A way to represent the entire equation. for example: 3x - 4 = 10
        self.eqaution = f"{[i.rep for i in LHS]} = {[j.rep for j in RHS]}"

```
### Now that we have an Equation we can move further in terms of how a human would aproch this problem. In the standard way the human would bring all the variables to one side of the Equation and bring all the constants to the other side of of the equation. So lets go ahead and do the same with a function that we will call factorize. 

```python
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
```