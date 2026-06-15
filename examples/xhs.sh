#!/bin/bash
# Human-like alternation: F10 then F7, 300 times, with varied timing
# (triangular sleep: min 0.5s, typical 0.8s, max 1.5s).
sudo python3 pi0key.py f10,sleep:.5:.8:1.5,f7,sleep:.5:.8:1.5,repeat:300
