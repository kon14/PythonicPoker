import os
from setuptools import setup, find_packages
from setuptools.command.build_py import build_py
import subprocess


class GenerateGrpcClient(build_py):
    def run(self):
        print("Generating gRPC client code...")
        subprocess.check_call(["python3", os.path.join("pythonic_poker_sdk", "rpc", "generate.py")])
        super().run()


setup(
    name="pythonic-poker-sdk",
    version="0.1.0",
    # packages=find_packages(where="pythonic_poker_sdk"),
    py_modules=["pythonic_poker_sdk"],
    description="A RusticPoker client library SDK for Python 🐍.",
    author="Konstantinos Feretos",
    author_email="konferetos@tutanota.com",
    url="https://github.com/kon14/PythonicPoker",
    license_files = ("../LICENSE.md",),
    cmdclass={
        "build_py": GenerateGrpcClient,
    },
    install_requires=[
        "attrs==22.2.0",
        "build==0.10.0",
        "CacheControl==0.12.11",
        "certifi==2022.12.7",
        "cffi==1.15.1",
        "charset-normalizer==3.1.0",
        "cleo==2.0.1",
        "click==8.1.8",
        "crashtest==0.4.1",
        "cryptography==39.0.2",
        "distlib==0.3.6",
        "dulwich==0.21.3",
        "filelock==3.9.0",
        "grpcio==1.70.0",
        "grpcio-tools==1.70.0",
        "html5lib==1.1",
        "idna==3.4",
        "importlib-metadata==6.0.0",
        "installer==0.6.0",
        "jaraco.classes==3.2.3",
        "jeepney==0.8.0",
        "jsonschema==4.17.3",
        "keyring==23.13.1",
        "lockfile==0.12.2",
        "more-itertools==9.1.0",
        "msgpack==1.0.5",
        "packaging==23.0",
        "pexpect==4.8.0",
        "pipenv==2023.2.18",
        "pkginfo==1.9.6",
        "platformdirs==2.6.2",
        "poetry==1.4.0",
        "poetry-core==1.5.1",
        "poetry-plugin-export==1.3.0",
        "protobuf==5.29.3",
        "protoletariat==3.3.9",
        "ptyprocess==0.7.0",
        "pycparser==2.21",
        "pyproject_hooks==1.0.0",
        "pyrsistent==0.19.3",
        "rapidfuzz==2.15.1",
        "requests==2.28.2",
        "requests-toolbelt==0.10.1",
        "SecretStorage==3.3.3",
        "shellingham==1.5.0.post1",
        "tomlkit==0.11.6",
        "trove-classifiers==2023.3.9",
        "types-protobuf==5.29.1.20250208",
        "urllib3==1.26.15",
        "virtualenv==20.20.0",
        "virtualenv-clone==0.5.7",
        "webencodings==0.5.1",
        "zipp==3.15.0",
    ],
)
