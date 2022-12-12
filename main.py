def calc_inflation(init_bal, interest_rate, years_to_go):
    if years_to_go == 0:
        return init_bal
    if init_bal == 0:
        return 0
    interest = init_bal*interest_rate
    new_bal = init_bal*interest
    return calc_inflation(new_bal, interest, years_to_go-1)
#for above, could also do:
# years_remaining = years_to_go-1
# return calc_inflation(init_bal*(1+interest_rate), interest_rate, years_remaining