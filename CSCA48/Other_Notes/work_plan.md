|    ID    |   User Story/Sub Task   |    Priority   |   Story Points  |
|:--------:|:------------------------|:-------------:|:---------------:|
|  **1**   | **As Professor Rein, I want the application to be able to converts all other data format (csv or others) files to XML data files I used in my catalogue.** |  1  |  45  |
|          | **1.1** Create account and get auth token for NASA Exoplanet Archive APIs |
|          | **1.2** Export data points from NASA Exoplanet Archive |
|          | **1.3** Export data points from exoplanet.eu |
|          | **1.4** Convert CSV data file to XML format |
|  **2**   | **As Rein, I want the application to be able to converts other measurement units to the units I use in my catalogue.** |  1  |  20  |
|          | **2.1** List all units of measurement used in NASA Exoplanet Archive database (or CSV files) |
|          | **2.2** List all units of measurement used in exoplanet.eu database (or CSV files) |
|          | **2.3** List all units of measurement used in Open Exoplanet Catalogues (OEC) from directory "systems" |
|          | **2.4** List all units of measurement used in OEC from directory "systems_kepler" |
|          | **2.5** Find the units that are not used in OEC from directory "systems" |
|          | **2.6** Find the units that are not used in OEC from directory "systems_kepler" |
|          | **2.7** Convert non-existing units to the units used in OEC |
|  **3**   | **As Rein, when new attributes are available in other catalogues but not in mine, I want the application to automatically add such attributes to existing XML files during the merge phrase without causing any error.** |  1  |  20  |
|          | **3.1** Find list of attributes that not present in OEC |
|          | **3.2** Add new attributes into OEC |
|          | **3.3** Insert value into new attributes |
|          | ~~3.4 Update existing entries in OEC with values for the new attribute if applicable~~ |
|          | ~~3.5 Merge entries not found in OEC into OEC~~ |
|          | **3.6** Build python class frameworks for System/Planet/Star/Binary |
|          | ~~3.7 Convert "System" section from XML data to python "System" class objects~~ |
|          | ~~3.8 Convert "Planet" section from XML data to python "Planet" class objects~~ |
|          | ~~3.9 Convert "Star" section from XML data to python "Star" class objects~~ |
|          | ~~3.10 Convert "Binary" section from XML data to python "Binary" class objects~~ |
|          | **3.11** Convert python class objects to XML data format |
|  **4**   | **As Rein, when I accept new data from other catalogues, I want the application (terminal) to provide me with a simple (command prompt) Yes/No or Y/N instruction to approve or decline each change.** |  2  |  75  |
|          | **4.1** Implement Unittest for parsing celestial objects.
|          | **4.2** Implement Unittest for downloading csv data and parsing csv to raw xml data.
|          | **4.3** Parse "System" section from XML data to python "System" class objects.
|          | **4.4** Parse "Star" section from XML data to python "Star" class objects.
|          | **4.5** Parse "Planet" section from XML data to python "Planet" class objects.
|          | **4.6** Parse "Binary" section from XML data to python "Binary" class objects.
|          | **4.7** Search and parse both raw XML and existing XML in OEC "systems" directory into class objects.
|          | **4.8** Generate updated XML from OEC class objects, write new XML files to OEC "systems" directory.
|          | **4.9** Compare attributes in System objects, find differences and update new data to OEC System object.
|          | **4.10** Compare attributes in each Star objects within the system, find differences and update new data to each OEC Star object.
|          | **4.11** Compare attributes in each Planet objects within the system/star, find differences and update new data to each OEC Planet object.
|          | ~~**4.12** Compare attributes in each Binary objects within the system/star, find differences and update new data to each OEC Binary object. (ON HOLD)~~
|          | **4.13** Implement a function to prompt the user to enter Y/N instruction to accept/decline each change within the objects.
|          | ~~**4.14** Implement Push updated XMLs to git repository.~~
|          | **4.15** Refactor Python System/Star/Planet/Binary Classes.
|  **5**   | **As Rein, I want the software to be able to recognize all alternate names of a given planet/star/system across databases before merging the values under those names.** |  2  |  120  |
|          | ~~**5.1** Search NASA XML file with any additional \<name\> value of "system" class under "OEC" object.~~
|          | ~~**5.2** Search NASA XML file with any additional \<name\> value of "star" class under "OEC" object.~~
|          | ~~**5.3** Search NASA XML file with any additional \<name\> value of "planet" class under "OEC" object.~~
|  **6**   | **As Rein, I want to be warned if my input value for planet's data has a bigger different than the average value calculated from other databases/catalogues by a preset value/percentage.** |  3  |  30  |
|          | ~~**6.1** Check if difference between two values is greater than preset value/percentage.~~
|          | ~~**6.2** Display a warning message in terminal when difference is greater than tolerance.~~
|  **7**   | **As Rein, when I update my catalogue by running the script/application and providing/typing the name of a planet/star/system to it, I want to see a list of changes (on terminal) and the source catalogue name between my catalogue and other catalogues.** |  4  |  25  |
|          | ~~**7.1** Display the difference between tags/values of search result and tags/values of search input, in terminal.~~
|          | ~~**7.2** Display the source catalog name in terminal.~~