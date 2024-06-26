from nada_dsl import *

def nada_main():
    party1 = Party(name="Party1")
    my_int1 = SecretInteger(Input(name="my_int1", party=party1))
    my_int2 = SecretInteger(Input(name="my_int2", party=party1))

    # Performing the computations
    sum_result = my_int1 + my_int2
    product_result = my_int1 * my_int2
    difference_result = my_int1 - my_int2

    # Conditional operation: if my_int1 > my_int2, compute my_int1 / my_int2 else compute my_int2 / my_int1
    greater_than = my_int1 > my_int2
    quotient_result = If(greater_than, my_int1 / my_int2, my_int2 / my_int1)

    # Outputting the results of the computations
    return [
        Output(sum_result, "sum_output", party1),
        Output(product_result, "product_output", party1),
        Output(difference_result, "difference_output", party1),
        Output(quotient_result, "quotient_output", party1)
    ]
