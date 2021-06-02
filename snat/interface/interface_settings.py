# main module for interface management
# This configuration will be used to all over the application.
import os
import subprocess



class Interface():
    def __init__(self):
        self.methods={
            '1':self.show_interfaces,
        }

    def set_choice_numbers(self,input_list):
        new_list=[]
        for i in range(len(input_list)):
            new_list.append(input_list[i])
        return new_list

    def show_interfaces(self):
        interfaces=subprocess.check_output('ifconfig',shell=True)
        interfaces=interfaces.decode().split('\n\n')
        interfaces=self.set_choice_numbers(interfaces)
        for i,interface in enumerate(interfaces):
            modes=interface.split('\n')
            print(f'\n\n\t\t------Interface----{i+1}')
            for mode in modes:
                print(mode)

    def show_options(self):
        print('\t\t=======  Interface  ======')
        print('\t\t 1) Show Interfaces')
        print('\t\t 2) Set Default Interface')
        print('\t\t 3) Change Mac Address')
        print('\t\t 3) Print Detailed Help Message')
        print('\t\t-1) Go TO Previous Options')

    def process_input(self,choice):
        self.methods.get(choice)()
