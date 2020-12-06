import socket
import json
import os
import hashlib

BUFF_SIZE = 1024

ADDRESS = "0.0.0.0"
PORT = 7777
SAVE_PATH = './upload_save'
CONNECTION_NUMBERS = 10


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
    """
    文件信息对象。
    """

    def __init__(self, file):
        """
        :param file:(str)
        """
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
    save_path = './upload_save'
    if not os.path.isdir(save_path):
        os.makedirs(save_path)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((ADDRESS, PORT))
    sock.listen(CONNECTION_NUMBERS)
    try:
        while True:
            conn, client_address = sock.accept()

            receiver = conn.recv(BUFF_SIZE)
            file_info = Message(**json.loads(receiver.decode("utf-8")))
            conn.sendall(str(Message(status=Message.STATUS_OK)).encode())
            print("Receiver from {} data: {}".format(client_address, file_info))

            file = os.path.join(save_path, file_info.md5)
            with open(file, 'wb') as wf:
                size = 0
                while True:
                    data = conn.recv(BUFF_SIZE)
                    size += len(data)
                    if size == file_info.size:
                        wf.write(data)
                        break
                    wf.write(data)
            print("Success write file: {}".format(file))

            file = File(file)
            if file.md5 == file_info.md5:
                msg = Message(status=Message.STATUS_OK)
            else:
                msg = Message(status=Message.STATUS_FAILED)

            conn.sendall(str(msg).encode())
            conn.close()
    except Exception as e:
        print(e)
        sock.close()


if __name__ == '__main__':
    main()
