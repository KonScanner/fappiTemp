FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9


COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

COPY ./service /app

# Expose to 8080 from port container port 80
EXPOSE 8080:80