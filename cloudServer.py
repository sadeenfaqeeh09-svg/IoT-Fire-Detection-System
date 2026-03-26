import argparse
import json
import socket

def handle(conn):
    buf = b""
    while True:
        chunk = conn.recv(4096)
        if not chunk:
            break
        buf += chunk
        while b"\n" in buf:
            line, buf = buf.split(b"\n", 1)
            if not line.strip():
                continue
            try:
                evt = json.loads(line.decode("utf-8"))
                print(f"Event received: {evt}")
            except json.JSONDecodeError:
                print("Invalid JSON")

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--host", default="0.0.0.0")
    p.add_argument("--port", type=int, default=5000)
    args = p.parse_args()

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((args.host, args.port))
    s.listen(5)
    print(f"Server listening on {args.host}:{args.port}")
    try:
        while True:
            conn, addr = s.accept()
            print(f"Connected by {addr}")
            try:
                handle(conn)
            finally:
                conn.close()
    finally:
        s.close()

if __name__ == "__main__":
    main()
