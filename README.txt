Instructions and guidance on files
The repository contains two main folders: Extraction Process and Analysis Process


A. Extraction Process
https://github.com/maiihn/SDS379R_Spring2020/tree/master/Extraction_process
Environment: Terminal
Server: fri.oden.utexas.edu using ssh

1. Pt-system: https://github.com/maiihn/SDS379R_Spring2020/tree/master/Extraction_process/pt-system

a) Test 1: Three saddle search condition

- Three folders: contain materials for calculation in EON (not included in Github due to heavy memory)
https://github.com/maiihn/SDS379R_Spring2020/tree/master/Extraction_process/pt-system/akmc-pt-ransearch
https://github.com/maiihn/SDS379R_Spring2020/tree/master/Extraction_process/pt-system/akmc-pt-onlykdb
https://github.com/maiihn/SDS379R_Spring2020/tree/master/Extraction_process/pt-system/akmc-pt-kdbransearch

- export.py module : contain functions to export
https://github.com/maiihn/SDS379R_Spring2020/tree/master/Extraction_process/pt-system/export.py

- script:
  * fc_export.py : export force calls information for each saddle for each state and sum force call for each state
  https://github.com/maiihn/SDS379R_Spring2020/tree/master/Extraction_process/pt-system/fc_export.py
  
- OUTPUT folder : contain output

b) Test 2: Six different configuration

  i) all_monomers
  https://github.com/maiihn/SDS379R_Spring2020/tree/master/Extraction_process/pt-system/newtest/all_monomers
  ii) one_dimer
  https://github.com/maiihn/SDS379R_Spring2020/tree/master/Extraction_process/pt-system/newtest/one_dimer
  iii) one_trimer
  https://github.com/maiihn/SDS379R_Spring2020/tree/master/Extraction_process/pt-system/newtest/one_trimer
  iv) one_tetramer
  https://github.com/maiihn/SDS379R_Spring2020/tree/master/Extraction_process/pt-system/newtest/one_tetramer
  v) one_pentamer
  https://github.com/maiihn/SDS379R_Spring2020/tree/master/Extraction_process/pt-system/newtest/one_pentamer
  vi) one_hexamer
  https://github.com/maiihn/SDS379R_Spring2020/tree/master/Extraction_process/pt-system/newtest/one_hexamer
  
  Six folders each contain:
  - 10 states from 0 to 9 (not included due to heavy memory)
  - export.py module : contain functions to export
  - saddle_info.py : export saddle information
  - state_info.py : export force call and number of saddles information about state
  - OUTPUT folder : contain output
  
  
  
2. Al-system: https://github.com/maiihn/SDS379R_Spring2020/tree/master/Extraction_process/al-system

Test: 2 different binding sites for Al adatom

a) Hollow-site
https://github.com/maiihn/SDS379R_Spring2020/tree/master/Extraction_process/al-system/onestate/hollow_site
b) Bridge-site
https://github.com/maiihn/SDS379R_Spring2020/tree/master/Extraction_process/al-system/onestate/bridge_site

Two folders each contain:
- 10 states from 0 to 9 (not included due to heavy memory)
- export.py module : contain functions to export
- saddle_info.py : export saddle information
- state_info.py : export force call and number of saddles information about state
- OUTPUT folder : contain output




B. Analysis Process
https://github.com/maiihn/SDS379R_Spring2020/tree/master/Analysis_process
Environment: Jupyter Notebook
Server: Local

1. Pt-system: https://github.com/maiihn/SDS379R_Spring2020/tree/master/Analysis_process/Pt-system

a) Test 1: Three saddle search condition

- Three folders: each contain force call information output in Extraction process
https://github.com/maiihn/SDS379R_Spring2020/tree/master/Analysis_process/Pt-system/akmc-pt-ransearch
https://github.com/maiihn/SDS379R_Spring2020/tree/master/Analysis_process/Pt-system/akmc-pt-onlykdb
https://github.com/maiihn/SDS379R_Spring2020/tree/master/Analysis_process/Pt-system/akmc-pt-kdbransearch

- script:
  * Force_call.ipynb : compute and plot sum force calls and average force call per saddle
  https://github.com/maiihn/SDS379R_Spring2020/tree/master/Analysis_process/Pt-system/Force_call.ipynb

b) Test 2: Six different configuration

  i) all_monomers
  https://github.com/maiihn/SDS379R_Spring2020/tree/master/Analysis_process/Pt-system/newtest/all_monomers/OUTPUT
  ii) one_dimer
  https://github.com/maiihn/SDS379R_Spring2020/tree/master/Analysis_process/Pt-system/newtest/one_dimer/OUTPUT
  iii) one_trimer
  https://github.com/maiihn/SDS379R_Spring2020/tree/master/Analysis_process/Pt-system/newtest/one_trimer/OUTPUT
  iv) one_tetramer
  https://github.com/maiihn/SDS379R_Spring2020/tree/master/Analysis_process/Pt-system/newtest/one_tetramer/OUTPUT
  v) one_pentamer
  https://github.com/maiihn/SDS379R_Spring2020/tree/master/Analysis_process/Pt-system/newtest/one_pentamer/OUTPUT
  vi) one_hexamer
  https://github.com/maiihn/SDS379R_Spring2020/tree/master/Analysis_process/Pt-system/newtest/one_hexamer/OUTPUT
  
  Six folders each contain:
  - 2 folders: onlykdb and ransearch output in Extraction Process
  - Saddle_fc.ipynb : compute ratio force call between RS and KDB of a saddle versus its barrier
  - State_saddle.py : compute number of saddles found by RS and KDB and average force call per saddle for each state
  
c) Compute ratio force call between RS and KDB of a saddle versus its barrier for all 60 configurations from b)
https://github.com/maiihn/SDS379R_Spring2020/blob/master/Analysis_process/Pt-system/newtest/Saddle_fc.ipynb

  
2. Al-system: https://github.com/maiihn/SDS379R_Spring2020/tree/master/Analysis_process/Al-system

Test: 2 different binding sites for Al adatom

a) Hollow-site
https://github.com/maiihn/SDS379R_Spring2020/tree/master/Analysis_process/Al-system/hollow_site/OUTPUT
b) Bridge-site
https://github.com/maiihn/SDS379R_Spring2020/tree/master/Analysis_process/Al-system/bridge_site/OUTPUT
  
Two folders each contain:
- 2 folders: onlykdb and ransearch output in Extraction Process
- Saddle_fc.ipynb : compute ratio force call between RS and KDB of a saddle versus its barrier
- State_saddle.py : compute number of saddles found by RS and KDB and average force call per saddle for each state

Compute ratio force call between RS and KDB of a saddle versus its barrier for all 20 configurations from a) and b)
https://github.com/maiihn/SDS379R_Spring2020/blob/master/Analysis_process/Al-system/Saddle_fc.ipynb

