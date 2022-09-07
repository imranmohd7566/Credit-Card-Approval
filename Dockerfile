FROM continuumio/anaconda3:4.4.0

WORKDIR /usr/app/
COPY . /usr/app/
RUN pip install -r requirements.txt
COPY . /usr/app/
EXPOSE 5000
CMD ["python", "app.py"]