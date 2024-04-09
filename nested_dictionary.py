server_config = {
    'server1': {'ip': '192.168.1.1', 'port': 8080, 'status': 'active'},
    'server2': {'ip': '192.168.1.2', 'port': 8000, 'status': 'inactive'},
    'server3': {'ip': '192.168.1.3', 'port': 9000, 'status': 'active'}
}

# Retrieving information
def get_server_ip(server_name):
    return server_config.get(server_name, {}).get('ip', 'Server not found')

# Example usage
server_name = 'server2'
ip = get_server_ip(server_name)
print(f"{server_name} ip: {ip}")