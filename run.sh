#!/bin/bash
uvicorn legalEaseAPI.main:app --reload &
streamlit run frontend/app.py