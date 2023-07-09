FROM python:3.10

WORKDIR /src

# Install 'gcc', 'g++', 'musl-dev', 'libffi-dev', and other necessary tools
# RUN apt-get update && apt-get install -y --no-install-recommends gcc g++ libffi-dev

COPY ./requirements.txt /src
RUN pip install --no-cache-dir -r requirements.txt

COPY . /src

CMD [ "streamlit", "run", "app.py" ]