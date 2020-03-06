from datetime import datetime, timedelta

def initialization(creditAmount, creditRate, paymentStep, period, payPerPeriod, total, type):
        resPay = [{} for i in range(int(period))]
        creditAmountCopy, totalCreditAmountCopy = float(creditAmount), float(total)
        totalPlus = 0.0
        today = datetime.now()
        for i in range(int(period)):
            percent = float(creditAmountCopy * (creditRate / 100))
            if type:
                percent /= 12
            if not type:
                percent = percent * paymentStep
            creditAmountCopy -= payPerPeriod - percent
            #-----------------------------------------------
            resPay[i]["Id"] = i + 1
            if type:
                resPay[i]["Date"] = (today + timedelta(i)).strftime("%d/%m/%y")
            if not type:
                resPay[i]["Date"] = (today + timedelta(paymentStep * i)).strftime("%d/%m/%y")
            resPay[i]["Body"] = round(payPerPeriod - percent, 2)
            resPay[i]["Percent"] = round(percent, 2)
            resPay[i]["MainBalance"] = round(abs(creditAmountCopy), 2)
            totalCreditAmountCopy -= round(payPerPeriod, 2)
            totalPlus = resPay[i]["MainBalance"]
            #-----------------------------------------------
        resPay[0]["TotalOverPay"] = round(total - creditAmount + totalPlus,2)
        return resPay

def PaymentScheduleForYearRate(creditAmount, creditRate, creditPeriod, paymentStep):
    ratePerMonth = creditRate / 100 / 12
    payPerMonth = creditAmount * (ratePerMonth / (1 - (1 + ratePerMonth) ** -creditPeriod))
    totalCreditAmount = payPerMonth * creditPeriod

    pay = initialization(creditAmount, creditRate, paymentStep, creditPeriod, payPerMonth, totalCreditAmount, True)

    res = {}
    res["calc"] = pay
    res["payPer"] = str(round(payPerMonth, 2))
    res["totalOverpay"] = str(pay[0]["TotalOverPay"])
    return res

def PaymentScheduleForDayRate(creditAmount, creditRate, creditPeriod, paymentStep):
    thisPeriod = creditPeriod // paymentStep
    ratePerStep = creditRate / 100 * paymentStep
    payPerStep = creditAmount * ((ratePerStep * ((1 + ratePerStep) ** (creditPeriod / paymentStep))) / (((1 + ratePerStep) ** (creditPeriod / paymentStep)) - 1))
    totalCreditAmount = payPerStep * creditPeriod / paymentStep
    pay = initialization(creditAmount, creditRate, paymentStep, thisPeriod, payPerStep, totalCreditAmount, False)

    res = {}
    res["calc"] = pay
    res["payPer"] = str(round(payPerStep, 2))
    res["totalOverpay"] = str(pay[0]["TotalOverPay"])
    return res