# Propulsion-Test-Data
CSV records of test data from the UVR propulsion division.

# Important! Formatting rules for uploaded data:
Create a folder named `YYYY-MM-DD_DESCRIPTION` where `DESCRIPTION` is very brief context for the test. Eg. `2024-11-17_MULE-1-COLDFLOW`
Within this folder, all data files must adhere to the following format so that it can be parsed easily by a script without having to modify code for each dataset.
- Filename for each test: `data0.csv`, `data1.csv` etc. where `data0.csv` was recorded before `data1.csv`.
- Comma seperated values
- The first line is units of the header line.
- The second line is a header of at least the columns of data within the file.
- Remaining lines are data which all *must* contain a `timestamp` entry in `YYYY-MM-DD HH:MM:SS.mmmmmm`. This can be obtained from `timestamp = str(datetime.datetime.now())` using the `datetime` module in python. These lines *must* also contain a `seconds` entry which is time in seconds counting up from 0 where the zero time is the first line.
### Example:
```
,psi,psi,psi,psi,psi,kg,N,C,C,C,C,,s
,P_INJECTOR,P_COMB_CHMBR,P_N2O_FLOW,P_N2_FLOW,P_RUN_TANK,L_RUN_TANK,L_THRUST,T_RUN_TANK,T_INJECTOR,T_COMB_CHMBR,T_POST_COMB,timestamp,seconds
174998,-0.09042528765881297,-14.7,518.1840747978135,-9629589.133284336,0.37792664197329273,-0.1128813292363132,4708.63782820118,6.574598643056447,10.023778504105621,-273.15,-273.15,2024-11-17 11:38:17.281538,0.0
174999,0.16659977286448768,-14.7,516.6705690594731,-9831213.754677927,-0.00896759596597363,-0.09218324387887797,4708.63782820118,7.989862214856487,10.967892296897617,-273.15,-273.15,2024-11-17 11:38:17.283722,0.002184
```
An additional `report.md` should be included that gives context for the test. Include relevant data (location of the test, if it was particularly cold that day, if additional hardware was being tested, any interesting anomalies encountered etc).
### Example:
See [2024-11-17_MULE_1_N2O_COLDFLOW](https://github.com/UVicRocketry/Propulsion-Test-Data/tree/main/2024-11-17_MULE_1_N2O_COLDFLOW) for an example of how data should be structured.

