import xmlrpc.client

server = xmlrpc.client.ServerProxy('http://localhost:8000')

num1 = 1995
num2 = 2208

result = server.add(num1, num2)

print(f"Result: {result}")