#!/bin/bash

fswatch -0 *.py | xargs -n1 -0 ./showimg.sh
