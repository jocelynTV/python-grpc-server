# Python gRPC Server

## Installation

```bash
$ python3 -m pip install grpcio grpcio-tools
```

## Usage

```bash
# generate the stubs
$ python3 -m grpc_tools.protoc --proto_path=. ./user.proto --python_out=. --grpc_python_out=.

# run
$ python3 main.py
```


