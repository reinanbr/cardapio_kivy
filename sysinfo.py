#####################################################
############### author Reynan Br ####################
###############   sysinfo lib    ####################
############# 01/11/2021 01:01 pm ###################
#####################################################
import os, signal, sys

# set stderr to dev/null
sys.stderr = open(os.devnull, "w")
try:
    pass
  #import psutil 
#except:
  #handle module not found 
finally:
  sys.stderr = sys.__stderr__

from collections import namedtuple
#########################################################
########## def's for getting info from system ###########
#ps = psutil

## datting the time in the choice format ##
def date(fmt="%d/%m/%Y %H:%M:%S"):
    from datetime import datetime as dt
    dt = dt.now()
    return dt.strftime(fmt)

## get info from ram ##
def get_info_ram():
   r_max = psutil.virtual_memory().total
   r_per = psutil.virtual_memory().percent
   r_use = psutil.virtual_memory().used
   #r_ping = round(time.process_time()*100,1)
   r_ = namedtuple('ram',['use','max','percent'])
   return r_(r_use,r_max,r_per)

## get info from cpu ##
def get_info_cpu():
	cpu_crock = (ps.cpu_freq().max)
	cpu_freq_use = round(ps.cpu_freq().current,3)
	cpu_percent = ps.cpu_percent()
	cpu_info_ = namedtuple('cpu',['use','crock','percent'])
	return cpu_info_(cpu_freq_use,cpu_crock,cpu_percent)

## get info from gpu ##
def get_info_gpu():
	pass

## get dir memory used ##
def get_info_dir(dir='/'):
	disk_usage = round(ps.disk_usage(dir)/(1024**3),2)
	disk_total = round(ps.disk_usage(dir)/(1024**3),2)
	disk_percent = ps.disk_usage(dir).percent
	disk = namedtuple('disk',['use','total','percent'])
	return disk(disk_usage,disk_total,disk_percent)
######### end def's for getting info system #############
#########################################################



######################################################################
######### def's for the sho and work with the info's system ##########



def get_size(bytes, suffix="B"):
    """
    Scale bytes to its proper format
    e.g:
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
    """
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor


## working for the android ## 
def cmd(command): return os.popen(command).read()

def info_android():
    info = {}
    
    #hardware
    base_ = 'cat /system/build.prop | grep '
    
    model = cmd(base_+'system.model=').split('=')[1].strip('\n')
    company = cmd(base_+'system.brand=').split('=')[1].strip('\n').capitalize()
    chipset = cmd(base_+'hardware.chipname=').split('=')[1].strip('\n')
    arch = cmd(base_+'cpu.abi=').split('=')[1].strip('\n')
    
    #cpu
    cpu_ = 'cat /proc/cpuinfo | grep '
    
    n_nucleo = cmd(cpu_+'architecture -m 1').split(': ')[1].strip('\n')
    cpu_brand = cmd(cpu_+'Hardware').split(': ')[1].strip('\n')
    
    info['model'] = model
    info['brand'] = company
    info['chipset'] = chipset
    info['arch'] = arch
    info['n_nucleo'] = n_nucleo
    info['brand_cpu'] = cpu_brand
    
    return info

def show_info_system():
    system_version_info = os.popen('cat /proc/version').read().split(' ')
    name_system = system_version_info[0]
    version_system = system_version_info[2]
    name_version = system_version_info[3]

    if True:
        print('is Android!')
        #pass
    else:
        print('dont is Android!')
        android_info = ''
    cpu = get_info_cpu()
    ram = get_info_ram()
    text_info = f'''
    [b]name system:[/b] {name_system}
    [b]version:[/b] {version_system}
    [b]version name:[/b] {name_version}
    [b]cpu using:[/b] {cpu.use}Mhz
    [b]cpu crock:[/b] {cpu.crock}Mhz
    [b]cpu percent:[/b] {cpu.percent}%
    [b]ram using:[/b] {get_size(ram.use)}
    [b]ram max:[/b] {get_size(ram.max)}
    [b]ram percent:[/b] {ram.percent}%
    
    '''
    
    return text_info
    
#print(show_info_system())