FROM python:3.9
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
RUN apt-get -y update
RUN apt-get install -y google-chrome-stable
ENV APPROOT="/app"
WORKDIR $APPROOT
ADD . $APPROOT
RUN pip3 install pipenv
RUN pipenv install
RUN pipenv lock
RUN pipenv sync



