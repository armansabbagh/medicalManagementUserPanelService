FROM python:3.8

ENV PORT=3000

RUN mkdir -p /opt/app
RUN mkdir -p /opt/app/pip_cache
COPY . /opt/app/
#COPY .pip_cache /opt/app/pip_cache/
WORKDIR /opt/app
#RUN pip install -r requirements.txt --cache-dir /opt/app/pip_cache
RUN pip install -r requirements.txt
RUN chmod +x /opt/app/start.sh
RUN chmod +x /opt/app/rmscript.sh

EXPOSE $PORT
#STOPSIGNAL SIGTERM
CMD ["/opt/app/rmscript.sh"]
CMD "/opt/app/start.sh" "$PORT"