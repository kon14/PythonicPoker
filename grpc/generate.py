#!/usr/bin/env python3

import os
import subprocess
from urllib.request import urlretrieve

PATH_ROOT = os.path.dirname(os.path.abspath(__file__))

PROTO_FETCH_URL = "https://raw.githubusercontent.com/kon14/RusticPoker/refs/heads/main/proto/rustic_poker.proto"
PROTO_DIR_PATH  = f"{PATH_ROOT}/proto"
PROTO_NAME      = "rustic_poker.proto"
PROTO_GEN_PATH  = f"{PATH_ROOT}/../app/rpc/gen"


def fetch_proto_file():
    try:
        os.makedirs(PROTO_DIR_PATH, exist_ok=True)
        urlretrieve(PROTO_FETCH_URL, f"{PROTO_DIR_PATH}/{PROTO_NAME}")
        print("Proto file downloaded successfully!")
    except Exception as err:
        print(f"Failed to download proto file from: {PROTO_FETCH_URL}")
        print(err)


def generate_grpc_client():
    subprocess.run(f"mkdir -p {PROTO_GEN_PATH}", shell=True, capture_output=True, text=True)

    gen_cmd = f"python3 -m grpc_tools.protoc -I{PROTO_DIR_PATH} --python_out={PROTO_GEN_PATH} --pyi_out={PROTO_GEN_PATH} --grpc_python_out={PROTO_GEN_PATH} {PROTO_DIR_PATH}/{PROTO_NAME}"
    r = subprocess.run(gen_cmd, shell=True, capture_output=True, text=True)
    if r.returncode != 0:
        print("Error creating 'gen' directory:\n", r.stderr)

    # # https://github.com/protocolbuffers/protobuf/issues/1491
    # # https://github.com/cpcloud/protoletariat
    fix_gen_cmd = f"python3 -m protoletariat --create-package --in-place --python-out {PROTO_GEN_PATH} protoc --proto-path={PROTO_DIR_PATH} {PROTO_NAME}"
    r = subprocess.run(fix_gen_cmd, shell=True, capture_output=True, text=True)
    if r.returncode != 0:
        print("Error creating 'gen' directory:\n", r.stderr)

    print("gRPC client code generated successfully!")


fetch_proto_file()

generate_grpc_client()
