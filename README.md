# Filmcrawler

```
Scrapy FilmCrawler Project Readme
```

```
Create Environment run scrapy
```
* Using virtualenv.
* Install virtualenv: **$pip install virtualenv**
* Create environment: **$virtualenv env_linux** (*with env_linux is name virtualenv created in Linux machine*)

```
Activate virtualenv
```
* Activate virtualenv on Linux/Mac OS: **$source env_linux/bin/activate**
* Activate virtualenv on Windows     : **>. env_linux\Script\activate**
* Result after activate: **(env_linux)$**

```
Install Scrapy
```
* Install scrapy on virtualenv: **(env_linux)$pip install -r requirement.txt**


```
Run Scrapy
```
* Run scrapy: **$scrapy crawl film -a config_file=sources/config/<name_config_file> -o output/<name_output_file>**
* Example: **$scrapy crawl film -a config_file=sources/config/phim3s_config.json -o output/phim3s_output.json**

```
Deactivate virtualenv
```
* Deactivate virtualenv: **$deactivate**

```
Convert from output json to csv if you want check
```
* Deactivate virtualenv: **$python tools/convert_json_to_csv.py -i output/<name_output_file_json> -o output/<name_output_file_csv>**

```
Set speed crawl data on code
```
* Set download delay on settings scrapy:
* On file:  filmcrawler/scrapy/crawler/settings.py
* Set: **DOWNLOAD_DELAY = n** (with n is seconds). If comment line code, Download delay is 0.25s as default of scrapy framework.