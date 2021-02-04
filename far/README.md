# Federal Acquisition Regulation API
This project will attempt to convert the FAR into separate JSON objects, each ontaining html text for each section. This way, the FAR can be stored in a database and pulled whenever required, and only updated in one location.

The FAR still needs to exist online in html in order for us to do some google searches on its contents, but maybe this API will allow the FAR parts/subparts/sectiosns to be stored in a more centralized location. This FAR API can pull the html text into wherever the FAR is required.

Before jumping into too many ideas, problems will be explained below that will detail the rationale behind revamping the current system.

### Problem 1: Inconsistent html structure
The html structure of the FAR is not consistent among each regulation. Here is a table of how each regulation indents their lists:

|REGULATION|STYLE|
|---|---|
|FAR|`<span class="ph autonumber">`|
|DFARS|`<p class= "p List1">`<br>`<p class="p List2">`<br>...|
|DFARS PGI|`<p class="p List1">`<br>`<p class="p List2">`<br>...|
|AFFARS|`<p align="left" style="margin-left: 0.3in"...>`|
|DARS|`<p style="margin-left: 0.57in">`<br>`<p style="margin-left: 0.89in">`<br>...|
|DLAD|`<p style="margin-left: 0.25in;">`<br>`<p style="margin-left: 0.50in;">`<br>...|
|NMCARS|`<p class="p List1">`<br>`<p class="p List2">`<br>...|"
|SOFARS|Uses a combination of `<li>` and `<p>`|
|TRANSFARS|Just uses `<p>`, no indentations|
|AGAR|Just uses `<p>`, no indentations|
|AIDAR|Just uses `<p>`, no indentations|
|CAR|Just uses `<p>`, no indentations|
|DEAR|Just uses `<p>`, headings use `<li>`|
|DIAR|`<p class="p List1">`<br>`<p class="p List2">`<br>...|
|DOLAR|Just uses `<p>`, no indentations|
|DOSAR|Just uses `<p>`, no indentations|
|DTAR|Just uses `<p>`, no indentations|
|EDAR|Just uses `<p>`, no indentations|
|EPAAR|`<p class="p List1">`<br>`<p class="p List2">`<br>...|
|FEHBAR|Just uses `<p>`, no indentations|
|GSAM/R|`<span class="ph autonumber">`|
|HHSAR|Just uses `<p>`, no indentations|
|HSAR|`<p class="p List1">`<br>`<p class="p List2">`<br>...|
|HUDAR|`<p class="p List1">`<br>`<p class="p List2">`<br>...|
|IAAR|Just uses `<p>`, no indentations|
|JAR|Just uses `<p>`, no indentations|
|LIFAR|Just uses `<p>`, no indentations|
|NFS|Just uses `<p>`, no indentations|
|NRCAR|Just uses `<p>`, no indentations|
|TAR|Just uses `<p>`, no indentations|
|VAAR|`<p class="indenta">`<br>`<p class="indenti">`<br>`<p class="indent1">`<br>...|

As you can see, the vast majority of the regulations don't even have indents. Those that do never have their text line up with the indent itself and end up trail well past the indentation, which defeats the purpose of showing a list.

If all the regulation had the same formatting and structure, perusing their contents will easier and more efficient. The current version of the FAR isn't unreadable, but it could use some improvements.

### Problem 2: Hyperlinks with arbitrary names
Scoring through the html code, you can find numerous examples of hyperlink ID's that make no sense at all. Take HHSAR part 317: the contents of this has almost not a single id that makes logical sense. For example, what exactly is `P8_300` supposed to mean in a section that direcetly preceeds `P18_1718`?

Each section should have a hyperlink of course, but how about a more generalized format such as the actual reference of the text in the regulation? `P8_300` is the hyperlink ID for HHSAR 317.105-1. What if it was called `0317_105_1` so that we can parse this ID and easily get the part, section, and subsection? Having links like this in a more standardized format will allow setting up the webpage so much easier and more convenient. A solid foundation eases future edits.

### Problem 3: Separate html files for each and every subsection
I believe that each subsection for every regulation deserves to be it's own object in some sort of database to be pulled or edited at will. However, each of these subsections absolutely does not need to be their own html file.

Individuals in the acquisition field are not trained to read just the specific verbiage of text that relates to their requirement: they are taught to 'zoom-out' to the prescription of said text, then to 'zoom-out' even further to see if it still applies. This 'zooming-out' is crucial to ensuring any and all text applies to the issues at hand, and having one html file per subsection is inefficient.

The good news is, much of the regulations are already strcutured this way. This problem isn't too big among the supplements, but when it gets to the DFARS, all the text pertaining to the 






