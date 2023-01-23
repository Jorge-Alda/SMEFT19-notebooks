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

### Dev container

If you are using `VSCode` with the Remote Development, you should be prompted to re-open the folder in a dev container. After the container is built, you will be in an enviroment where all the dependencies are already installed.

If you don't use VSCode but have Docker installed, go to the cloned directory and run the command

```bash
docker build -t smeft19nb .
```

Don't forget the final dot! Once the container finishes to build, open it with the command

```bash
docker run -it -v $(pwd):/app smeft19nb
```

That will open a `bash` shell inside the container. If you want to run `python`, you can also use
```bash
docker run -it -v $(pwd):/app smeft19nb python
```

To start the Jupyter server, you will need also to expose the ports of the container. Use the command

```bash
docker run -it -p 8888:8888 -v $(pwd):/app smeft19nb bash run_nb.sh
```

If you want to install a `python` package, run `poetry add package_name` inside the shell, and don't forget to build the container again the next time. To install an OS package, add it to the file `apt.txt` and rebuild the container.

### Run on-line [Not updated yet!!]

The simplest way to run the notebooks is by visiting [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/Jorge-Alda/SMEFT19-notebooks/HEAD)

Click on `demo.ipynb` to see a simple example, or navigate the folders to run the code [Be careful! Binder might impose CPU limits for long computations].

You can save any generated files with the menu File > Download. All files will be lost after shutting down Binder.
