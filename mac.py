import subprocess

class MAC_changer:
    def __init__(self):
        self.MAC=""

    def get_MAC(self, iface):
        output = subprocess.run(["ifconfig", iface], shell=False, capture_output=True)

        cmd_result = output.stdout.decode('utf-8')
        print(cmd_result)
