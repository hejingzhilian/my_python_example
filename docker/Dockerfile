FROM ubuntu:20.04  

# Edit with mysql-client, postgresql-client, sqlite3, etc. for your needs.
# Or delete entirely if not needed.
#RUN apt-get update \
#    && apt-get install -y --no-install-recommends \
#        postgresql-client \
#    && rm -rf /var/lib/apt/lists/*
#
#WORKDIR /usr/src/app
#
#COPY requirements.txt /usr/src/app/
#RUN pip install --no-cache-dir -r requirements.txt
#
#COPY . /usr/src/app
#
## For Django
#EXPOSE 8000
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
#
## For some other command
# CMD ["python", "app.py"]

RUN useradd -ms /bin/bash -u 1014 shishuai
USER shishuai
WORKDIR /home/shishuai/
RUN mkdir /home/shishuai/.ssh
COPY ./authorized_keys /home/shishuai/.ssh/

USER root
WORKDIR /
RUN apt update --fix-missing
RUN apt install vim openssh-server -y
RUN apt install git -y
RUN apt install pip -y
RUN apt install python3.9 -y
RUN echo "UsePAM no" >> /etc/ssh/sshd_config
RUN echo "PermitRootLogin yes" >> /etc/ssh/sshd_config
#RUN echo "AllowTcpForwarding yes" >> /etc/ssh/sshd_config
RUN chown -R shishuai:shishuai /home/shishuai/.ssh
RUN service ssh start

USER shishuai
WORKDIR /home/shishuai/

CMD ["bash","-c", "echo $HOME"]

