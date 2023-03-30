import subprocess
import sys

system = sys.platform
print(system)

cmd = ['ping', '127.0.0.1','-c','4'] 
if system == 'win32':
	cmd = ['ping', '127.0.0.1'] 

proc = subprocess.run(
	cmd,
	capture_output=True,
	encoding='cp850',
	text=True
)

print('proc',proc)
print('proc.args:',proc.args)
print('proc.stderr:',proc.stderr)
print('proc.returncode:',proc.returncode)
# print(proc.stdout.decode('utf_8'))
print('proc.stdout:',proc.stdout) 


if system == 'linux':
	print('-'*10)
	cmd = ['ls -lah /']

	proc = subprocess.run(
		cmd,
		capture_output=True,
		encoding='utf_8',
		shell=True,
		text=True,
	)
	print(proc.stdout) 
