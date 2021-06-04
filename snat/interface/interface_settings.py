# main module for interface management
# This configuration will be used to all over the application.
import os
import subprocess
import re



class Interface():
    def __init__(self):
        self.interfaces={}
        self.choice=None
        self.default_interface=None
        self.methods={
            '1':self.show_interfaces,
            '2':self.set_default_interface,
            '3':self.change_mac_address,
            '4':self.set_interface_mode,
            '5':self.process_all,
        }
        self.interface_modes={1:'monitor',2:'managed'}

    def set_choice_numbers(self,input_list):
        new_list=[]
        for i in range(len(input_list)):
            res=re.search('.*\w: ',input_list[i])
            if res:
                new_list.append(input_list[i])
                self.interfaces[i+1]=res.group(0)[:-2]
        return new_list
    
    def set_default_interface(self):
        self.show_interfaces()
        choice=input('\t\tEnter interface number\t')
        print('-=======self.in',self.interfaces,choice,type(choice))
        choice=int(choice)
        if self.interfaces.get(choice):
            self.default_interface=self.interfaces.get(choice)
            print(f'\t\tInterface defaults to {self.default_interface}.')
            return self.show_options
        else:
            print('\t\tInvalid Choice!\n')
            self.set_default_interface()
    def check_default_interface(self):
        if not self.default_interface:
            print('Set default interface first and try again!')
            self.show_options()
            user_input=input('\n\t\t What is your choice?')
            return self.process_input(user_input)
        return True

    def change_mac_address(self):
        default_interface=self.check_default_interface()
        if default_interface:
        
            mac_address=input('\n\t\tEnter mac address to set')
            res=self.change_mac(mac_address)
            if res:
                res=subprocess.check_output(['ifconfig',self.default_interface])
                print('\n\t\t',res)

    def change_mac(self,mac_address):
        try:
            subprocess.check_output(['ifconfig',self.default_interface,'down'])
            subprocess.check_output(['ifconfig',self.default_interface,'hw','ether',mac_address])
            subprocess.check_output(['ifconfig',self.default_interface,'up'])
            return True
            
        except Exception as e:
            subprocess.call(['ifconfig',self.default_interface,'up'])
            print(e)
            return self.change_mac_address()

    def set_interface_mode(self):
        default_interface=self.check_default_interface()
        if default_interface:

            mode=input('\n\t\tWhich mode? \t\t1) Monitor 2) Managed')
            res=self.set_mode(mode)
            if res:
                print('\n\t\t',check_output(['iwconfig',self.default_interface]))

    def set_mode(self,mode):
        try:
            subprocess.check_output(['ifconfig',self.default_interface,'down'])
            subprocess.check_output(['iwconfig',self.default_interface,'mode',self.interface_modes.get(int(mode))])
            return True
        except Exception as e:
            subprocess.call(['ifconfig',self.default_interface,'up'])
            print(e)
            return self.show_options()

    def process_all(self):
        self.set_default_interface()
        self.change_mac_address()
        self.set_interface_mode()
        return
        






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
        print('\t\t 4) Set Interface Mode')
        print('\t\t 5) All')
        print('\t\t 6) Print Detailed Help Message')
        print('\t\t-1) Go TO Previous Options')

    def process_input(self,choice):
        self.choice=choice
        self.methods.get(self.choice)()
