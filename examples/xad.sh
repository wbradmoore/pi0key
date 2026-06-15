#!/bin/bash
# Slow rotation: cycle F6 -> F7 -> F8 with ~30s between each, 29 times (~45 min total).
sudo python3 pi0key.py f6,sleep:30,f7,sleep:30,f8,sleep:30,repeat:29
