# ############## Request #################
"""
POST / HTTP/1.1\r\n
Host: example.com\r\n
Accept: application/json\r\n
Content-type: application/json\r\n
Content-length: 2\r\n
\r\n
{}
"""
# ############## Response #################
ddd = b"""
HTTP/1.1 200 OK\r\nContent-type: text/html\r\nContent-length: 15\r\n\r\n<h1>Hello!</h1>
"""

RESPONSE = b"""\
HTTP/1.1 200 OK
Content-Type: text/html
Content-Length: 25

<h1>Hello</h1><h2>222</h2>
""".replace(
    b"\n", b"\r\n"
)

import socket
import typing
import os
import mimetypes


HOST = "127.0.0.1"
PORT = 9000

BAD_REQUEST_RESPONSE = b"""\
HTTP/1.1 400 Bad Request
Content-type: text/plain
Content-length: 11

Bad Request""".replace(
    b"\n", b"\r\n"
)

NOT_FOUND_RESPONSE = b"""\
HTTP/1.1 404 Not Found
Content-type: text/plain
Content-length: 9

Not Found""".replace(
    b"\n", b"\r\n"
)

METHOD_NOT_ALLOWED_RESPONSE = b"""\
HTTP/1.1 405 Method Not Allowed
Content-type: text/plain
Content-length: 17

Method Not Allowed""".replace(
    b"\n", b"\r\n"
)

SERVER_ROOT = os.path.abspath("www")

FILE_RESPONSE_TEMPLATE = """\
HTTP/1.1 200 OK
Content-type: {content_type}
Content-length: {content_length}

""".replace(
    "\n", "\r\n"
)


def iter_lines(
    sock: socket.socket, bufsize: int = 16384
) -> typing.Generator[bytes, None, bytes]:
    buff = b""
    while True:
        data = sock.recv(bufsize)
        if not data:
            return b""
        buff += data
        while True:
            try:
                i = buff.index(b"\r\n")
                line, buff = buff[:i], buff[i + 2 :]
                if not line:
                    return buff

                yield line
            except IndexError:
                break


def serve_file(sock: socket.socket, path: str) -> None:
    """Given a socket and the relative path to a file (relative to
    SERVER_SOCK), send that file to the socket if it exists.  If the
    file doesn't exist, send a "404 Not Found" response.
    """
    if path == "/":
        path = "/index.html"

    abspath = os.path.normpath(os.path.join(SERVER_ROOT, path.lstrip("/")))
    print(abspath)
    if not abspath.startswith(SERVER_ROOT):
        sock.sendall(NOT_FOUND_RESPONSE)
        return

    try:
        with open(abspath, "rb") as f:
            stat = os.fstat(f.fileno())
            content_type, encoding = mimetypes.guess_type(abspath)
            if content_type is None:
                content_type = "application/octet-stream"

            if encoding is not None:
                content_type += f"; charset={encoding}"

            response_headers = FILE_RESPONSE_TEMPLATE.format(
                content_type=content_type, content_length=stat.st_size
            ).encode("ascii")

            sock.sendall(response_headers)
            sock.sendfile(f)
    except FileNotFoundError:
        sock.sendall(NOT_FOUND_RESPONSE)
        return


class Request(typing.NamedTuple):
    method: str
    path: str
    headers: typing.Mapping[str, str]

    @classmethod
    def from_socket(cls, sock: socket.socket) -> "Request":

        lines = iter_lines(sock)
        try:
            request_line = next(lines).decode("ascii")
        except StopIteration:
            raise ValueError("Request line missing")

        try:
            method, path, _ = request_line.split(" ")
        except ValueError:
            raise ValueError(f"Malformed request line {request_line!r}.")

        headers = {}
        for line in lines:
            try:
                # partition?
                name, _, value = line.decode("ascii").partition(":")
                headers[name.lower()] = value.lstrip()
            except ValueError:
                raise ValueError(f"Malformed header line {line!r}.")

        return cls(method=method.upper(), path=path, headers=headers)


with socket.socket() as server_socket:
    # This tells the kernel to reuse sockets that are in `TIME_WAIT` state.
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server_socket.bind((HOST, PORT))
    # 0 is the number of pending connections the socket may have before
    # new connections are refused.  Since this server is going to process
    # one connection at a time, we want to refuse any additional connections.
    server_socket.listen(0)
    print(f"Listening on {HOST}: {PORT}...")

    while True:
        client_sock, client_addr = server_socket.accept()
        print(f"Received connection from {client_addr}...")
        with client_sock:
            try:
                request = Request.from_socket(client_sock)
                if request.method != "GET":
                    client_sock.sendall(METHOD_NOT_ALLOWED_RESPONSE)
                    continue

                serve_file(client_sock, request.path)
            except Exception as e:
                print(f"Failed to parse request: {e}")
                client_sock.sendall(BAD_REQUEST_RESPONSE)
