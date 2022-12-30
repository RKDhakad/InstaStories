# InstaStories

It is a Instagram Story scraping tool.


## Authors

- [@RKDhakad](https://github.com/RKDhakad/)


## Use

To see hidded mentions on the instagram stories

To save instagram stories

To save heighlights of instagram user



## Installation

```bash
  git clone https://github.com/RKDhakad/InstaStories.git
```
```bash
  cd InstaStories
```
```bash
  pip install -r requirments.txt
```
After successful Installation
```bash
  mitmdump -s main.py   # This command gives you a lot of logs
```
For quit run
```bash
   mitmdump -s main.py -q
```
Now all Done
## Screenshots

![All Done](https://github.com/RKDhakad/InstaStories/blob/main/screenshots/Screenshot01.png)


## Optimizations

After all instalation oper the firfox browser and setup the browser proxy on IP ==> 127.0.0.1 and PORT ==> 8080

After setup proxy on firfox

open instagram and login 

when you see any story on the browser this story will save on you system and can be accesible from the web ui of this tool

## On Windows and Linux

```bash
  python -m http.server
```

## On Termux
On the termux all server all run with the main.py script so there is no need to run again
just go on the http://127.0.0.1:8000
