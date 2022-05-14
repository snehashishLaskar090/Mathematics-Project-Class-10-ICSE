


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


