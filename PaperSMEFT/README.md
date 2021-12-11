# Fit to SMEFT coefficients I

This series of notebooks contain all the code to reproduce the data in Section 6.2 of my PhD thesis, which is adapted from [2012.14799](https://arxiv.org/abs/2012.14799):

* [01](01_Fits.ipynb): Best fit points for each Scenario for Table 6.2
* [02](02_LikelihoodPlots.ipynb): Plots for Scenarios IV, V, VI and XI for Figure 6.1
* [03](03_RKRD.ipynb): Calculation of the central values and uncertainties for the $R_{K^{(*)}}$ and $R_{D^{(*)}}$ ratios for Table 6.3 and Figure 6.2.
* [04](04_ScenarioVII.ipynb): Hessian matrix and ellipse points for Scenario VII. Eqs (6.18) and (6.22), and Table 6.4. Pulls from all observables for Figure 6.3 and Appendix C.1. Largest pull differences for Table 6.5. Figure 6.4.

## Additional files

* Hessian ellipse data for:
   * [Scenario I](https://github.com/Jorge-Alda/SMEFT19-notebooks/raw/master/data/ellipses/scI.yaml)
   * [Scenario II](https://github.com/Jorge-Alda/SMEFT19-notebooks/raw/master/data/ellipses/scII.yaml)
   * [Scenario III](https://github.com/Jorge-Alda/SMEFT19-notebooks/raw/master/data/ellipses/scIII.yaml)
   * [Scenario IV](https://github.com/Jorge-Alda/SMEFT19-notebooks/raw/master/data/ellipses/scIV.yaml)
   * [Scenario V](https://github.com/Jorge-Alda/SMEFT19-notebooks/raw/master/data/ellipses/scV.yaml)
   * [Scenario VI](https://github.com/Jorge-Alda/SMEFT19-notebooks/raw/master/data/ellipses/scVI.yaml)
   * [Scenario VII](https://github.com/Jorge-Alda/SMEFT19-notebooks/raw/master/data/ellipses/scVII.yaml)
   * [Scenario VIII](https://github.com/Jorge-Alda/SMEFT19-notebooks/raw/master/data/ellipses/scVIII.yaml)
   * [Scenario IX](https://github.com/Jorge-Alda/SMEFT19-notebooks/raw/master/data/ellipses/scIX.yaml)
   * [Scenario X](https://github.com/Jorge-Alda/SMEFT19-notebooks/raw/master/data/ellipses/scX.yaml)
   * [Scenario XI](https://github.com/Jorge-Alda/SMEFT19-notebooks/raw/master/data/ellipses/scXI.yaml)
* Likelihood plots for:
   * Scenario IV: [(pdf)](https://raw.githubusercontent.com/Jorge-Alda/SMEFT19-notebooks/master/data/plots/scIVbeta.pdf) | [(pgf)](https://raw.githubusercontent.com/Jorge-Alda/SMEFT19-notebooks/master/data/plots/scIVbeta.pgf)
   * Scenario V: [(pdf)](https://raw.githubusercontent.com/Jorge-Alda/SMEFT19-notebooks/master/data/plots/scV.pdf) | [(pgf)](https://raw.githubusercontent.com/Jorge-Alda/SMEFT19-notebooks/master/data/plots/scV.pgf)
   * Scenario VI: [(pdf)](https://raw.githubusercontent.com/Jorge-Alda/SMEFT19-notebooks/master/data/plots/scVIbeta.pdf) | [(pgf)](https://raw.githubusercontent.com/Jorge-Alda/SMEFT19-notebooks/master/data/plots/scVIbeta.pgf)
   * Scenario XI: [(pdf)](https://raw.githubusercontent.com/Jorge-Alda/SMEFT19-notebooks/master/data/plots/scXIbeta.pdf) | [(pgf)](https://raw.githubusercontent.com/Jorge-Alda/SMEFT19-notebooks/master/data/plots/scXIbeta.pgf)
* $R_{K^{(*)}}$ and $R_{D^{(*)}}$ observables:
    * [Scenario IV](https://raw.githubusercontent.com/Jorge-Alda/SMEFT19-notebooks/master/data/observables/obsIV.yaml)
    * [Scenario VII](https://raw.githubusercontent.com/Jorge-Alda/SMEFT19-notebooks/master/data/observables/obsVII.yaml)
    * [Scenario IX](https://raw.githubusercontent.com/Jorge-Alda/SMEFT19-notebooks/master/data/observables/obsIX.yaml)
    * [Scenario X](https://raw.githubusercontent.com/Jorge-Alda/SMEFT19-notebooks/master/data/observables/obsX.yaml)
    * [Scenario XI](https://raw.githubusercontent.com/Jorge-Alda/SMEFT19-notebooks/master/data/observables/obsXI.yaml)
* Confidence plots for observables:
    * $R_{K^{(*)}}$: [(pdf)](https://raw.githubusercontent.com/Jorge-Alda/SMEFT19-notebooks/master/data/plots/RKplot.pdf) | [(pgf)](https://raw.githubusercontent.com/Jorge-Alda/SMEFT19-notebooks/master/data/plots/RKplot.pgf)
    * $R_{D^{(*)}}$: [(pdf)](https://raw.githubusercontent.com/Jorge-Alda/SMEFT19-notebooks/master/data/plots/RDplot.pdf) | [(pgf)](https://raw.githubusercontent.com/Jorge-Alda/SMEFT19-notebooks/master/data/plots/RDplot.pgf)
* Plot of the pulls for every observable in Scenario VII [(pdf)](https://raw.githubusercontent.com/Jorge-Alda/SMEFT19-notebooks/master/data/plots/pullsVII.pdf) | [(pgf)](https://raw.githubusercontent.com/Jorge-Alda/SMEFT19-notebooks/master/data/plots/pullsVII.pgf)
* List of the pulls for every observable in Scenario VII: [(pdf)](https://raw.githubusercontent.com/Jorge-Alda/SMEFT19-notebooks/master/data/TeX/standalone_pullsVII.pdf) | [(tex)](https://raw.githubusercontent.com/Jorge-Alda/SMEFT19-notebooks/master/data/TeX/pullsVII.tex)
* Evolution of some observables along the axes of the ellipsoid:
    * Axis 1: [(pdf)](https://raw.githubusercontent.com/Jorge-Alda/SMEFT19-notebooks/master/data/plots/evo_ax1.pdf) | [(pgf)](https://raw.githubusercontent.com/Jorge-Alda/SMEFT19-notebooks/master/data/plots/evo_ax1.pgf)
    * Axis 2: [(pdf)](https://raw.githubusercontent.com/Jorge-Alda/SMEFT19-notebooks/master/data/plots/evo_ax2.pdf) | [(pgf)](https://raw.githubusercontent.com/Jorge-Alda/SMEFT19-notebooks/master/data/plots/evo_ax2.pgf)
    * Axis 3: [(pdf)](https://raw.githubusercontent.com/Jorge-Alda/SMEFT19-notebooks/master/data/plots/evo_ax3.pdf) | [(pgf)](https://raw.githubusercontent.com/Jorge-Alda/SMEFT19-notebooks/master/data/plots/evo_ax3.pgf)
    * SM-best fit point direction: [(pdf)](https://raw.githubusercontent.com/Jorge-Alda/SMEFT19-notebooks/master/data/plots/evo_sm.pdf) | [(pgf)](https://raw.githubusercontent.com/Jorge-Alda/SMEFT19-notebooks/master/data/plots/evo_sm.pgf)
