FROM python:3.9

WORKDIR /minirestapi

COPY api.py /minirestapi
COPY ./app /minirestapi/app
COPY .env /minirestapi
COPY requirements.txt /minirestapi/

# Install any needed packages specified in requirements.txt
RUN pip3 install --upgrade pip
RUN pip3 install --no-cache-dir -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

ENV SQLALCHEMY_DATABASE_URI=postgresql://shreyaliganvir:postgres@postgres/postgres
# Run flask application
#ENTRYPOINT ["python3", "api.py"]