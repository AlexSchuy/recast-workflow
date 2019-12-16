#!/bin/bash
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
export PYTHONPATH=$(realpath $DIR/..)
export WORKON_HOME=$HOM$E/.local/share/.virtualenvs