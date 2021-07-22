from xmlrpc.server import SimpleXMLRPCServer
from models import Product
import xmlrpc.client
def sayHello():
    return 'Hello World From XMLRPCSrver'
server=SimpleXMLRPCServer(("localhost",8002))
print("server is listening on port 80000")
server.register_function(sayHello,"sayHello")
server.serve_forever()
