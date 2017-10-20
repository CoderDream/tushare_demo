# tushare_demo
tushare使用手册





## 环境安装 ##

###安装lxml###

	C:\Users\Admin>pip install wheel
	Collecting wheel
	  Downloading wheel-0.30.0-py2.py3-none-any.whl (49kB)
	    100% |████████████████████████████████| 51kB 114kB/s
	Installing collected packages: wheel
	Successfully installed wheel-0.30.0
	
	C:\Users\Admin>pip install lxml
	Collecting lxml
	  Downloading lxml-4.1.0-cp27-cp27m-win_amd64.whl (3.6MB)
	    100% |████████████████████████████████| 3.6MB 67kB/s
	Installing collected packages: lxml
	Successfully installed lxml-4.1.0

###安装pandas###

	C:\Users\Admin>pip install pandas
	Collecting pandas
	  Downloading pandas-0.20.3-cp27-cp27m-win_amd64.whl (8.3MB)
	    100% |████████████████████████████████| 8.3MB 39kB/s
	Requirement already satisfied: pytz>=2011k in d:\python27\lib\site-packages (from pandas)
	Collecting python-dateutil (from pandas)
	  Downloading python_dateutil-2.6.1-py2.py3-none-any.whl (194kB)
	    100% |████████████████████████████████| 194kB 52kB/s
	Collecting numpy>=1.7.0 (from pandas)
	  Downloading numpy-1.13.3-cp27-none-win_amd64.whl (13.0MB)
	    100% |████████████████████████████████| 13.0MB 35kB/s
	Collecting six>=1.5 (from python-dateutil->pandas)
	  Downloading six-1.11.0-py2.py3-none-any.whl
	Installing collected packages: six, python-dateutil, numpy, pandas
	Successfully installed numpy-1.13.3 pandas-0.20.3 python-dateutil-2.6.1 six-1.11.0
	
	C:\Users\Admin>pip install pandas
	Requirement already satisfied: pandas in d:\python27\lib\site-packages
	Requirement already satisfied: pytz>=2011k in d:\python27\lib\site-packages (from pandas)
	Requirement already satisfied: python-dateutil in d:\python27\lib\site-packages (from pandas)
	Requirement already satisfied: numpy>=1.7.0 in d:\python27\lib\site-packages (from pandas)
	Requirement already satisfied: six>=1.5 in d:\python27\lib\site-packages (from python-dateutil->pandas)

### 安装 requests ###

	C:\Users\Admin>pip install requests
	Collecting requests
	  Downloading requests-2.18.4-py2.py3-none-any.whl (88kB)
	    100% |████████████████████████████████| 92kB 47kB/s
	Collecting urllib3<1.23,>=1.21.1 (from requests)
	  Downloading urllib3-1.22-py2.py3-none-any.whl (132kB)
	    100% |████████████████████████████████| 133kB 123kB/s
	Collecting idna<2.7,>=2.5 (from requests)
	  Downloading idna-2.6-py2.py3-none-any.whl (56kB)
	    100% |████████████████████████████████| 61kB 109kB/s
	Collecting chardet<3.1.0,>=3.0.2 (from requests)
	  Downloading chardet-3.0.4-py2.py3-none-any.whl (133kB)
	    100% |████████████████████████████████| 143kB 71kB/s
	Collecting certifi>=2017.4.17 (from requests)
	  Downloading certifi-2017.7.27.1-py2.py3-none-any.whl (349kB)
	    100% |████████████████████████████████| 358kB 89kB/s
	Installing collected packages: urllib3, idna, chardet, certifi, requests
	Successfully installed certifi-2017.7.27.1 chardet-3.0.4 idna-2.6 requests-2.18.4 urllib3-1.22

### 安装 bs4 ###

	C:\Users\Admin>pip install bs4
	Collecting bs4
	  Downloading bs4-0.0.1.tar.gz
	Collecting beautifulsoup4 (from bs4)
	  Downloading beautifulsoup4-4.6.0-py2-none-any.whl (86kB)
	    100% |████████████████████████████████| 92kB 129kB/s
	Building wheels for collected packages: bs4
	  Running setup.py bdist_wheel for bs4 ... done
	  Stored in directory: C:\Users\Admin\AppData\Local\pip\Cache\wheels\84\67\d4\9e09d9d5adede2ee1c7b7e8775ba3fbb04d07c4f94
	6f0e4f11
	Successfully built bs4
	Installing collected packages: beautifulsoup4, bs4
	Successfully installed beautifulsoup4-4.6.0 bs4-0.0.1


### pip list ###

	C:\Users\Admin>pip list	
	backports.shutil-get-terminal-size (1.0.0)
	beautifulsoup4 (4.6.0)
	bs4 (0.0.1)
	certifi (2017.7.27.1)
	chardet (3.0.4)
	colorama (0.3.9)
	decorator (4.1.2)
	Django (1.11.6)
	enum34 (1.1.6)
	idna (2.6)
	ipython (5.5.0)
	ipython-genutils (0.2.0)
	lxml (4.1.0)
	numpy (1.13.3)
	pandas (0.20.3)
	pathlib2 (2.3.0)
	pickleshare (0.7.4)
	pip (9.0.1)
	prompt-toolkit (1.0.15)
	Pygments (2.2.0)
	python-dateutil (2.6.1)
	pytz (2017.2)
	requests (2.18.4)
	scandir (1.6)
	setuptools (28.8.0)
	simplegeneric (0.8.1)
	six (1.11.0)
	traitlets (4.3.2)
	tushare (0.9.9)
	urllib3 (1.22)
	wcwidth (0.1.7)
	wheel (0.30.0)
	win-unicode-console (0.5)

## 参考文档 ##

1. [Python财经数据接口包TuShare的使用](https://jingyan.baidu.com/article/3065b3b68d7fb5becff8a494.html)
2. [Python 与 炒股TuShare TuShare 安装篇](http://blog.csdn.net/robertsong2004/article/details/50642610)
3. [Python 与 炒股TuShare TuShare 分析篇](http://blog.csdn.net/robertsong2004/article/details/50642677)
4. [Python 与 炒股TuShare 使用篇之一](http://blog.csdn.net/robertsong2004/article/details/50642617)
5. [Python 与 炒股TuShare 使用篇之二](http://blog.csdn.net/robertsong2004/article/details/50642655)
6. [Python 与 炒股TuShare 使用篇之三](http://blog.csdn.net/robertsong2004/article/details/50643198)