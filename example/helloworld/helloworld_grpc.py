# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: helloworld/helloworld.proto
# plugin: grpclib.plugin.main
import abc

import grpclib.const
import grpclib.client

import helloworld.helloworld_pb2


class GreeterBase(abc.ABC):

    @abc.abstractmethod
    async def UnaryUnaryGreeting(self, stream):
        pass

    @abc.abstractmethod
    async def UnaryStreamGreeting(self, stream):
        pass

    @abc.abstractmethod
    async def StreamUnaryGreeting(self, stream):
        pass

    @abc.abstractmethod
    async def StreamStreamGreeting(self, stream):
        pass

    def __mapping__(self):
        return {
            '/helloworld.Greeter/UnaryUnaryGreeting': grpclib.const.Handler(
                self.UnaryUnaryGreeting,
                grpclib.const.Cardinality.UNARY_UNARY,
                helloworld.helloworld_pb2.HelloRequest,
                helloworld.helloworld_pb2.HelloReply,
            ),
            '/helloworld.Greeter/UnaryStreamGreeting': grpclib.const.Handler(
                self.UnaryStreamGreeting,
                grpclib.const.Cardinality.UNARY_STREAM,
                helloworld.helloworld_pb2.HelloRequest,
                helloworld.helloworld_pb2.HelloReply,
            ),
            '/helloworld.Greeter/StreamUnaryGreeting': grpclib.const.Handler(
                self.StreamUnaryGreeting,
                grpclib.const.Cardinality.STREAM_UNARY,
                helloworld.helloworld_pb2.HelloRequest,
                helloworld.helloworld_pb2.HelloReply,
            ),
            '/helloworld.Greeter/StreamStreamGreeting': grpclib.const.Handler(
                self.StreamStreamGreeting,
                grpclib.const.Cardinality.STREAM_STREAM,
                helloworld.helloworld_pb2.HelloRequest,
                helloworld.helloworld_pb2.HelloReply,
            ),
        }


class GreeterStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.UnaryUnaryGreeting = grpclib.client.UnaryUnaryMethod(
            channel,
            '/helloworld.Greeter/UnaryUnaryGreeting',
            helloworld.helloworld_pb2.HelloRequest,
            helloworld.helloworld_pb2.HelloReply,
        )
        self.UnaryStreamGreeting = grpclib.client.UnaryStreamMethod(
            channel,
            '/helloworld.Greeter/UnaryStreamGreeting',
            helloworld.helloworld_pb2.HelloRequest,
            helloworld.helloworld_pb2.HelloReply,
        )
        self.StreamUnaryGreeting = grpclib.client.StreamUnaryMethod(
            channel,
            '/helloworld.Greeter/StreamUnaryGreeting',
            helloworld.helloworld_pb2.HelloRequest,
            helloworld.helloworld_pb2.HelloReply,
        )
        self.StreamStreamGreeting = grpclib.client.StreamStreamMethod(
            channel,
            '/helloworld.Greeter/StreamStreamGreeting',
            helloworld.helloworld_pb2.HelloRequest,
            helloworld.helloworld_pb2.HelloReply,
        )
