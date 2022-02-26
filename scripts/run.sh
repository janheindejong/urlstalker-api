#!/bin/bash

.venv/bin/uvicorn urlstalker.app:app --port 8000 --host localhost
