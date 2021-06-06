from snat.utils.common_utils import CommonUtils
import sys
from snat.snat import Snat


common=CommonUtils()
snat=Snat()


if __name__=='__main__':
    common.welcome_print()
    
    while True:
        try:
            user_input=snat.get_user_input()
            if user_input:
                snat.process_input(user_input)
            
        except KeyboardInterrupt:
            snat.exit_with_message()
        
    