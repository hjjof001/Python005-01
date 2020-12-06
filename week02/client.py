import os
import hashlib
import socket
import json

BUFF_SIZE = 1024

ADDRESS = '127.0.0.1'
PORT = 7777


class Message(object):
    STATUS_OK = 'ok'
    STATUS_FAILED = 'failed'

    def __init__(self, name="", size="", md5="", status="", msg=""):
        self.name = name
        self.size = size
        self.md5 = md5
        self.status = status
        self.msg = msg

    def __str__(self):
        return json.dumps({'name': self.name, 'size': self.size, 'md5': self.md5,
                           'status': self.status, 'msg': self.msg})


class File(object):

    def __init__(self, file):
        self.file = file

    @property
    def path(self):
        return os.path.dirname(self.file)

    @property
    def name(self):
        return os.path.basename(self.file)

    @property
    def md5(self):
        try:
            with open(self.file, 'rb') as rf:
                hash_md5 = hashlib.md5()
                hash_md5.update(rf.read())
                md5_value = hash_md5.hexdigest()
            return md5_value
        except Exception as e:
            print(e)

    @property
    def size(self):
        try:
            size = os.path.getsize(self.file)
            return size
        except Exception as e:
            print(e)


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ADDRESS, PORT))
    my_file = File("./test.txt")
    msg = Message(name=my_file.name, size=my_file.size, md5=my_file.md5)
    sock.sendall(str(msg).encode())
    receive = sock.recv(BUFF_SIZE)
    receive_data = Message(**json.loads(receive.decode('utf-8')))
    if receive_data.status == Message.STATUS_OK:
        with open("./test.txt", 'rb') as rf:
            while True:
                data = rf.read(BUFF_SIZE)
                if not data or data == b'':
                    break
                sock.sendall(data)
        receive = sock.recv(BUFF_SIZE)
        receive_data = Message(**json.loads(receive.decode("utf-8")))
        if receive_data.status == Message.STATUS_OK:
            print("Upload File Success!")
    sock.close()


if __name__ == '__main__':
    main()
