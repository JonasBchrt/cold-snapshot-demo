# Demonstration of cold snapshot GNSS

*Author: Jonas Beuchert*

This script shows how to obtain a GNSS position fix from an 11-millisecond raw GNSS signal snapshot without any prior knowledge about the position of the receiver and only coarse knowledge about the time.

Algorithm adapted from:

> Ignacio Fernández-Hernández and Kai Borre. “Snapshot positioning without initial
information”. In: *GPS Solutions* 20.4 (Mar. 2016), pp. 605–616

There is a [discussion in another repository](https://github.com/JonasBchrt/snapshot-gnss-algorithms/discussions/2) with more details on my cold snapshot GNSS implementation.

## Setup

Clone [snapshot-gnss-algorithms](https://github.com/JonasBchrt/snapshot-gnss-algorithms) to your machine.

Follow the setup instructions for snapshot-gnss-algorithms.

Add the files from this repository to the cloned directory.

Download [some exemplary data](http://agamenon.tsc.uah.es/Asignaturas/it/rd/apuntes/GPSdata-DiscreteComponents-fs38_192-if9_55.bin) to the cloned directory.

Run demo_cold_snapshot.py with Python 3, e.g., open a terminal and execute `python3 demo_cold_snapshot.py` in the cloned directory.
