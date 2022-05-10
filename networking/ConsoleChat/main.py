import argparse
from os import chdir, path
import sys

from net.serverProtocol import runServer


def main(args: argparse.Namespace):
    host = args.host if args.host else "127.0.0.1"
    port = args.port if args.port else 5001

    if args.server:
        print("Starting server...")
        runServer(host, port)


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
    arguments = parser.parse_args(sys.argv[1:])
    main(args=arguments)
