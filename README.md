# Jupyter Notebooks used for Chapters 6 and 7 of my PhD Thesis



[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.5782809.svg)](https://doi.org/10.5281/zenodo.5782809) [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/Jorge-Alda/SMEFT19-notebooks/HEAD)


In these pages you will find the `jupyter` notebooks that are needed to fully reproduce the results of chapters 6 and 7, about various applications of the Standard Model Effective Field Theory to investigate the _B_-meson anomalies and their relation to other observables.

For the source code, go to https://github.com/Jorge-Alda/SMEFT19
and to download the notebooks, go to https://github.com/Jorge-Alda/SMEFT19-notebooks

This code was used for the following papers:
* Jorge Alda, Jaume Guasch, Siannah Penaranda, *Anomalies in B mesons decays: A phenomenological approach*. [![](https://img.shields.io/badge/arXiv-2012.14799-00ff00)](https://arxiv.org/abs/2012.14799)
* Jorge Alda, Jaume Guasch, Siannah Penaranda, *Anomalies in B mesons decays: Present status and future collider prospects*. Contribution to [LCWS2021](https://www.slac.stanford.edu/econf/C2103151/). [![](https://img.shields.io/badge/arXiv-2105.05095-00ff00)](https://arxiv.org/abs/2105.05095)
* Jorge Alda, Jaume Guasch, Siannah Penaranda, *Using Machine Learning techniques in phenomenological studies in flavour physics*. [![](https://img.shields.io/badge/arXiv-2109.07405-00ff00)](https://arxiv.org/abs/2109.07405)
* Jorge Alda, Jaume Guasch, Siannah Penaranda, *Exploring B-physics anomalies at colliders*. Contribution to [EPS-HEP2021](https://www.eps-hep2021.eu/). [![](https://img.shields.io/badge/arXiv-2110.12240-00ff00)](https://arxiv.org/abs/2110.12240)

## Contents

* [Section 6.2](PaperSMEFT/README.md)
* [Section 6.3](PaperILC/README.md)
* [Chapter 7](PaperML/README.md)

## How to run the notebooks

### Run on-line

The simplest way to run the notebooks is by visiting [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/Jorge-Alda/SMEFT19-notebooks/HEAD)

Click on `demo.ipynb` to see a simple example, or navigate the folders to run the code [Be careful! Binder might impose CPU limits for long computations].

You can save any generated files with the menu File > Download. All files will be lost after shutting down Binder.

### Run on your computer

The cleanest way to run the notebooks is using the [Docker](https://docs.docker.com/engine/install/) container. In this way you always have the right version of each packaging without interfering with the rest of your system. To get the [container](https://hub.docker.com/repository/docker/jorgealda/smeft19-notebooks) use the command (only the first time, may take a while)

```bash
docker pull jorgealda/smeft19-notebooks
```

and to start it

```bash
docker run -p 8888:8888 jorgealda/smeft19-notebooks
```

Copy the url that will appear at the bottom of the terminal and open it in your favourite browser.

Click on `demo.ipynb` to see a simple example, or navigate the folders to run the code. You can save any generated files with the menu File > Download.

Using File > Shut Down closes the JupyterLab and **deletes the current container**, so don't do this if you want to come back. If you just want to temporally stop the container, open another terminal and type

```bash
docker ps -a | grep smeft19-notebooks
```

and you will get something like this

```txt
068d5ecc684e   jorgealda/smeft19-notebooks           "/usr/local/bin/repo…"   43 seconds ago   Up 37 seconds            0.0.0.0:8888->8888/tcp, :::8888->8888/tcp   agitated_wiles
```

The first hexadecimal digits, `068d5ecc684e` in this case, are the ID of the running container (yours will be different). You can stop the container using

```bash
docker stop 068d5ecc684e
```

To restart the container, use

```bash
docker start 068d5ecc684e && docker attach
```

To retrieve any file, even if the container is stopped, use Docker's `cp`. Files are stored by default in `/home/smeft19/`, and a copy the data produced for my thesis is in `/home/smeft19/data/`. If you have executed the Notebook `demo.ipynb`, you can get the generated plot with the command

```bash
docker cp 068d5ecc684e:/home/smeft19/demo.pdf demo.pdf
```
