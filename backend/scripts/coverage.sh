#!/usr/bin/env bash
coverage run --source './api' -m unittest -v | coverage report | coverage html