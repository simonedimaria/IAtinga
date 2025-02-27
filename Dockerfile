FROM python:3.12-bookworm

# Install dependencies
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y supervisor ansible uuid-runtime \
    && rm -rf /var/lib/apt/lists/*

# add user
RUN useradd -ms /bin/bash IAtinga

# Add application
RUN mkdir -p /home/IAtinga/IAtinga
WORKDIR /home/IAtinga/IAtinga
RUN chown -R IAtinga:root /home/IAtinga/IAtinga

COPY challenge/requirements.txt .
# Install python dependencies as IAtinga
USER IAtinga
ENV PATH="${PATH}:/home/IAtinga/.local/bin"
ENV HOME="/home/IAtinga"
RUN pip install -r requirements.txt

# Download lm first-run dependencies
COPY config/lm_dependencies.py .
RUN python lm_dependencies.py
RUN rm lm_dependencies.py

# Add readflag binary
USER root
COPY flag.txt /root/flag.txt

# Setup superivsord
COPY config/supervisord.conf /etc/supervisord.conf

# Expose the port app is reachable on
EXPOSE 1337
EXPOSE 8888

# copy entrypoint script
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

COPY challenge .
# Run entrypoint script
CMD ["/entrypoint.sh"]
