#!/usr/bin/env python
# Example of how to get number of block from your running node. Using python-bitcoinlib library to simplify API access. We need a BTC Core instance up and running

from bitcoin.rpc import RawProxy

# Create a connection to BTC Core Node

p = RawProxy()

info = p.getblockchaininfo()

print(info["blocks"])