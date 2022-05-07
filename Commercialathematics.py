# Author: Snehashish Laskar
# Date : 18-04-2022

"""

Commercial Mathematics Topics being covered:
1) Simple Interest
2) Compound Interest
3) Reccuring Deposit
4) GST
5) Banking
6) Shares and dividends

"""


# First we will takle Simple Interest

def SimpleInterest(principle:int=0, time:int=0, rate=0, amount:int=0, interest:int=0):

    # This function Implements the Formula : I = (P x R x T)/100
    
    if principle != 0 and time != 0 and  rate != 0 and amount == 0 and interest == 0:

        interest = (principle*rate*time)
        amount  = principle + interest

        return interest

    # Now if interest is given and principle is not given and we are asked to find principle we use this
    
    elif principle == 0 and time != 0 and  rate != 0 and amount == 0 and interest != 0:

        print("find time")
        principle = interest * 100 / (rate * time)
        amount  = interest + principle
        
        return principle

    # Now if interest is given and the time is not given, then we use this to find the value of the time variable

    elif principle != 0  and time == 0 and rate != 0 and amount == 0 and interest  != 0:

        time = interest * 100 / (principle * rate)
        amount = interest + principle

        return time

    # Now if the interest is given and the rate is not given, then this is the way to 

    elif principle != 0 and time != 0 and  rate == 0 and amount == 0 and interest != 0:

        rate  = interest * 100 / (principle*time)
        amount = interest + principle

        return rate



def CompoundInterest(principle=0, rate  = 0, time  = 0, interest = 0, amount = 0):

     # Implements the formula:  A = P((1 + (R/100))**N)

    if principle != 0 and rate != 0  and time != 0 and interest == 0 and amount == 0:
         
        amount  = principle * ((1 + (rate / 100))**time)
        interest = amount - principle

        return amount, int(interest)

    elif principle == 0 and rate != 0  and time != 0 and interest == 0 and amount != 0:

        principle = amount / ((1 + (rate / 100))**time)
        interest = amount  - principle

        return round(principle), int(interest)


    elif principle != 0 and rate == 0  and time != 0 and interest == 0 and amount != 0:

        # Derived a formula : R = (100 * A - 100 * p) / P

        rate  = 100 * ((amount - principle)/principle)
        interest  = amount - principle

        return rate, interest


def calculateGST(intra=True, inter=False, rate=0, principle=0):

    if intra:
        CGST = ((rate/2) / 100 ) * principle
        SGST = ((rate/2) / 100 ) * principle


        return {
        "CGST":CGST,
        "SGST":SGST,
        "IGST":0,
        "Price for end user": principle + CGST + SGST
        }

    elif inter:
        IGST = (rate/ 100) * principle

        return{
        "CGST":0,
        "SGST":0,
        "IGST":IGST,
        "Price for end user": principle + IGST
        }



def calculateGST2(intra1 = True, inter1 = False, intra2 = True, inter2 = False, principle = 0, profitPercent=0, profitAmount=0,rate1 = 0, rate2  = 0):

    

    if intra1 and intra2:

        GST = 0

        CGST1 = ((rate1/2)/100) * principle
        SGST1 = ((rate1/2)/100) * principle

        GST += round(CGST1 + SGST1)

        new_sp = 0

        if profitPercent !=0  and profitAmount == 0 :

            profitAmount = (profitPercent/ 100) * principle
            new_sp = principle + profitAmount

        elif profitPercent == 0 and profitAmount == 0:
            new_sp = principle + profitAmount


        CGST2 = ((rate2/2)/100) * new_sp
        SGST2 = ((rate2/2)/100) * new_sp

        GST += round(CGST2 + SGST2)

        return {
            "marked price by wholeseller":principle,
            "cost price for retailer": principle + CGST1 + SGST1,
            "selling price of retailer":new_sp,
            "marked price for consumer": principle + GST,
            "total GST":GST
        }


def reccuringDeposit(P, n, r):
    
    i = P*((n * (n+1)) / (2*12)) * (r/100)
    mv = (P*n)+i

    return {
        "interest":i,
        "Maturing Value":mv
    }
    







