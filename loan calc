import math
import argparse


def number_of_monthly_payments(loan_principal, monthly_payment, nominal_rate):
    months = math.log(monthly_payment / (monthly_payment - nominal_rate * loan_principal), 1 + nominal_rate)
    months_to_repay = math.ceil(months)
    if months_to_repay == 1:
        message = "It will take 1 month to repay the loan"
    elif months_to_repay > 11:
        years = months_to_repay // 12
        p_months = months_to_repay % 12
        if years == 1:
            m_year = "1 year"
        else:
            m_year = f"{years} years"
        if p_months == 1:
            m_month = " and 1 month"
        elif p_months == 0:
            m_month = ""
        else:
            m_month = f" and {p_months} months"
        message = "It will take " + m_year + m_month + " to repay this loan!"
    else:
        message = f"It will take {months} months to repay the loan"
    print(message)
    print(f"Overpayment = {round((months_to_repay * monthly_payment) - loan_principal)}")


def annuity_payment(loan_principal, periods, nominal_rate):
    param = math.pow(1 + nominal_rate, periods)
    payment = math.ceil(loan_principal * ((nominal_rate * param) / (param - 1)))
    print(f"Your monthly payment = {payment}!")
    print(f"Overpayment = {round(payment * periods - loan_principal)}")


def principal(monthly_payment, periods, nominal_rate):
    param = math.pow(1 + nominal_rate, periods)
    loan_principal = math.floor(monthly_payment / ((nominal_rate * param) / (param - 1)))
    print(f"Your loan principal = {loan_principal}!")
    print(f"Overpayment = {round(monthly_payment * periods - loan_principal)}")


def differentiate_payment(p, n, i):
    overpayment = - p
    for m in range(1, n + 1):
        d_payment = math.ceil(p / n + i * (p - p * (m - 1) / n))
        print(f"Month {m}: payment is {d_payment}")
        overpayment += d_payment
    else:
        print(f"\nOverpayment = {round(overpayment)}")


parser = argparse.ArgumentParser()
parser.add_argument("--type")
parser.add_argument("--principal", type=float)
parser.add_argument("--periods", type=int)
parser.add_argument("--interest", type=float)
parser.add_argument("--payment", type=float)
args = parser.parse_args()

if ((args.type != "diff") and (args.type != "annuity")) or args.interest is None:
    print("Incorrect parameters")
elif args.type == "diff":
    if args.payment is not None or args.principal is None or args.periods is None:
        print("Incorrect parameters")
    else:
        differentiate_payment(args.principal, args.periods, args.interest / 1200)
elif args.type == "annuity":
    if args.payment is None and args.principal is not None and args.periods is not None:
        annuity_payment(args.principal, args.periods, args.interest / 1200)
    elif args.payment is not None and args.principal is None and args.periods is not None:
        principal(args.payment, args.periods, args.interest / 1200)
    elif args.payment is not None and args.principal is not None and args.periods is None:
        number_of_monthly_payments(args.principal, args.payment, args.interest / 1200)
    else:
        print("Incorrect parameters")
