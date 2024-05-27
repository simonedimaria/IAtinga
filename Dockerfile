FROM python:3.8.18-bookworm

# install dependencies
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y supervisor gcc \
    && rm -rf /var/lib/apt/lists/*

# add user
RUN useradd -ms /bin/bash chrono

# add application
RUN mkdir -p /home/chrono/chrono-mind
WORKDIR /home/chrono/chrono-mind
COPY challenge .
RUN chown -R chrono:root /home/chrono/chrono-mind

# install python dependencies as chrono
USER chrono
ENV PATH="${PATH}:/home/chrono/.local/bin"
ENV HOME="/home/chrono"
RUN pip install -r requirements.txt

# download lm first-run dependencies
COPY config/lm_dependencies.py .
RUN python lm_dependencies.py
RUN rm lm_dependencies.py

# add readflag binary
USER root
COPY flag.txt /root/flag
COPY config/readflag.c /
RUN gcc -o /readflag /readflag.c && chmod 4755 /readflag && rm /readflag.c

# setup superivsord
COPY config/supervisord.conf /etc/supervisord.conf

# expose the port app is reachable on
EXPOSE 1337

# copy entrypoint script
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# run entrypoint script
CMD ["/entrypoint.sh"]
