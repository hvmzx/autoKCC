FROM python:3.10
WORKDIR .
RUN git clone https://github.com/ciromattia/kcc.git
RUN python -m pip install --upgrade pip
RUN apt-get update && apt-get install -y --no-install-recommends python3 python3-dev python3-pip libpng-dev libjpeg-dev p7zip-full python3-pyqt5 unrar-free libgl1
RUN pip install Cmake watchdog
RUN pip install -r kcc/requirements.txt
RUN wget https://archive.org/download/kindlegen_linux_2_6_i386_v2_9/kindlegen_linux_2.6_i386_v2_9.tar.gz
RUN tar -xf kindlegen_linux_2.6_i386_v2_9.tar.gz "kindlegen"  
RUN cp -R 'kindlegen' '/usr/local/bin/'
RUN chmod +rwx '/usr/local/bin/kindlegen'
RUN rm kindlegen_linux_2.6_i386_v2_9.tar.gz

COPY . .
CMD [ "python", "-u", "./main.py"]