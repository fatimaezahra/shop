FROM python:3.7.1
ENV PYTHONUNBUFFERED 1
RUN apt-get update ; apt-get --assume-yes install binutils libproj-dev gdal-bin

RUN wget http://download.osgeo.org/geos/geos-3.7.1.tar.bz2
RUN tar -xjf geos-3.7.1.tar.bz2
RUN cd geos-3.7.1; ./configure; make; make install

RUN wget http://download.osgeo.org/gdal/2.4.1/gdal-2.4.1.tar.gz
RUN tar -xzf gdal-2.4.1.tar.gz
RUN cd gdal-2.4.1; ./configure; make; make install

RUN mkdir /code
WORKDIR /code
ADD . /code/
RUN pip install -r requirements.txt

