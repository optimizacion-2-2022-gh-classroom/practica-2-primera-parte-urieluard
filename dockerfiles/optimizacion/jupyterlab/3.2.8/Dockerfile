#dummy line to trigger build
FROM palmoreck/kale_certs:0.6.1
USER root


COPY requirements.txt .
RUN pip3 install --requirement requirements.txt
RUN pip install --quiet "git+https://github.com/optimizacion-2-2022-gh-classroom/practica-1-segunda-parte-LuzVerde23.git#egg=MaxFlowAeiu&subdirectory=src"

VOLUME ["/shared_volume"]

WORKDIR /

ENV NB_PREFIX myurl

ENTRYPOINT ["/usr/local/bin/jupyter", "lab", "--ip=0.0.0.0", "--no-browser", "--allow-root", "--LabApp.allow_origin='*'", "--LabApp.base_url=myurl"]
