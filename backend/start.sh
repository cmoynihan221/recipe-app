#!/bin/bash
source venv/bin/activate
cd ..
uvicorn backend.main:app --reload
