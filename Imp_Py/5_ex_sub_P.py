from subprocess import PIPE, Popen

process = Popen(['ls', '-l'], stdout=PIPE, stderr=PIPE)

stdout, stderr = process.communicate()

print(stdout)

# subprocess.call(['ls', '-l'])
# s = subprocess.check_output(["echo", "Hello Hacker!"])

