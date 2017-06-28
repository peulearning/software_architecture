'''
*************************************************
*              IFNMG - Campus Januária          *
*                       TADS                    *
*              Arquitetura de Software          *
*************************************************

Servidor de venda XML-RPC em Python 3.

'''

__project_name__ = 'IFNMG - Januária - TADS - Arquitetura de Software'
__author__ = 'Prof. Danilo Nunes <danilo.nunes@ifnmg.edu.br>'
__updated__ = '2017-06-28T10:47:57.531741'
__source__ = 'https://github.com/danilonunes/arquitetura/tree/master/python/exemplos/xmlrpc'

from xmlrpc.server import SimpleXMLRPCServer


server = SimpleXMLRPCServer(("localhost", 8000))

print("Listening on port 8000...")
server.register_function(is_even, "is_even")
server.serve_forever()