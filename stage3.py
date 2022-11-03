import math


def p_loan_principal():
    annuity = float(input("Enter the annuity payment:"))
    period = int(input("Enter the number of periods:"))
    interest = float(input("Enter the loan interest:"))
    p = math.ceil(annuity/((interest/1200*(1+interest/1200)**period)/(((1+interest/1200)**period)-1)))
    print("Your loan principal =", p)


def n_num_monthly_payment():
    loan = float(input("Enter the loan principal:"))
    mp = int(input("Enter the monthly payment:"))
    interest = float(input("Enter the loan interest:"))

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


def a_annuity_payment():
    loan = int(input("Enter the loan principal:"))
    period = int(input("Enter the number of periods:"))
    interest = float(input("Enter the loan interest:"))

    a = math.ceil(loan*(interest/1200*(1+interest/1200)**period)/(((1+interest/1200)**period)-1))
    print("Your monthly payment =", a)


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

