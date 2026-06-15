#!/bin/bash
# Single key, human-like timing: tap F7 300 times
# (triangular sleep: min 0.5s, typical 0.8s, max 1.5s).
sudo python3 pi0key.py f7,sleep:.5:.8:1.5,repeat:300
