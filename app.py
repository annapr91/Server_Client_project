from server_client.Server  import Server



def main():
    server = Server()
    server.creating_server()
    while True:
        server.for_reading()




if __name__ == "__main__":
    main()