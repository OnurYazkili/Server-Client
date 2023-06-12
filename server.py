from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

class CalculatorService:
    def add(self, num1, num2):
        return num1 + num2

server = SimpleXMLRPCServer(('localhost', 8000),
                            requestHandler=RequestHandler)
server.register_instance(CalculatorService())

print('Calculator service is running...')
server.serve_forever()