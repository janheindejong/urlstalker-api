#!/bin/bash

set -ex

export PREFIX=".venv/bin/"
export SOURCE_FILES="urlstalker tests"

${PREFIX}autoflake --in-place --recursive $SOURCE_FILES
${PREFIX}isort $SOURCE_FILES
${PREFIX}black $SOURCE_FILES