<br/>
<p align="center">
  <a href="https://github.com/SpotlightForBugs/g-dork">
    <img src="https://www.linkpicture.com/q/Google-2Bdork.png" alt="Logo" width"50%" height="50%">
  </a>

  <h3 align="center">another Google Dorker</h3>

  <p align="center">
    An OSINT script, running on Python
    <br/>
    <br/>
    <a href="https://github.com/SpotlightForBugs/g-dork/issues">Report Bug</a>
    .
    <a href="https://github.com/SpotlightForBugs/g-dork/issues">Request Feature</a>
  </p>
</p>

![Contributors](https://img.shields.io/github/contributors/SpotlightForBugs/g-dork?color=dark-green) ![Issues](https://img.shields.io/github/issues/SpotlightForBugs/g-dork) ![License](https://img.shields.io/github/license/SpotlightForBugs/g-dork) 

## Table Of Contents

* [About the Project](#about-the-project)
* [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Usage](#usage)
* [Roadmap](#roadmap)
* [Contributing](#contributing)
* [License](#license)
* [Authors](#authors)
<!--* [Acknowledgements](#acknowledgements)-->

## About The Project

![Web capture_11-6-2022_225030_](https://user-images.githubusercontent.com/73603712/173204471-4596734e-4502-4ff3-bb67-afd81fbde943.jpeg)

There are many great Google Dork scripts available on GitHub, however, I didn't find one that really suit my needs so I created this enhanced one. I want to create a Google Dork script so amazing that it'll be the last one you ever need.

Here's why:

* Your time should be focused on finding information.
 
* You shouldn't be doing the same tasks over and over like creating a googling 100 searches per hand


This script is not finished yet and I am actively working on it.
 You may also suggest changes by forking this repo and creating a pull request or opening an issue.

A list of commonly used resources that I find helpful are listed in the acknowledgements.

## Built With

This script is made with Python and would not be possible without the amazing module 'googlesearch'

## Getting Started

To get a local copy up and running follow these simple example steps.

### Prerequisites

You'll need Python3 and python3-pip

### Installation



1. Clone the repo

```sh
git clone https://github.com/SpotlightForBugs/g-dork.git && cd g-dork
```

2. Install requirements
```sh
pip install -r requirements.txt
```


## Usage
```
usage: g-dork.py [-h] -q TARGET [-html | -j | -t] [-qty QTY] [-d DELAY]

options:
  -h, --help            show this help message and exit
  -q TARGET, -query TARGET
                        what you want to find
  -html, -webversion    outputs the result as HTML5
  -j, -json             outputs the result as JSON
  -t, -txt              outputs the result as a text
  -qty QTY, -quantity QTY how many results shoud be processed, defaults to 10 results                                           
  -d DELAY, -delay DELAY  how long to wait between searches in seconds, defaults to 1
                       
                       
```


## Roadmap

See the [open issues](https://github.com/SpotlightForBugs/g-dork/issues) for a list of proposed features (and known issues).

## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.
* If you have suggestions for adding or removing projects, feel free to [open an issue](https://github.com/SpotlightForBugs/g-dork/issues/new) to discuss it, or directly create a pull request after you edit the affected file with necessary changes.
* Please make sure you check your spelling and grammar.
* Create individual PR for each suggestion.
* Please also read through the [Code Of Conduct](https://github.com/SpotlightForBugs/g-dork/blob/main/CODE_OF_CONDUCT.md) before posting your first idea as well.

### Creating A Pull Request

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See [LICENSE](https://github.com/SpotlightForBugs/g-dork/blob/main/LICENSE.md) for more information.

## Authors

* **Johannes Häusler aka. SpotlightForBugs** - *Student @pius-gymnasium.de* - [Johannes Häusler aka. SpotlightForBugs](https://github.com/SpotlightForBugs) - *Made this repository*

<!--## Acknowledgements-->


