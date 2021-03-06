import argparse
from os import chdir, path
import sys

from net import runServer
from chatClient import runClient

def main(args: argparse.Namespace):
    host = args.host if args.host else "127.0.0.1"
    port = args.port if args.port else 5001
    test = args.test

    if args.server:
        print("Starting server...")
        runServer(host, port)
        return
    
    runClient(host=host,port = port, test = test)

if __name__ == "__main__":
    chdir(path.dirname(path.abspath(__file__)))

    # set up command line arguments
    # python main.py -s to start server
    # python main.py -t to start client in testing mode

    parser = argparse.ArgumentParser()
    parser.add_argument("--server", "-s", default=False,
                        action="store_true", help="start chat server")
    parser.add_argument("--host", type=str,
                        help="Specify hostname for client/server")
    parser.add_argument("--port", type=int,
                        help="Specify port for client/server")
    parser.add_argument("--test","-t", default=False, action="store_true",help="Start chat client in testing mode")
    arguments = parser.parse_args(sys.argv[1:])
    main(args=arguments)
