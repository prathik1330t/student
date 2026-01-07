FROM python:3.11-slim

WORKDIR /student

# Upgrade pip
RUN python -m pip install --upgrade pip

# INSTALL PYTEST (THIS IS THE MISSING PART)
RUN python -m pip install pytest

# Copy application files
COPY student.py .
COPY test_student.py .

CMD ["pytest", "student.py"]
