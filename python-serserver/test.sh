#!/bin/bash

echo '{"rv":128, "rh":128, "lv":128, "lh":200, "b0":0, "b1":0, "b2":0, "b3":1, "b4":1, "b5":1, "b6":1, "b7":1}' | nc -v euclid 9999
