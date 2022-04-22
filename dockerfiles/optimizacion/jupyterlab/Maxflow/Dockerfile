FROM palmoreck/kale_certs:0.6.1
USER root

ENV PIP_PACKAGES_COMMON="MaxFlowAeiu==0.1.1 pytest networkx"

RUN pip3 install $PIP_PACKAGES_COMMON

RUN sed -i "s/# c.NotebookApp.password = u'sha1:115e429a919f:21911277af52f3e7a8b59380804140d9ef3e2380' .*/c.NotebookApp.password = u'argon2:$argon2id$v=19$m=10240,t=10,p=8$hnggGGwUhlYbm7qvS2LB6g$V+7MsXgO2uCT41cFEe82zA'/" ~/.jupyter/jupyter_notebook_config.py

VOLUME ["/shared_volume"]
