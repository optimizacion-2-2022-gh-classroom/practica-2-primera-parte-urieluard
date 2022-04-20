FROM ubuntu:20.04
USER root
ENV TIMEZONE America/Mexico_City
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV DEBIAN_FRONTEND noninteractive
ENV DEB_PACKAGES="sudo nano less time git curl wget htop graphviz gfortran libopenblas-dev"
ENV PIP_PACKAGES_KALE="kubeflow-kale==0.6.1"
#
#install app debian
RUN apt-get update && export $DEBIAN_FRONTEND && \
    echo $TIMEZONE > /etc/timezone && apt-get install -y tzdata

#install python
RUN apt-get update && apt-get install -y $DEB_BUILD_DEPS $DEB_PACKAGES && pip3 install --upgrade pip

# Install nodejs deps
RUN curl -sL https://deb.nodesource.com/setup_16.x | sudo -E bash - && apt-get install -y nodejs

RUN pip3 install jupyter "jupyterlab>=2.0.0,<3.0.0" --upgrade

# excecute jypyter and set user and pass
RUN jupyter notebook --generate-config && \
    sed -i "s/# c.NotebookApp.password = .*/c.NotebookApp.password = u'sha1:115e429a919f:21911277af52f3e7a8b59380804140d9ef3e2380'/" ~/.jupyter/jupyter_notebook_config.py

#install python package
RUN pip install $PIP_PACKAGES_KALE --upgrade

RUN jupyter labextension install kubeflow-kale-labextension --minimize=False

COPY requirements.txt .
RUN pip3 install --requirement requirements.txt
COPY . .

RUN git clone https://github.com/optimizacion-2-2022-gh-classroom/practica-1-segunda-parte-LuzVerde23.git

VOLUME ["/shared_volume"]

WORKDIR /

ENV NB_PREFIX myurl

ENTRYPOINT ["/usr/local/bin/jupyter", "lab", "--ip=0.0.0.0", "--no-browser", "--allow-root", "--LabApp.allow_origin='*'", "--LabApp.base_url=myurl"]
