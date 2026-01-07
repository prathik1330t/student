FROM python:3.11-slim

WORKDIR /student

RUN python -m pip install --upgrade pip
RUN python -m pip install pytest

COPY student.py .
COPY test_student.py .

ENTRYPOINT ["sh", "-c", "echo '===== Docker Test =====' && pytest -v && python student.py \"$@\"", "--"]
