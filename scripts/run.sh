#!/bin/bash

export PREFIX=".venv/bin/"

${PREFIX}uvicorn urlstalker.app:app --port 8000 --host localhost
