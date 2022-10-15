from server_client.Server  import Server



def main():
    server = Server()
    server.creating_server()
    while True:
        server.creating_select()
        server.for_reading()
        server.for_writing()



if __name__ == "__main__":
    main()