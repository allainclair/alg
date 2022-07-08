## Setup and running project

Python version used: 3.10.4

Using https://pdm.fming.dev/

Or just install requests: `pip install requests`

### Running using pdm

* First: `pdm update`

* `pdm run requests 94306` returns the count for the zipcode 94306
  * To get this count, only use the zipcode

* `pdm run requests Potliquor 94114` returns business info for the "Potliquor 94114"
  * Always put the zipcode at the end

### Running using python (with requests dependency)

* Insatead of `pdm run requests` use  `python requests_.py`

## Future work

* Add unit tests!!
* Refactor `requests_.py`
* Separate the app into modules: split `requests_.py` in other files
* Analyse, follow up and update `design.md`
