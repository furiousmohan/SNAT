
from snat.interface.interface_settings import Interface


"""
    This is the main class that handles all the other modules.
    You can create a module with its own class and functions and then you must resgister that function here.
    self.modules will contain alll the modules that are beeing registered.
"""

class Snat(Interface):
    def __init__(self):
        self.modules={
            '0':self,
            '1':Interface(),
        }
        self.choice=0
        self.current_module=self.modules.get('0')
       

    def show_options(self):
        print('\t\t 1) Interface')
        print('\t\t q) Quit')
     
    def process_input(self,choice):
        self.modules.get(choice).process_input(choice)
        self.modules.get(choice).show_options()

