# Pacemaker29

### 3K04 Group 29
**Group Members**
- [Alden Luscher](https://github.com/alusch7)
- [Andrew Gurges](https://github.com/gurgea1)
- [Dayyan Hashmi](https://github.com/hashmid)
- [Ranuja Pinnaduwage](https://github.com/pinnaduk)

### About
Group 29's pacemaker project repository for our 3K04 Lab. In this project, we interface with an artifical heart and a pacemaker of our own design, and via Simulink, demonstrate the VOO, AOO, VVI, and AAI modes of a real pacemaker. We also have created a DCM which allows us to interface with the pacemaker via a GUI, and change funcitonal parameters.

## Our VVI and AAI Refractory Period Explained
For explanation purposes, we will assume a hear trate of 60 BPM and a refractory period of 300ms. A photo of our AAI workflow is attached at the bottom.

In this case (60 BPM), the entire pacing cycle (including the refractory period) must last 1000ms. Therefore, the time between charging and pacing must be equivalent to the total period time (1000ms) minus the refractory period (300ms) minus the pulse width. So the delay between charging and pacing can be written as (PERIOD - VRP - VPW) as shown below.

Then, we must set the correct pins in order to pace, and pace for one pulse width before entering the refractory period state.

However, since the refractory period is supposed to start at the same time as the beginning of a pace, the refractory period has now been delayed by one pulse width. Therefore, in order to adjust for that, we must define the refractory period as the refractory period duration minus a pulse width as shown in the diagram below.

![Pulse_Diagram](https://user-images.githubusercontent.com/76706672/197328356-484f168b-3d33-44af-b930-602e8a8d6e4d.png)
