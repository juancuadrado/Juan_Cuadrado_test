# Juan_Cuadrado_test<br />
Dev Test<br />


**Question A**<br />
Your goal for this question is to write a program that accepts two lines (x1,x2) and (x3,x4) on the x-axis and returns whether they overlap. As an example, (1,5) and (2,6) overlaps but not (1,5) and (6,8).<br />
 
**Question B**<br />
The goal of this question is to write a software library that accepts 2 version string as input and returns whether one is greater than, equal, or less than the other.<br /> As an example: “1.2” is greater than “1.1". Please provide all test cases you could think of.<br />
 
**Question C**<br />
Your goal is to write a new library that can be integrated to the stack. Dealing with network<br /> issues everyday, latency is our biggest problem. Thus, your challenge is to write a new Geo Distributed LRU (Least Recently Used) cache with time expiration. This<br /> library will be used extensively by many of our services so it needs to meet the following criteria:
<br /> 
    1 - Simplicity. Integration needs to be dead simple.<br />
    2 - Resilient to network failures or crashes.<br />
    3 - Near real time replication of data across Geolocation. Writes need to be in real time.<br />
    4 - Data consistency across regions<br />
    5 - Locality of reference, data should almost always be available from the closest region<br />
    6 - Flexible Schema<br />
    7 - Cache can expire <br />
