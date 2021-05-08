## Second Try
import subprocess
import json

## MacOs Users
# command = './derive -g --mnemonic="INSERT HERE" --cols=path,address,privkey,pubkey --format=json'

## Windows Users
command = 'php hd-wallet-derive.php -g --mnemonic="gather game midnight sport patch myth crawl avocado deputy fee smile route" --cols=path,address,privkey,pubkey --format=json'
# command = 'ls'

p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
output, err = p.communicate()
p_status = p.wait()

keys = json.loads(output)
print(keys)

print(keys[0]['address'])