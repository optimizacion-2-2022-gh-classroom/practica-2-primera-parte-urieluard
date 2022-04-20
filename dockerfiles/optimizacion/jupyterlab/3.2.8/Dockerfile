FROM ubuntu:20.04
USER root
ENV TIMEZONE America/Mexico_City
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV DEBIAN_FRONTEND noninteractive
ENV DEB_BUILD_DEPS="build-essential python3-dev python3-pip python3-setuptools software-properties-common libgit2-dev dirmngr libgmp3-dev libmpfr-dev"
ENV DEB_PACKAGES="sudo nano less time git curl wget htop graphviz gfortran libopenblas-dev"
ENV PIP_PACKAGES_COMMON="numpy scipy pandas matplotlib pytest networkx MaxFlowAeiu==0.1.1"
ENV PIP_PACKAGES_KALE="kubeflow-kale==0.6.1"
ENV JUPYTERLAB="jupyter-client==5.3.4 jupyterlab==2.3.2 qtconsole==5.2.1 nbconvert==5.6.1 jupyter-console==6.4.0 ipykernel==6.6.0 MarkupSafe==2.0.1"

#install app debian
RUN apt-get update && export $DEBIAN_FRONTEND && \
    echo $TIMEZONE > /etc/timezone && apt-get install -y tzdata

#install python
RUN apt-get update && apt-get install -y $DEB_BUILD_DEPS $DEB_PACKAGES && pip3 install --upgrade pip

# Install nodejs deps
RUN curl -sL https://deb.nodesource.com/setup_16.x | sudo -E bash - && apt-get install -y nodejs

RUN pip3 install $JUPYTERLAB

# excecute jypyter and set user and pass
RUN jupyter notebook --generate-config && sed -i "s/# c.NotebookApp.password = .*/c.NotebookApp.password = u'sha1:115e429a919f:21911277af52f3e7a8b59380804140d9ef3e2380'/" ~/.jupyter/jupyter_notebook_config.py

#install python package
RUN pip3 install $PIP_PACKAGES_COMMON
RUN pip install $PIP_PACKAGES_KALE --upgrade
RUN pip install --quiet "git+https://github.com/ITAM-DS/analisis-numerico-computo-cientifico.git#egg=opt&subdirectory=src"

RUN jupyter labextension install kubeflow-kale-labextension --minimize=False

VOLUME ["/shared_volume"]

WORKDIR /

ENV NB_PREFIX myurl

ENTRYPOINT ["/usr/local/bin/jupyter", "lab", "--ip=0.0.0.0", "--no-browser", "--allow-root", "--LabApp.allow_origin='*'", "--LabApp.base_url=myurl"]
