from server import Server
from counter import Counter

HOST = "127.0.0.1"
PORTS = [4201, 4202, 4203]

if __name__ == "__main__":

    servers = [
        Server(id=id, host=HOST, port=PORTS[id-1], state_machine=Counter())
        for id in range(1, len(PORTS)+1)
    ]

    for server in servers:
        server.run()
    
    # TODO: a client interface to interact with the servers e.g. 
    # client = Client(server_config=[HOST, PORTS]) 
    # client.send_command("INC")