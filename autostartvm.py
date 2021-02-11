import paramiko
import requests

#get vmid = vim-cmd vmsvc/getallvms |grep <vm name>

vmid = "1"
ip = "#########"
user = "#####"
passw = "########"
pwcheck = "vim-cmd vmsvc/power.getstate " + vmid
pwon = "vim-cmd vmsvc/power.on " + vmid
pwoff = "vim-cmd vmsvc/power.off " + vmid

url = 'https://notify-api.line.me/api/notify'
token = '#######'
headers = {
            'content-type':
            'application/x-www-form-urlencoded',
            'Authorization':'Bearer '+token
           }

ssh = paramiko.SSHClient()

def checkvm(ipaddr, theuser, thepassword, cmd):
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ipaddr, username=theuser, password=thepassword, look_for_keys=False )
    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(cmd)
    output = ssh_stdout.readlines()
    return output
    ssh.close()

state = checkvm(ip, user, passw, pwcheck)
output = state[1]

if output[0:-1] == "Powered off":
    print(output[0:-1] + " Starting VM ...")
    #requests.post(url, headers=headers , data = {'message':output[0:-1] + " Starting VM ..."})
    checkvm(ip, user, passw, pwon)
else:
    print(output[0:-1])
    #requests.post(url, headers=headers , data = {'message':output[0:-1]})
