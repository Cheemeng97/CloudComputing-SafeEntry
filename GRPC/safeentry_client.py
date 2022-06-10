# Copyright 2015 gRPC authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""The Python implementation of the GRPC helloworld.Greeter client."""

from __future__ import print_function

import logging

import grpc
import safeentry_pb2
import safeentry_pb2_grpc

def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel('localhost:50051') as channel:
        
        stub = safeentry_pb2_grpc.SafeEntryStub(channel)

        pass
        response = stub.Add(safeentry_pb2.Request(x=5, y=6))
        print("Check In Status" + str(response.res))

        #TODO: invoke the Sub() procedure and print the result
        pass

        #TODO: invoke the Multipy() procedure and print the result
        pass

        #TODO: invoke the Divide() procedure and print the result
        pass


if __name__ == '__main__':
    logging.basicConfig()
    run()
