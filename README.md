# Demonstration of cold snapshot GNSS

*Author: Jonas Beuchert*

This script shows how to obtain a GNSS position fix from an 11-millisecond raw GNSS signal snapshot without any prior knowledge about the position of the receiver and only coarse knowledge about the time. The algorithm is adapted from

> Ignacio Fernández-Hernández and Kai Borre. “Snapshot positioning without initial
information”. In: *GPS Solutions* 20.4 (Mar. 2016), pp. 605–616.

There is a [discussion in another repository](https://github.com/JonasBchrt/snapshot-gnss-algorithms/discussions/2) with more details on my cold snapshot GNSS implementation.

## Setup

Clone [snapshot-gnss-algorithms](https://github.com/JonasBchrt/snapshot-gnss-algorithms) to your machine.

Follow the setup instructions for snapshot-gnss-algorithms.

Add the files from this repository to the cloned directory.

Download some exemplary data to the cloned directory. Use the file *GPSdata-DiscreteComponents-fs38_192-if9_55.bin* from the *Extras Archive File* [here](https://extras.springer.com/?query=978-0-8176-4390-4).

Run demo_cold_snapshot.py with Python 3, e.g., open a terminal and execute `python demo_cold_snapshot.py` in the cloned directory.

## Funding statment

SnapperGPS was supported by an EPSRC IAA Technology Fund.

Additionally, Jonas Beuchert is supported by the EPSRC Centre for Doctoral Training in Autonomous Intelligent Machines and Systems.
