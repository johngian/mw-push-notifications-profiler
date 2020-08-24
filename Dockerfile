FROM python:3.8

# Install dependencies
RUN pip install pipenv
COPY Pipfile Pipfile.lock /tmp/
RUN cd /tmp && pipenv lock --requirements > requirements.txt
RUN pip install -r /tmp/requirements.txt

# Install local packages
RUN mkdir /code
COPY . /code
WORKDIR /code
RUN python setup.py install

CMD locust -f src/push_notifications.py
