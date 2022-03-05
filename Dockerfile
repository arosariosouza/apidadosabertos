FROM ubuntu:20.04

ENV DEBUG=False
ENV HOST=0.0.0.0
ENV SQLALCHEMY_TRACK_MODIFICATIONS=False

LABEL Author="Allan Souza <allan.souza@saude.gov.br>"
LABEL Description="Container de execucao API de Dados Abertos - DEMAS"

WORKDIR /root
USER root

ADD app.py /root
ADD requirements.txt /root
ADD runtime.txt /root
ADD sql_alchemy.py /root

COPY templates/home.html /root/templates/home.html
COPY static/swagger.json /root/static/swagger.json

COPY models/__init__.py /root/models/__init__.py 
COPY models/estabelecimento.py /root/models/estabelecimento.py 
COPY models/tipo_unidade.py /root/models/tipo_unidade.py 

COPY resources/__init__.py /root/resources/__init__.py 
COPY resources/estabelecimento.py  /root/resources/estabelecimento.py 
COPY resources/tipo_unidade.py  /root/resources/tipo_unidade.py 

RUN apt update && apt -y install python3 python3-venv python3-pip && apt clean && pip install -r /root/requirements.txt

CMD ["/root/app.py"]
ENTRYPOINT ["/usr/bin/python3"]

EXPOSE 5000
