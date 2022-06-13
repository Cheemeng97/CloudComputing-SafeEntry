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
"""The Python implementation of the GRPC helloworld.Greeter server."""

from concurrent import futures
import logging

import grpc
import calculator_pb2
import calculator_pb2_grpc


class Calculator(calculator_pb2_grpc.CalculatorServicer):


  def Add(self, request, context):
    return calculator_pb2.Reply(res=request.x + request.y)

  def Sub(self, request, context):
    return calculator_pb2.Reply(res=request.x - request.y)

  def Multiply(self, request, context):
    return calculator_pb2.Reply(res=request.x * request.y)

  def Divide(self, request, context):
    return calculator_pb2.Reply(res=request.x / request.y)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    calculator_pb2_grpc.add_CalculatorServicer_to_server(Calculator(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
