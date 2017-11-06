#!/bin/bash
python urls.py && python lyric.py && cat lyrics/* > lyric.txt

