#!/bin/bash

# Run toy experiment and generate data (sample_experiment.csv)
python3 experiment.py

# Plot all, using the generated data
python3 plot_all.py -in_file=sample_experiment -out_folder=plots
