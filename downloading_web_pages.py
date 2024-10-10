import socket


class URL:
    def __init__(self, url):
        self.scheme, url = url.split("://")
        if "/" not in url:
            url += "/"
        self.host, self.path = url.split("/", 1)  # only split the first time
        self.path = "/" + self.path

    def request(self):
        s = socket.socket(
            # address family
            family=socket.AF_INET,
            # arbitrary amounts of data
            type=socket.SOCK_STREAM,
            # network protocol
            proto=socket.IPPROTO_TCP,
        )
        s.connect((self.host, 80))
        # make request
        request = f"GET {self.path} HTTP/1.0\r\n"
        request += f"Host: {self.host}\r\n"
        # protocol specifies that we need to end with the blank line
        # without this, the request does not terminate!
        request += "\r\n"
        s.send(request.encode("utf8"))
        response = s.makefile("r", encoding="utf8", newline="\r\n")
        


url = URL("http://google.com/index.html")
print(f"scheme: {url.scheme}")
print(f"host: {url.host} \npath: {url.path}")

url.request()
