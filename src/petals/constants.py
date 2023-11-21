import torch

# PUBLIC_INITIAL_PEERS = [
#     # IPv4 DNS addresses
#     "/dns/bootstrap1.petals.dev/tcp/31337/p2p/QmedTaZXmULqwspJXz44SsPZyTNKxhnnFvYRajfH7MGhCY",
#     "/dns/bootstrap2.petals.dev/tcp/31338/p2p/QmQGTqmM7NKjV6ggU1ZCap8zWiyKR89RViDXiqehSiCpY5",
#     # IPv6 DNS addresses
#     "/dns6/bootstrap1.petals.dev/tcp/31337/p2p/QmedTaZXmULqwspJXz44SsPZyTNKxhnnFvYRajfH7MGhCY",
#     "/dns6/bootstrap2.petals.dev/tcp/31338/p2p/QmQGTqmM7NKjV6ggU1ZCap8zWiyKR89RViDXiqehSiCpY5",
#     # Reserved IPs
#     "/ip4/159.89.214.152/tcp/31337/p2p/QmedTaZXmULqwspJXz44SsPZyTNKxhnnFvYRajfH7MGhCY",
#     "/ip4/159.203.156.48/tcp/31338/p2p/QmQGTqmM7NKjV6ggU1ZCap8zWiyKR89RViDXiqehSiCpY5",
# ]
PUBLIC_INITIAL_PEERS = [
  '/ip4/172.20.54.234/tcp/42041/p2p/12D3KooWGdHnpGihG8A5tuCYApxybH6q4SqJs64zhzoWwcWo24Bw', 
  '/ip4/127.0.0.1/tcp/42041/p2p/12D3KooWGdHnpGihG8A5tuCYApxybH6q4SqJs64zhzoWwcWo24Bw', 
  '/ip6/::1/tcp/38191/p2p/12D3KooWGdHnpGihG8A5tuCYApxybH6q4SqJs64zhzoWwcWo24Bw'
]

# The reachability API is currently used only when connecting to the public swarm
REACHABILITY_API_URL = "https://health.petals.dev"

DTYPE_MAP = dict(bfloat16=torch.bfloat16, float16=torch.float16, float32=torch.float32, auto="auto")
