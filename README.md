# distanceproject

This program takes a set of packages with associated notes, weights, times, and delivery locations, compares them to a list of addresses, and finds the fastest and shortest
way to delivery these packages within a specific time table. 

The packages are first parsed, loaded onto a truck. That truck then delivers the packages before going back to the hub. Repeat until packages are delivered.

The only requirement were that all packages had to be delivered by their required time. They also had to be delivered in less than 140 total miles driven.
