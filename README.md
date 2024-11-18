# Propulsion-Test-Data
CSV records of test data from the UVR propulsion division.

# Important! Formatting rules for uploaded data:
Create a folder named `YYYY-MM-DD_DESCRIPTION` where `DESCRIPTION` is very brief context for the test. Eg. `2024-11-17_MULE-1-COLDFLOW`
Within this folder, all data files must adhere to the following format so that it can be parsed easily by a script without having to modify code for each dataset.
- Filename for each test: `data0.csv`, `data1.csv` etc. where `data0.csv` was recorded before `data1.csv`.
- Comma seperated values (CSV) (except the first line)
- The first line is units of the header line.
- The second line is a header of at least the columns of data within the file.
- Remaining lines are data which all *must* contain a timestamp entry in `YYYY-MM-DD HH:MM:SSSSSS`. This can be obtained from `timestamp = str(datetime.datetime.now())` using the `datetime` module in python.
### Example:
```
,psi,psi,psi,psi,psi,kg,N,C,C,C,C,
,P_INJECTOR,P_COMB_CHMBR,P_N2O_FLOW,P_N2_FLOW,P_RUN_TANK,L_RUN_TANK,L_THRUST,T_RUN_TANK,T_INJECTOR,T_COMB_CHMBR,T_POST_COMB,timestamp
9999,1.0661874846960417,-14.7,508.9769148895765,-10944475.88095628,1.216197490841708,0.057479834859498175,4708.63782820118,2.556179119456715,9.00019350994711,-273.15,-273.15,2024-11-17 11:48:57.311401
10000,0.5521373636494404,-14.7,508.88232078093023,-11079036.518839126,1.47412698280122,0.009715022496186526,4708.63782820118,2.7139854061517212,9.00019350994711,-273.15,-273.15,2024-11-17 11:48:57.324701
10001,2.030031461658422,-14.7,509.039977628674,-11019327.939971497,0.7003385069226837,0.08868617893686218,4708.63782820118,1.9247864362628206,8.4486998564239,-273.15,-273.15,2024-11-17 11:48:57.328648
```
An additional `report.md` should be included that gives context for the test. Include relevant data (location of the test, if it was particularly cold that day, if additional hardware was being tested, any interesting anomalies encountered etc).
### Example:
```
Mule-1 cold flow test conducted with N2O at the Malahat Fish and Game range. It was particularly cold that day (6C or so) meaning N2O saturation pressure was lower than desirable. No issues encountered with instrumentation or controls. Two cold flows were conducted back to back with about 10 minutes seperating the tests.
```
