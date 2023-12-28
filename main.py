from concurrent import futures
import logging

import grpc
import user_pb2
import user_pb2_grpc


class User(user_pb2_grpc.UserService):
    def CreateUser(self, request, context):
        name = request.name
        email = request.email
        result = {'name': name, 'email': email}
        return user_pb2.UserResponse(**result)


def serve():
    port = "50051"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    user_pb2_grpc.add_UserServiceServicer_to_server(User(), server)
    server.add_insecure_port("[::]:" + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    serve()
