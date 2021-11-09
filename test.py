from os import curdir

def Calculate_Percent(current_value, final_value):
    calc_var = int((current_value/final_value) * 100) 
    print(str(calc_var).replace(".", "") + "%")


Calculate_Percent(float(input("current value")), float(input("final value")))