# This module contains helper functions.
# All The common helper functions should be populated through this class.
import sys
from colorama import Fore,Back,Style

class CommonUtils():

    def welcome_print(self):
        print(Fore.WHITE+r"""\
                                                          O
                                    //*****\\            ooo
            **********              ||      ||           
            ||  ||        ||    //*****\\   ||  ||    //*****\\
            ||  ||        ||    ||     ||   ||  ||    ||     ||
          /*||**||**\\    ||    ||     ||   ||  ||    ||     ||
          ||    ||  ||    ||    ||     ||   ||  ||    ||     ||
          ++++++//  ||    ***************   **  ***************   *****  ||\\   ||     //\\     *********
                    ||                                ||          ||     || \\  ||    //  \\        ||
          *=========*/                                 %%$$$%%     ++++  ||  \\ ||   // ** \\       ||
                                                    ||   ||           || ||   \\||  //      \\      ||
                                                    %%%% //       *****  **    **  **        **     **
       """)
        print(Fore.BLUE)


    def ask_user_input(self,question,char=False):
        try:
            if char:
                user_input=input(f'\n\n\t\t{question}\t\t')
            else:
                user_input=int(input(f'\n\n\t\t{question}\t\t'))
            return user_input
        except ValueError:
            print('\n\n\t\tPlease enter integers instead charecters!')
            return self.ask_user_input()
        except KeyboardInterrupt:
            self.exit_with_message()
    
    def exit_with_message(self):
        print(Fore.YELLOW+'\n\n\t\tThankyou for using snat. Please provide your feedback and bug report @https://github.com/furiousmohan/SNAT.git')
        sys.exit(0)

    def error_message(self,error):
        print(Fore.RED+'\n\n\t\t================== ERROR! =============')
        print(Fore.YELLOW+f'\t\t{str(error)}')
        print(Fore.RED+'\t\t==================  END  =============\n\n')
        print(Fore.BLUE)


    def success_message(self,message):
        print(Fore.GREEN+'\n\n\t\t================== SUCCESS! ===========')
        print(Fore.YELLOW+f'\t\t{str(message)}')
        print(Fore.GREEN+'\t\t==================  END  ===============\n\n')
        print(Fore.BLUE)
    
    def print_message(self,message):
        print(Fore.YELLOW+f'\t\t{str(message)}')

    def set_options_color(self):
        print(Fore.CYAN)
    
    def set_default_color(self):
        print(Fore.BLUE)


    


