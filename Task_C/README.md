
This task requires a search about the topic. In the quest to understand the problem entirely, it was found a library on PyPI, which was the problem partially covered. This library wholly covered four items on the issue.  The other three were partially covered. So the primary approach was to improve the existing library.
Topics to improve:<br />
5 - Locality of reference, data should almost always be available from the closest region<br />
    [partially covered, an additional iteration is needed in order to indicate on which region/instance/etc the data will be obtained]<br />
6 - Flexible Schema<br />
    [is a flexible schema, keys are stored in strings and values, but the data could be parsed from a specific structure or model]<br />
7 - Cache can expire<br />
    [partially covered, the expiration functionality is rusty and needs to be more flexible and robust]<br />
    
There wasn't a relevant improve in the code.
