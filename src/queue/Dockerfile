FROM arm64v8/amazoncorretto:20-alpine-full

RUN yum install -y which wget gzip tar && wget -O activemq.tar.gz http://archive.apache.org/dist/activemq/5.18.1/apache-activemq-5.18.1-bin.tar.gz

RUN tar -xzf activemq.tar.gz

ENV JAVA_HOME=/usr/bin/

CMD ["apache-activemq-5.18.1/bin/activemq", "console"]
