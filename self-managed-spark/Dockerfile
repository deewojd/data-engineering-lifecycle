FROM apache/spark:4.0.1

USER root

ENTRYPOINT []

ENV JAVA_HOME=/opt/java/openjdk
ENV SPARK_HOME=/opt/spark
ENV PATH="${JAVA_HOME}/bin:${SPARK_HOME}/bin:${PATH}"

RUN pip install --no-cache-dir pandas duckdb

USER spark
