import os
# pipenv run pytest ./tests/test_full_model.py
INITIAL_PEERS = os.environ.get("INITIAL_PEERS")
# INITIAL_PEERS = '/dns/bootstrap1.petals.dev/tcp/31337/p2p/QmedTaZXmULqwspJXz44SsPZyTNKxhnnFvYRajfH7MGhCY' # works
# INITIAL_PEERS = '/ip4/127.0.0.1/tcp/31337/p2p/QmS9KwZptnVdB9FFV7uGgaTq4sEKBwcYeKZDfSpyKDUd1g'
print("INITIAL_PEERS", INITIAL_PEERS)
if not INITIAL_PEERS:
    raise RuntimeError("Must specify INITIAL_PEERS environment variable with one or more peer ids")
INITIAL_PEERS = INITIAL_PEERS.split()


MODEL_NAME = os.environ.get("MODEL_NAME")

if not MODEL_NAME:
    raise RuntimeError("Must specify MODEL_NAME as an index of a transformer block to be tested")

REF_NAME = os.environ.get("REF_NAME")

ADAPTER_NAME = os.environ.get("ADAPTER_NAME")
