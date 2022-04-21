FROM sancas96/docker_kale:0.1

USER root
#
RUN pip install --quiet "git+https://github.com/optimizacion-2-2022-gh-classroom/practica-1-segunda-parte-LuzVerde23.git#egg=MaxFlowAeiu&subdirectory=src"

VOLUME ["/shared_volume"]

WORKDIR /

ENV NB_PREFIX myurl

ENTRYPOINT ["/usr/local/bin/jupyter", "lab", "--ip=0.0.0.0", "--no-browser", "--allow-root", "--LabApp.allow_origin='*'", "--LabApp.base_url=myurl"]
