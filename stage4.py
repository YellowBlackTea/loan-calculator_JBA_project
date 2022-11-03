import math
import argparse

parser = argparse.ArgumentParser(description="loan calculator")
parser.add_argument("-t", "--type", choices=["diff", "annuity"])
parser.add_argument("-payment", "--payment")
parser.add_argument("-loan", "--principal")
parser.add_argument("-p", "--periods")
parser.add_argument("-i", "--interest")

args = parser.parse_args()
arguments = [args.type, args.principal, args.periods, args.interest, args.payment]
arguments_len = len([arg for arg in arguments if arg is not None])
negative = len([True for elt in arguments if elt is not None and elt != "diff" and elt != "annuity" and float(elt) < 0])

if not args.type or not args.interest:
    print("Incorrect parameters")
elif args.type == "diff" and args.payment:
    print("Incorrect parameters")
elif arguments_len < 4 or negative:
    print("Incorrect parameters")


def loan_principal(annuity, period, interest):
    p = math.ceil(annuity/((interest/1200*(1+interest/1200)**period)/(((1+interest/1200)**period)-1)))
    print("Your loan principal =", p)
    total_sum = annuity * period
    print("Overpayment =", total_sum-p)


def number_monthly_payment(loan, mp, interest):
    nb_month = math.ceil(math.log(mp/(mp-(interest/1200*loan)), 1+interest/1200))

    if nb_month == 1:
        print("It will take", nb_month, "month to repay this loan!")
    elif 1 < nb_month < 12:
        print("It will take", nb_month, "months to repay this loan!")
    else:
        year = nb_month // 12
        month = nb_month - year*12
        if year == 1:
            if month == 1:
                print("It will take", year, "year and", month, "month to repay this loan!")
            elif month == 0:
                print("It will take", year, "year to repay this loan!")
            else:
                print("It will take", year, "year and", month, "months to repay this loan!")
        elif year == 0:
            if month == 1:
                print("It will take", month, "month to repay this loan!")
            else:
                print("It will take", month, "months to repay this loan!")
        else:
            if month == 1:
                print("It will take", year, "years and", month, "month to repay this loan!")
            elif month == 0:
                print("It will take", year, "years to repay this loan!")
            else:
                print("It will take", year, "years and", month, "months to repay this loan!")
    total_sum = nb_month * mp
    print("Overpayment =", total_sum-loan)


def monthly_payment(loan, period, interest, payment_type):
    total_sum = 0
    if payment_type == "annuity":
        a = math.ceil(loan*(interest/1200*(1+interest/1200)**period)/(((1+interest/1200)**period)-1))
        print("Your annuity payment =", a)
        total_sum = a * period
    if payment_type == "diff":
        for m in range(1, period+1):
            d = math.ceil(loan/period + interest/1200*(loan - (loan*(m - 1))/period))
            print("Month", m+": payment is", d)
            total_sum += d

    print("Overpayment =", total_sum-loan)


# diff appels des fonctions
if args.type and args.principal and args.payment and args.interest and not args.periods:
    print(number_monthly_payment(float(args.principal), float(args.payment), float(args.interest)))
elif args.type and args.principal and not args.payment and args.interest and args.periods:
    print(monthly_payment(float(args.principal), int(args.periods), float(args.interest), args.type))
elif args.type == "annuity" and not args.principal and args.payment and args.interest and args.periods:
    print(loan_principal(float(args.payment), int(args.periods), float(args.interest)))


def main():
    print("What do you want to calculate?")
    print('type "n" for number of monthly payments,')
    print('type "a" for annuity monthly payment amount,')
    print('type "p" for loan payment:')
    choice = input()
    if choice == 'n':
        n_num_monthly_payment()
    if choice == 'p':
        p_loan_principal()
    if choice == 'a':
        a_annuity_payment()


if __name__ == '__main__':
    main()

