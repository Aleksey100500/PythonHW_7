import model_sum
import except_num as ex

def user_interface():
    number_a = ex.get_number()
    number_b = ex.get_number()
    print(model_sum.sum(number_a,number_b))
    
user_interface()
