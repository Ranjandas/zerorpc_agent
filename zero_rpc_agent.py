#!/usr/bin/env python
import socket
import zerorpc

class KickBackServer(object):
    def test_connectivity(self,dest_ip, port, proto):
    if(proto == "TCP"):
        proto_type = socket.SOCK_STREAM
    elif(proto == "UDP"):
        proto_type = socket.SOCK_DGRAM

    sock = socket.socket(socket.AF_INET, proto_type)
    sock.settimeout(10)
    status = sock.connect_ex((dest_ip, port))
    sock.close()
    print str(dest_ip) + " : " + str(port) + " : " + proto + " : " + str(status)
    return status
    
    def get_firewall_status(self, destination_ip, port, protocol):
        print destination_ip, port
        status = self.test_connectivity(destination_ip, port, protocol)
       
        # return connection_status
        return status

s = zerorpc.Server(KickBackServer())
s.bind('tcp://0.0.0.0:4242')
s.run()
