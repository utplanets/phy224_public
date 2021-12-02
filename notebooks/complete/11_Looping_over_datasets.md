## Use a `for` loop to process files given a list of their names.
* A filename is just a character string.
* And lists can contain character strings.



```python
import numpy
for filename in ["data/galileo_flat.csv","data/galileo_ramp.csv"]:
    distance, height = numpy.loadtxt(filename, skiprows=2,\
                                     comments="#", delimiter=',', unpack=True)
    print(filename, distance.min(), height.max())
```

    data/galileo_flat.csv 800.0 1000.0
    data/galileo_ramp.csv 253.0 1000.0


## Use `glob.glob` to find sets of files whose names match a pattern.
*   In Unix, the term "globbing" means "matching a set of files with a pattern".
*   The most common patterns are:
    *   `*` meaning "match zero or more characters"
    *   `?` meaning "match exactly one character"
*   Python contains the `glob` library to provide pattern matching functionality
*   The `glob` library contains a function also called `glob` to match file patterns
*   E.g., `glob.glob('*.txt')` matches all files in the current directory 
    whose names end with `.txt`.
*   Result is a (possibly empty) list of character strings.



```python
import glob
print("all csv files in data/random directory:", glob.glob("data/random/*.csv"))
```

    all csv files in data/random directory: ['data/random/data.029.csv', 'data/random/data.015.csv', 'data/random/data.001.csv', 'data/random/data.000.csv', 'data/random/data.014.csv', 'data/random/data.028.csv', 'data/random/data.002.csv', 'data/random/data.016.csv', 'data/random/data.017.csv', 'data/random/data.003.csv', 'data/random/data.007.csv', 'data/random/data.013.csv', 'data/random/data.012.csv', 'data/random/data.006.csv', 'data/random/data.010.csv', 'data/random/data.004.csv', 'data/random/data.038.csv', 'data/random/data.039.csv', 'data/random/data.005.csv', 'data/random/data.011.csv', 'data/random/data.076.csv', 'data/random/data.062.csv', 'data/random/data.089.csv', 'data/random/data.088.csv', 'data/random/data.063.csv', 'data/random/data.077.csv', 'data/random/data.049.csv', 'data/random/data.061.csv', 'data/random/data.075.csv', 'data/random/data.074.csv', 'data/random/data.060.csv', 'data/random/data.048.csv', 'data/random/data.064.csv', 'data/random/data.070.csv', 'data/random/data.058.csv', 'data/random/data.059.csv', 'data/random/data.071.csv', 'data/random/data.065.csv', 'data/random/data.073.csv', 'data/random/data.067.csv', 'data/random/data.098.csv', 'data/random/data.099.csv', 'data/random/data.066.csv', 'data/random/data.072.csv', 'data/random/data.057.csv', 'data/random/data.043.csv', 'data/random/data.094.csv', 'data/random/data.080.csv', 'data/random/data.081.csv', 'data/random/data.095.csv', 'data/random/data.042.csv', 'data/random/data.056.csv', 'data/random/data.068.csv', 'data/random/data.040.csv', 'data/random/data.054.csv', 'data/random/data.083.csv', 'data/random/data.097.csv', 'data/random/data.096.csv', 'data/random/data.082.csv', 'data/random/data.055.csv', 'data/random/data.041.csv', 'data/random/data.069.csv', 'data/random/data.045.csv', 'data/random/data.051.csv', 'data/random/data.079.csv', 'data/random/data.086.csv', 'data/random/data.092.csv', 'data/random/data.093.csv', 'data/random/data.087.csv', 'data/random/data.078.csv', 'data/random/data.050.csv', 'data/random/data.044.csv', 'data/random/data.052.csv', 'data/random/data.046.csv', 'data/random/data.091.csv', 'data/random/data.085.csv', 'data/random/data.084.csv', 'data/random/data.090.csv', 'data/random/data.047.csv', 'data/random/data.053.csv', 'data/random/data.008.csv', 'data/random/data.034.csv', 'data/random/data.020.csv', 'data/random/data.021.csv', 'data/random/data.035.csv', 'data/random/data.009.csv', 'data/random/data.023.csv', 'data/random/data.037.csv', 'data/random/data.036.csv', 'data/random/data.022.csv', 'data/random/data.026.csv', 'data/random/data.032.csv', 'data/random/data.033.csv', 'data/random/data.027.csv', 'data/random/data.031.csv', 'data/random/data.025.csv', 'data/random/data.019.csv', 'data/random/data.018.csv', 'data/random/data.024.csv', 'data/random/data.030.csv']



```python
print("all txt files in data/random directory:", glob.glob("data/random/*.txt"))
```

    all txt files in data/random directory: []


## Use `glob` and `for` to process batches of files.
Helps a lot if the files are named and stored systematically and consistently so that simple patterns will find the right data.



```python
for filename in sorted(glob.glob('data/random/*.csv')):
    distance, height = numpy.loadtxt(filename, delimiter=',', unpack=True)
    print(filename, distance.mean(), height.std())
```

    data/random/data.000.csv 0.973455156 14.253108991004671
    data/random/data.001.csv -4.4384872 18.271604877007015
    data/random/data.002.csv -2.28566216 13.972753882460598
    data/random/data.003.csv -2.319335146 18.62861642517896
    data/random/data.004.csv 1.294413436 13.466904099021583
    data/random/data.005.csv -7.44047908 17.786138908909383
    data/random/data.006.csv -1.7816439620000002 18.817227525496232
    data/random/data.007.csv 4.6912883679999995 9.999054105208188
    data/random/data.008.csv -5.049618464 12.44592807947692
    data/random/data.009.csv -0.07109980799999999 17.83813061879353
    data/random/data.010.csv -8.717094524 20.849448541334226
    data/random/data.011.csv 0.053728404000000014 15.147772954205065
    data/random/data.012.csv -5.2156092 14.613099372696924
    data/random/data.013.csv -0.4909348 10.341980518209885
    data/random/data.014.csv 4.199319794 20.770533770383075
    data/random/data.015.csv -1.129316226 14.837675085738278
    data/random/data.016.csv 1.354752152 22.054233344383633
    data/random/data.017.csv -1.29629856 11.626441944587546
    data/random/data.018.csv -0.9475405182 20.233241837932603
    data/random/data.019.csv 0.6780552519999999 18.925705463682363
    data/random/data.020.csv 0.7654873360000001 13.489747407074168
    data/random/data.021.csv -0.001415861999999981 12.842900268316898
    data/random/data.022.csv -0.986253904 17.33037256376791
    data/random/data.023.csv 1.9309210620000001 9.087868023797867
    data/random/data.024.csv 5.483798139999999 15.458282480621016
    data/random/data.025.csv 1.415097562 9.235305537734275
    data/random/data.026.csv -3.35545337 15.232575577127255
    data/random/data.027.csv 5.36550574 11.8069795018849
    data/random/data.028.csv -8.191419953999999 16.503100963466885
    data/random/data.029.csv 2.49977854 15.47135921844907
    data/random/data.030.csv -1.2605272800000002 19.407473030973495
    data/random/data.031.csv -3.89636704 13.375499579354376
    data/random/data.032.csv 3.9812517599999997 19.651015005278758
    data/random/data.033.csv -5.78141256 18.532560769148397
    data/random/data.034.csv 1.38721754 15.93083223862817
    data/random/data.035.csv -3.40586724 15.28188961909269
    data/random/data.036.csv -4.02127652 11.664555327894277
    data/random/data.037.csv -5.86433188 16.14986316035672
    data/random/data.038.csv 1.2782799339999997 13.16648886951738
    data/random/data.039.csv -1.9918538799999999 19.577179065651684
    data/random/data.040.csv -0.9968814502 10.855899821539852
    data/random/data.041.csv 3.01251976 12.637877284988102
    data/random/data.042.csv 4.687270033999999 19.47352038013039
    data/random/data.043.csv 0.9401650579999999 18.264197058881198
    data/random/data.044.csv -5.6282113 15.961945665352657
    data/random/data.045.csv 4.295377220000001 13.530733112739293
    data/random/data.046.csv -3.2600629952 8.23421308853168
    data/random/data.047.csv -2.352025586 16.837443737827737
    data/random/data.048.csv -2.8432164882 12.367238364488546
    data/random/data.049.csv 2.5512576339999997 17.97961620391327
    data/random/data.050.csv 5.093506420000001 14.444537005058573
    data/random/data.051.csv -2.9846522305999996 21.406940859619752
    data/random/data.052.csv 1.9411847580000003 11.582002513744955
    data/random/data.053.csv -2.2120761594 18.91900010019242
    data/random/data.054.csv 6.511417462 12.915201922692296
    data/random/data.055.csv 6.301410980000001 15.048591717047419
    data/random/data.056.csv -5.09980774 18.701643207663597
    data/random/data.057.csv -0.6002595339999999 12.821220593759838
    data/random/data.058.csv 0.5823109 20.102536723527308
    data/random/data.059.csv -2.67354184 19.165192424218905
    data/random/data.060.csv 0.9920916359999999 9.423935739320731
    data/random/data.061.csv -3.8687329399999997 11.784302780395333
    data/random/data.062.csv 3.32145168 18.31816423598968
    data/random/data.063.csv -6.110594798000001 17.1653758318072
    data/random/data.064.csv -0.17609123999999995 10.658921705919411
    data/random/data.065.csv -5.22974142 10.96992350701607
    data/random/data.066.csv 3.1699939739999996 17.462587038145518
    data/random/data.067.csv -6.0860773 11.098078057417958
    data/random/data.068.csv -1.8609751156 17.962315241928643
    data/random/data.069.csv -6.29706456 13.124196489840418
    data/random/data.070.csv 4.2104994200000005 14.586825378207198
    data/random/data.071.csv -5.095741326 15.52351050000898
    data/random/data.072.csv 0.4404297926000001 13.21052946918686
    data/random/data.073.csv -5.03440886 14.672281230490235
    data/random/data.074.csv 4.30564458354 23.11505075996672
    data/random/data.075.csv 3.475419498 12.638129702757267
    data/random/data.076.csv -3.74129344 20.224019178872684
    data/random/data.077.csv -2.007808742 21.09642061632448
    data/random/data.078.csv 3.2629136940000008 8.86749437731909
    data/random/data.079.csv 2.964532682 15.938706452613655
    data/random/data.080.csv 3.2134671200000002 13.16432594114806
    data/random/data.081.csv -10.014815399999998 10.445101623119847
    data/random/data.082.csv -1.407920774 18.3542939041089
    data/random/data.083.csv 0.7053996178000002 10.0336599797134
    data/random/data.084.csv 1.4845570400000003 16.532368391548957
    data/random/data.085.csv -3.5595325160000004 13.699337435539135
    data/random/data.086.csv -1.1525967979999998 13.419724725084011
    data/random/data.087.csv -2.92201214 14.102074823859367
    data/random/data.088.csv -6.783227920000001 18.537439476607606
    data/random/data.089.csv 8.573129819999998 17.261241864736185
    data/random/data.090.csv -2.4358456799999995 13.342839933396927
    data/random/data.091.csv -0.272942136 14.908377707490997
    data/random/data.092.csv 0.97381578 15.441761974288225
    data/random/data.093.csv -8.362317458 14.714349874112642
    data/random/data.094.csv -1.82146777 16.869214663698486
    data/random/data.095.csv 0.5970510440000001 15.703879203447388
    data/random/data.096.csv 0.724618214 16.429186710317516
    data/random/data.097.csv 0.48894924 15.292681284065516
    data/random/data.098.csv 1.84267224 11.33741881916356
    data/random/data.099.csv -3.772237556 14.155571992376832


## keypoints:
* Use a `for` loop to process files given a list of their names.
* Use `glob.glob` to find sets of files whose names match a pattern.
* Use `glob` and `for` to process batches of files.
