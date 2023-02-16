import re

def is_valid_credit_card_number(cc_num):
    # check length and formatting
    if not re.match(r'^[4-6]\d{3}(-?\d{4}){3}$', cc_num):
        return False
    
    # remove hyphens and check for consecutive repeated digits
    cc_num = cc_num.replace('-', '')
    if re.search(r'(\d)\1{3,}', cc_num):
        return False
    
    return True
cc_num = input("Please enter the card number to validate: ")
#cc_num = int(cc_num)
if is_valid_credit_card_number(cc_num):
    print('Valid credit card number')
else:
    print('Invalid credit card number')
