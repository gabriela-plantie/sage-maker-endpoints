FROM python:3.9.1

RUN apt-get update -y && apt-get install -y libev-dev
RUN pip install bottle
RUN pip install bjoern
RUN pip install pandas==1.2.2
RUN pip install numpy==1.20.1
RUN pip install catboost==0.24.4

RUN mkdir -p /opt/program
RUN mkdir -p /opt/ml

ENV PYTHONUNBUFFERED=TRUE
ENV PYTHONDONTWRITEBYTECODE=TRUE
ENV PATH="/opt/program:${PATH}"
ENV MODEL_PATH='/opt/ml'

COPY app.py /opt/program
COPY model.py /opt/ml
COPY model.pkl /opt/ml
COPY predictors.csv /opt/ml
COPY to_cat.csv /opt/ml

WORKDIR /opt/program

ENTRYPOINT ["python", "app.py"]
