# Pacemaker29

### 3K04 Group 29
**Group Members**
- [Alden Luscher](https://github.com/alusch7)
- [Andrew Gurges](https://github.com/gurgea1)
- [Dayyan Hashmi](https://github.com/hashmid)
- [Ranuja Pinnaduwage](https://github.com/pinnaduk)

### About
Group 29's pacemaker project repository for our 3K04 Lab.

## Our VVI and AAI Mode Explained
For explanation purposes, we will assume a hear trate of 60 BPM and a refractory period of 300ms. A photo of our AAI workflow is attached at the bottom.

In this case (60 BPM), the entire pacing cycle (including the refractory period) must last 1000ms. Therefore, the time between charging and pacing must be equivalent to the total period time (1000ms) minus the refractory period (300ms) minus the pulse width. So the delay between charging and pacing can be written as (PERIOD - VRP - VPW) as shown below.

Then, we must set the correct pins in order to pace, and pace for one pulse width before entering the refractory period state.

However, since the refractory period is supposed to start at the same time as the beginning of a pace, the refractory period has now been delayed by one pulse width. Therefore, in order to adjust for that, we must define the refractory period as the refractory period duration minus a pulse width as shown in the diagram below.

![Pulse_Diagram](https://user-images.githubusercontent.com/76706672/197328356-484f168b-3d33-44af-b930-602e8a8d6e4d.png)

This is where the first issue arises. The refractory period is triggered by both natural and pacemaker pulses. If we enter the refractory period from a natural pulse, we do not want to subtract the pacemaker's pulse width since we haven't actually lost any time. Therefore, when we return to the charging state we subtract PACE_PW which only holds the value of a pulse width if the refractory period state was entered from the pacemaker pacing state.

However, now we encounter another issue. If a natural pulse arrives when we are in the refractory period, then the entire, TOTAL HEARTBEAT PERIOD of 1000ms must restart, **which means must start a new refractory period**. However, just like how the refractory period was delayed by a pacemaker pulse width when we entered the refractory period, **we are now being delayed by one natural pulse width** as well. Therefore, to make back this time from the delay for both the pacemaker and natural pulse widths, we must treat the next refractory period duration as (REFRACTORY PERIOD - PACEMAKER PULSE WIDTH - NATURAL PULSE WIDTH). 

In the rare case that there is a pacemaker beat or natural beat followed by a natural beat that is within the refractory period followed by another natural beat that is within the previous beat's refractory period (etcetera), we have added a sum, to sum up all the natural pulse widths and subtract them to adjust the refractory period correctly.

In the NEARLY IMPOSSIBLE case where there are so many of these pulses falling within the refractory period all in a row that the value of the refractory period adjusted for all the pulse width delays is somehow negative, there is an overflow condition to make allow the pacemaker to fall back into the charging state. If there is yet another pulse after that, it will be immediately pulled back up into the refractory period state and the cycle will repeat itself. **This condition can be seen in the exit from the refractory period state**.

Accounting for all of these caveats has allowed for near perfect timing intervals even with different natural pulse width durations, only inhibited by the time it takes Simulink to evaluate conditionals and set values at each state.

<img width="1246" alt="Screen Shot 2022-10-22 at 4 06 48 AM" src="https://user-images.githubusercontent.com/76706672/197328365-68e82515-808a-4c18-8b09-c5a0ea80399b.png">
