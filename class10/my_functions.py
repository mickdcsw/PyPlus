from netmiko import ConnectHandler


def ssh_command(device, command):
    with ConnectHandler(**device) as connect:
        output = connect.send_command(command)
        print(output)

def ssh_command2(device):
    op_args = device.pop("optional_args")
    command = "show version"
    with ConnectHandler(**device) as connect:
        output = connect.send_command(command)
        return output
