FROM python:3.8
RUN python
RUN pip install requests
RUN pip install validators
ADD hackernews.py /
ENTRYPOINT [ "python", "./hackernews.py" ]
