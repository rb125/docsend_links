# docsend_links

Docsend doesn't provide a public API to create links in bulk. So here's a simple python script that does it for you.<br/>
[![Screenshot-from-2023-05-01-22-34-21.png](https://i.postimg.cc/rFMgk117/Screenshot-from-2023-05-01-22-34-21.png)](https://youtu.be/U-NFJByuMKU)

### Dependencies
progress==1.6 <br/>
selenium==4.9.0<br/>
webdriver_manager==3.8.5

### How to use it?
Run the python program bulk_links.py and provide a csv file with the list of accounts through the -f parameter:<br/>
<b>python bulk_links.py -f sample_input.csv</b>

The program creates a new file <b>docsend_list_<timestamp>.csv</b> in the same directory with the list of accounts and corresponding docsend links. 
