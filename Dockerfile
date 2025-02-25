FROM python:3.11
RUN mkdir /src
WORKDIR /src
ADD . /src
RUN pip install -r requirements.txt
CMD ["python", "api_model_2.py"]
EXPOSE 5000