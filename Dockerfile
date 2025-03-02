ARG PYTHON_VERSION=3.10.2

FROM flink:1.17.2-java11

RUN apt-get update -y && apt-get install -y python3 python3-pip python3-dev

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/app

WORKDIR /app

COPY process_mining_flink process_mining_flink
COPY resources resources
RUN --mount=type=cache,target=/root/.cache/pip \
    --mount=type=bind,source=requirements.txt,target=requirements.txt \
    python3 -m pip install -r requirements.txt

RUN ln -s /usr/bin/python3 /usr/bin/python
RUN wget -P /opt/flink/usrlib https://repo.maven.apache.org/maven2/org/apache/flink/flink-sql-connector-kafka/1.17.2/flink-sql-connector-kafka-1.17.2.jar

CMD python3 process_mining_flink/heuristics_miner_main.py
