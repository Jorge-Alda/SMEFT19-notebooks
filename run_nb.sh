#!/usr/bin/env bash
poetry update && jupyter notebook --allow-root --no-browser --ip=0.0.0.0 --NotebookApp.token='' --NotebookApp.password=''
