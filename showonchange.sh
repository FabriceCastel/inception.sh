#!/bin/bash

fswatch *.py | xargs -n1 ./showimg.sh
