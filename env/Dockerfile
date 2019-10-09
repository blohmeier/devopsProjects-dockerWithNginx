FROM alpine:3.1

# Update
RUN apk add --update python py-pip

# Install app dependencies
RUN pip install Flask

# Bundle app source
COPY simpleapp.py /src/capstoneapp.py

EXPOSE  8000
CMD ["python", "/src/capstoneapp.py", "-p 8000"]