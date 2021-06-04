
from snat.interface.interface_settings import Interface
import sys


"""
    This is the main class that handles all the other modules.
    You can create a module with its own class and functions and then you must resgister that function here.
    self.modules will contain alll the modules that are beeing registered.
"""

class Snat(Interface):
    def __init__(self):

        self.modules={
            '-1':self,
            '1':Interface(),
        }
        self.choice='-1'
        self.current_module=self
    
    def get_user_input(self):
        if self.current_module==self:
            self.show_options()
        user_input=input('What  is your choice?')
        
        if user_input=='q':
            print('Thankyou for using snat. Please provide your feedback and bug report @https://github.com/furiousmohan/SNAT.git')
            sys.exit(0)
        print('--------user input',user_input)
        if user_input=='-1' or user_input==-1:
            print('==========coming go -11')
            self.current_module=self
            return self.get_user_input()
        else:
            if self.current_module==self:
                if self.modules.get(user_input):
                    print('======into user')
                    self.current_module=self.modules.get(user_input)
                    print('========cur module',self.current_module)
                    return user_input
                elif self.current_module.methods.get(user_input):
                    print('=======inv')
                    print('\n\n Invalid choice!.Try again')
                    return self.get_user_input()
        
        return user_input

    def show_options(self):
        print('\t\t 1) Interface')
        print('\t\t q) Quit')
     
    def process_input(self,choice):
        print('--------current module',self.current_module)
        self.current_module.process_input(choice)
        self.current_module.show_options()

