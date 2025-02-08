<div align="center">
<br>
<a href="https://github.com/kon14/RusticPoker" target="_blank">
    <h1>PythonicPoker 🃏</h1>
</a>
<h3>A reference client implementation of <a href="https://github.com/kon14/RusticPoker" target="_blank"><strong>PythonicPoker</strong></a></h3>
</div>

<hr />

This is a reference implementation of a gRPC Python 🐍 client for interacting with the RusticPoker server.

For more details on the server, including the gRPC server implementation and the .proto file, please visit the RusticPoker's [main repository](https://github.com/kon14/RusticPoker).

---

## Building 🔨 <a name="building"></a>

``` bash
# Dependency Installation
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# gRPC Client Code Generation
python3 grpc/generate.py
```

## Running 💻 <a name="running"></a>

``` bash
# With Predefined Connection Details
SERVER_URL=0.0.0.0:55100 PEER_ADDRESS=192.168.1.20 python3 app/main.py

# Without Predefined Connection Details
python3 app/main.py
```

---

## Documentation 📚 <a name="documentation"></a>

Check out the [RusticPoker documentation](https://github.com/kon14/RusticPoker#documentation--).

## Environment Variables 📃 <a name="env-vars"></a>

|    Variable    | Description                                                         | Required | Default |     Example     |
|:--------------:|:--------------------------------------------------------------------|:--------:|:-------:|:---------------:|
|  `SERVER_URL`  | Specifies the `RusticPoker` game server URL to connect to.          |  False   |    -    | `0.0.0.0:55100` |
| `PEER_ADDRESS` | Specifies the peer address to be used for player identity spoofing. |  False   |    -    | `192.168.1.20`  |
