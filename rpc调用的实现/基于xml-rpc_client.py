import xmlrpc.client
server=xmlrpc.client.ServerProxy("http://localhost:8088")
server.add(2,3)