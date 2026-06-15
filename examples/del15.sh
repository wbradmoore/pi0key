#!/bin/bash
# Tap Delete about once a second for ~10 minutes (600 repeats).
sudo python3 pi0key.py del,sleep:1,repeat:600
