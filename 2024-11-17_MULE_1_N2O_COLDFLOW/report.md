Mule-1 cold flow test conducted with N2O at the Malahat Fish and Game range.

It was particularly cold that day (6C or so) meaning N2O saturation pressure was lower than desirable. No issues encountered with instrumentation or controls. Two cold flows were conducted back to back with about 10 minutes seperating the tests.

Note that only `P_INJECTOR, P_N2O_FLOW, P_RUN_TANK, L_RUN_TANK, T_RUN_TANK, T_INJECTOR` were in use, and `T_INJECTOR` was attached to the normally closed valve (NCV) to monitor it's temperature.

The engine was not assembled during this test with a combustion chamber. The injector assembly was exposed to free air so it could be filmed for spray pattern analysis.

The first test (data0.csv) was accidentally recorded without time stamps for each data point, however the start time was recorded. The second test (data1.csv) included time stamps. To recover an approximation of the data, a script was written to calculate the average sample rate of the second test (458Hz) and compute time stamps based on the start time for each line in the data0.csv file. This is not perfect as the std deviation of sample rate is quite large (~100Hz) but it this is likely not an issue.
