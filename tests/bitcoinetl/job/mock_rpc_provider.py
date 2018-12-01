# MIT License
#
# Copyright (c) 2018 Omidiora Samuel, samparsky@gmail.com
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


import json

class MockRPCProvider():
    def __init__(self, read_resource):
        self.read_resource = read_resource

    def make_request(self, data):
        rpc_response = []
        for req in data:
            method = req[0]
            if method == 'getblock':
                blockhash = req[1]
                verbosity = req[2]
                file_name = 'rpc_response_{}_{}_{}.json'.format(method, blockhash, verbosity)
            elif method == 'getblockhash':
                height = req[1]
                file_name = 'rpc_response_{}_{}.json'.format(method, height)
            elif method == 'getrawtransaction':
                txid = req[1]
                file_name = 'rpc_response_{}_{}.json'.format(method, txid)
            else:
                raise ValueError('Request method {} is unexpected'.format(method))
            file_content = self.read_resource(file_name)
            rpc_response.append(json.loads(file_content))
        return rpc_response
    
    def getblock(self, blockhash, verbosity):
        file_name = 'rpc_response_{}_{}_{}.json'.format("geblock", blockhash, verbosity)
        file_content = self.read_resource(file_name)
        return json.loads(file_content)
    
    def getblockcount(self):
        pass
        # file_name = 'rpc_response_{}_{}_{}.json'.format("geblock", blockhash, verbosity)
        # file_content = self.read_resource(file_name)
        # return json.loads(file_content)
    
    def getblockhash(self, block_height):
        file_name = 'rpc_response_{}_{}.json'.format("getblockhash", block_height)
        file_content = self.read_resource(file_name)
        return json.loads(file_content)