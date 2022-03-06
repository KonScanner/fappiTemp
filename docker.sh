#!/bin/bash
docker build --pull --rm -f "Dockerfile" -t dockerfappi:latest .
docker run --rm -d  -p 80:80/tcp dockerfappi:latest