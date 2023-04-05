# Randomized-Markov

Code repository for reproducing the simulation studies in the paper

Ramdas, A. and Manole, T. (2023). Randomized and Exchangeable Improvements of Markov’s, Chebyshev’s and Chernoff’s Inequalities. _arXiv preprint._

## Dependencies

This code has only been tested using Python 3.10 on a standard Linux machine. Beyond the Python Standard Library, the only required packages for the main code are `NumPy`, `sklearn`, and [`confseq`](https://github.com/gostevehoward/confseq).

## Usage  
To reproduce the simulation studies in Sections 7.1--7.4 of the paper, run the respective files `intervals.py`, `Ke-vals.py`, `mixture_ui.py`, and `betting.py`. To reproduce the respective plots, run `plot_intervals.py`, `plot_Ke-vals.py`, `plot_ui.py`, and `plot_betting.py`. To reproduce the additional simulations in Appendix C, run the file `e-vals.py`, and to obtain the corresponding plots, run `plot_e-vals.py`. 
