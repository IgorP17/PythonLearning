import os
import socket
import threading
import multiprocessing


def worker(my_socket):
    while True:
        conn, addr = my_socket.accept()
        print("pid", os.getpid())
        th = threading.Thread(target=process_request, args=(conn, addr))
        th.start()


def process_request(conn, addr):
    print("connected client:", addr)
    with conn:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print(data.decode("utf8"))


if __name__ == '__main__':
    with socket.socket() as sock:
        sock.bind(("127.0.0.1", 10001))
        sock.listen(socket.SOMAXCONN)
        workers_count = 3
        workers_list = [multiprocessing.Process(target=worker, args=(sock,))
                        for _ in range(workers_count)]
        for w in workers_list:
            w.start()
        for w in workers_list:
            w.join()
