# main module for interface management
# This configuration will be used to all over the application.
import os
import subprocess
import re
from snat.utils.common_utils import CommonUtils



class Interface(CommonUtils):
    def __init__(self):
        self.interfaces={}
        self.choice=None
        self.default_interface=None
        self.methods={
            1:self.show_interfaces,
            2:self.set_default_interface,
            3:self.change_mac_address,
            4:self.set_interface_mode,
            5:self.process_all,
        }
        self.interface_modes={1:'monitor',2:'managed'}
    # default module options
    def show_options(self):
        self.set_options_color()
        print('\n\n\t\t=======  Interface Menu ======')
        print('\t\t 1) Show Interfaces')
        print('\t\t 2) Set Default Interface')
        print('\t\t 3) Change Mac Address')
        print('\t\t 4) Set Interface Mode')
        print('\t\t 5) All')
        print('\t\t 6) Print Detailed Help Message')
        print('\t\t-1) Go TO Previous Options')
        print('\t\t 0) Quit')
        print('\t\t======= End Interface Menu ======')
        self.set_default_color()



    # Show the available interfaces using ifconfig
    def show_interfaces(self):
        interfaces=subprocess.check_output('ifconfig',shell=True)
        interfaces=interfaces.decode().split('\n\n')
        interfaces=self.set_choice_numbers(interfaces)
        for key,interface in self.interfaces.items():
            self.print_message(f'{str(key)}) '+ interface)
            self.set_default_color()

    # setting up the default interface using ifconfig
    def set_default_interface(self):
        self.show_interfaces()
        choice=self.ask_user_input('Enter the interface number.')
        if self.interfaces.get(choice):
            self.default_interface=self.interfaces.get(choice)
            self.success_message(f'Interface defaults to {self.default_interface}.')
            return True
        else:
            self.error_message(f'Invalid choice!\t\t{choice}')
            self.set_default_interface()

    # Change the mac address using ifconfig and print the result
    def change_mac_address(self):
        default_interface=self.check_default_interface()
        if default_interface:
        
            mac_address=self.ask_user_input('Enter mac address to set',char=True)
            res=self.change_mac(mac_address)
            if res:
                self.success_message(f'Mac address changed to {mac_address}')

    # Change interface mode using iwconfig
    def set_interface_mode(self):
        default_interface=self.check_default_interface()
        if default_interface:

            mode=self.ask_user_input('\n\t\tWhich mode? \t\t1) Monitor \t2) Managed')
            res=self.set_mode(mode)
            if res:
                self.success_message(f'Interface mode changed successfully!')

    # Process all the functions above one by one.
    def process_all(self):
        self.set_default_interface()
        self.change_mac_address()
        self.set_interface_mode()
        return
 


    # ==================helper functions=================
    def set_choice_numbers(self,input_list):
        new_list=[]
        for i in range(len(input_list)):
            res=re.search('.*\w: ',input_list[i])
            if res:
                new_list.append(input_list[i])
                self.interfaces[i+1]=res.group(0)[:-2]
        return new_list
    
    
    def check_default_interface(self):
        if not self.default_interface:
            self.error_message('Set default interface first and try again!')
            self.show_options()
            user_input=input('\n\t\t What is your choice?')
            return self.process_input(user_input)
        return True

    

    def change_mac(self,mac_address):
        try:
            subprocess.check_output(['ifconfig',self.default_interface,'down'])
            subprocess.check_output(['ifconfig',self.default_interface,'hw','ether',mac_address])
            subprocess.check_output(['ifconfig',self.default_interface,'up'])
            return True
            
        except Exception as e:
            subprocess.call(['ifconfig',self.default_interface,'up'])
            self.error_message(e)
            return False

    def set_mode(self,mode):
        try:
            subprocess.check_output(['ifconfig',self.default_interface,'down'])
            subprocess.check_output(['iwconfig',self.default_interface,'mode',self.interface_modes.get(int(mode))])
            return True
        except Exception as e:
            subprocess.call(['ifconfig',self.default_interface,'up'])
            self.error_message(e)
            return False

    

    # Process the incomming input from the main module. 
    # All the classes must implement this function in order to handle the request.
    def process_input(self,choice):
        self.choice=choice
        if self.methods.get(self.choice):
            self.methods.get(self.choice)()
        else:
            print('Invalid choice. Try again!')
            return
