#!/bin/bash

export PREFIX=".venv/bin/"

${PREFIX}alembic upgrade head
