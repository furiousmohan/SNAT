
from snat.interface.interface_settings import Interface
from snat.utils.common_utils import CommonUtils
import sys


"""
    This is the main class that handles all the other modules.
    You can create a module with its own class and functions and then you must resgister that function here.
    self.modules will contain alll the modules that are beeing registered.
"""

class Snat(Interface):
    def __init__(self):
        self.modules={
            -1:self,
             1:Interface(),
             
        }
        self.choice=-1
        self.current_module=self
    
    def get_user_input(self):
        if self.current_module==self:
            self.show_options()
        try:
            user_input=int(input('\n\n\t\tWhat  is your choice?\t\t'))
        except ValueError:
            print('\n\n\t\tPlease enter number instead charecters!')
            return self.get_user_input()
        except KeyboardInterrupt:
            self.exit_with_message()
        
        if user_input==0:
           self.exit_with_message()
        if user_input==-1:
            self.current_module=self
            return self.get_user_input()
        else:
            if self.current_module==self:
                
                if self.modules.get(user_input):
                    self.current_module=self.modules.get(user_input)
                    self.current_module.show_options()
                    return False
            
        
        return user_input

    def show_options(self):
        print('\t\t 1) Interface')
        print('\t\t 0) Quit')
     
    def process_input(self,choice):
        self.current_module.process_input(choice)
        self.current_module.show_options()
    
    

