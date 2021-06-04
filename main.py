from snat.utils.common_utils import CommonUtils
import sys
from snat.snat import Snat


common=CommonUtils()
snat=Snat()


if __name__=='__main__':
    common.welcome_print()
    
    while True:
        user_input=snat.get_user_input()
        print('========user input',user_input)
        snat.process_input(user_input)
        
    