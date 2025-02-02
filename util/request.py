class Request:

    def __init__(self, request: bytes):
        # TODO: parse the bytes of the request and populate the following instance variables

        #self.parse(request)

        self.body = b""
        self.method = ""
        self.path = ""
        self.http_version = ""
        self.headers = {}
        self.cookies = {}

        self.parse(request)

    def parse(self, request):
        #converts bits to string
        decodedstring = request.decode() #by default is utf-8
        decodedstring = decodedstring.split("\r\n")


        # THIS SECTION IS FOR REQUEST LINE 
        requestline = decodedstring[0].split()
        self.method = requestline[0]
        self.path = requestline[1]
        self.http_version = requestline[2]

        decodedstring.pop(0) #remove the request line from decoded string after use
        

        # THIS SECTION IS FOR HEADERS
        while((header:=decodedstring.pop(0)) != ""): #this pops the first element off list and assigns it to 'header'
            header = header.split(": ", 1) #only split on the first occurse of ": " to denote key-value pair
            self.headers[header[0]] = header[1]

        
        # THIS SECTION IS FOR BODY
        self.body = decodedstring[0].encode() #body should be remaining string, encode to utf-8


def test1():
    request = Request(b'GET / HTTP/1.1\r\nHost: localhost:8080\r\nConnection: keep-alive\r\n\r\n')
    assert request.method == "GET"
    assert "Host" in request.headers
    assert request.headers["Host"] == "localhost:8080"  # note: The leading space in the header value must be removed
    assert request.body == b""  # There is no body for this request.
    # When parsing POST requests, the body must be in bytes, not str

    # This is the start of a simple way (ie. no external libraries) to test your code.
    # It's recommended that you complete this test and add others, including at least one
    # test using a POST request. Also, ensure that the types of all values are correct

def test2():
    request = Request(b'GET / HTTP/1.1\r\nHost: localhost:8080\r\nConnection: keep-alive\r\n\r\nhello body')
    assert request.method == "GET"
    assert "Host" in request.headers
    assert request.headers["Host"] == "localhost:8080"  # note: The leading space in the header value must be removed
    assert request.body == b"hello body"  # There is no body for this request

if __name__ == '__main__':
    test1()
    test2()
