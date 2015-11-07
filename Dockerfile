#sudo docker build -t nlarusso/test-api .

#docker run --name test -p 5000:5000 -v /opt/devops/test-api/:/opt/data_services/test-api -d nlarusso/test-api

FROM ubuntu:14.04
MAINTAINER nlarusso

# Install Python Setuptools
RUN apt-get update && apt-get install -y gcc python-setuptools python-psycopg2 && easy_install pip

ENV SRC /opt/data_services/
ENV NAME test-api

RUN mkdir -p /tmp/gunicorn/
RUN mkdir -p $SRC/$NAME

# Install requirements.txt
ADD requirements.txt $SRC/requirements.txt
RUN cd $SRC; pip install -r requirements.txt

EXPOSE 5000
# EXPOSE PORT

VOLUME ["/tmp/"]

WORKDIR $SRC/$NAME/src/

# Run the Flask APP
CMD ["gunicorn", "--workers=4", "--bind=0.0.0.0:5000", "--error-logfile=/tmp/gunicorn/error.log", "--access-logfile=/tmp/gunicorn/access.log", "app:APP"]

