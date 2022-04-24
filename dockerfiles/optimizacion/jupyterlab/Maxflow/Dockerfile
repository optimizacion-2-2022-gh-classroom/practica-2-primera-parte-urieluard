#dummy line to trigger build
FROM palmoreck/kale_certs:0.6.1
USER root

ENV PIP_PACKAGES_COMMON="MaxFlowAeiu==0.1.2 pytest networkx"

RUN pip3 install $PIP_PACKAGES_COMMON
RUN pip3 install numpy --upgrade


VOLUME ["/shared_volume"]

WORKDIR /

ENV NB_PREFIX myurl

ENTRYPOINT ["/usr/local/bin/jupyter", "lab", "--ip=0.0.0.0", "--no-browser", "--allow-root", "--LabApp.allow_origin='*'", "--LabApp.base_url=myurl"]