from  Get_Proxies_List import save_all_proxies
from  Find_Trusted_Proxies import save_checked_proxies
import os


def screenClear():
    print("\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n")

    if os.name=='nt':
        os.system('cls')
    elif os.name=='posix':
        os.system('clear')
    print("")

def screenWrite():
    print()
    print('\t#####################################################')
    print('\t#/*************************************************\#')
    print('\t#**||~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~||**#')
    print('\t#**||                                           ||**#')
    print('\t#**||         Gngr Proxy Harvester v1.0         ||**#')
    print('\t#**||                                           ||**#')
    print('\t#**||                                           ||**#')
    print('\t#**||       Developer: Exancodex                ||**#')
    print('\t#**||                                           ||**#')
    print('\t#**||~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~||**#')
    print('\t#\*************************************************/#')
    print('\t#####################################################')
    print()
    print()


if __name__ == '__main__':
    screenClear()
    screenWrite()
    save_all_proxies()
    save_checked_proxies()
