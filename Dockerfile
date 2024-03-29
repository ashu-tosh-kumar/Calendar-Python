# Setup Python and Pip
FROM python:3.11.1-bullseye
RUN pip install --upgrade pip

# Setup system packages
RUN apt-get update
RUN apt-get -y upgrade

# Setup working directory
WORKDIR /calendar-python

# Setup python packages
COPY requirements.txt .
# For faster installs
RUN pip install wheel
RUN pip install --default-timeout=100 --no-cache-dir -r requirements.txt

# Copy code
COPY ./api/ /calendar-python/api
COPY ./pyproject.toml /calendar-python/pyproject.toml
COPY ./tox.ini /calendar-python/tox.ini

# Provide access to script files
RUN chmod -R 777 api/src/scripts

# Setup the application
EXPOSE 8000
ENV PYTHONPATH=/calendar-python
ENTRYPOINT ["bash"]