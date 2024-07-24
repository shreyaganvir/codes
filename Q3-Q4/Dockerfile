FROM python:3.9.10-slim-buster

WORKDIR /minirestapi

RUN apt-get update && apt-get install -y netcat
# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /minirestapi/
# Install any needed packages specified in requirements.txt
RUN pip3 install -r requirements.txt

# copy project
COPY entrypoint.sh /minirestapi
RUN chmod u+x /minirestapi/entrypoint.sh

COPY api.py /minirestapi
COPY app /minirestapi/app
COPY .env /minirestapi


#CMD ["/bin/cat", "/minirestapi/entrypoint.sh"]

# Make port 5000 available to the world outside this container
EXPOSE 5000

# run entrypoint.sh
CMD ["/bin/bash", "/minirestapi/entrypoint.sh"]

#CMD ["/bin/echo", "hello!!"]
#CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
#CMD ["flask", "run", "--host=0.0.0.0"]