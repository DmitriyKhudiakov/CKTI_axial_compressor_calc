<h1 align="center">  CKTI axial compressor calc </h1>
<h3 align="center"> Designing an axial compressor using the CKTI method </h3>


<p align="center"> 
  <img src="source/ckti.gif" alt="Animated gif"  width="900px">
</p>

## Overview

<p align="justify"> 
  The CKTI method is based on the use of experimental characteristics of model steps and results
the influence of steps on each other and the influence of deviations from geometric similarity on the characteristics of the steps.

This method is suitable for the calculation of air compressor blades with a capacity of up to 300 kg/s.
with a pressure ratio of up to 4.5 and a circumferential speed of more than 280 m/s.

The calculation of the blade apparatus of an axial compressor of a stationary type consists of several stages. At the first stage, variant calculations of the blade apparatus are carried out in order to select the optimal variant for subsequent calculations. Variant calculations are performed using the experimental characteristics of the model stages and include an approximate calculation of pressure losses in the suction and discharge pipes of the compressor, the outer diameter of the blade apparatus, the length of the blades of the first and last stages, and the trim value of the last blades.

The calculation of the optimal variant consists of the first and second stepwise calculations of the blade apparatus, taking into account
corrections to the calculated values ​​of the efficiency and pressure coefficient due to deviation from
geometric and dynamic similarity, determination of the efficiency of the blade apparatus, the power spent on gas compression, static pressures and temperatures on the average radius in front of and behind the impellers.
</p>

## Installation
Clone this repo
```bash
git clone https://github.com/DmitriyKhudiakov/CKTI_axial_compressor_calc.git
```
Install libs
```bash
pip install -r requirements.txt
```

## Usage
Run visualization
```bash
main.py
```


## License
[MIT](https://choosealicense.com/licenses/mit/)
