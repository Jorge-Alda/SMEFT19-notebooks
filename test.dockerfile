FROM jupyter/datascience-notebook

COPY environment.yml /tmp/
RUN mamba install --quiet --yes gcc && \
    mamba env create -f /tmp/environment.yml && \
    mamba clean --all -f -y && \
    fix-permissions "${CONDA_DIR}" && \
    fix-permissions "/home/${NB_USER}"

COPY . /home/jovyan/work/
SHELL ["conda", "run", "-n", "test", "/bin/bash", "-c"]