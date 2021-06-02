from snat.utils.common_utils import CommonUtils
import sys
from snat.snat import Snat


common=CommonUtils()
snat=Snat()


if __name__=='__main__':
    common.welcome_print()
    
    while True:
        
        if snat.choice==0:
            snat.show_options()
            
        choice=input('\t\tPlease Enter Your Choice!\t')
        if choice=='q':
            print('Thankyou for using snat. Please provide your feedback and bug report @https://github.com/furiousmohan/SNAT.git')
            sys.exit(0)
        snat.choice=int(choice)
        snat.current_module=snat.modules.get(choice)
        snat.process_input(choice)
        
    