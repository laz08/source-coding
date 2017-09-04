# Source code: Shannon, Shannon fano and Huffman

## About

This little project is product of a class assignment, coded around March 2016.

It was used to study:

* Obtention of a __source of information__ from a text, where source of information
consists in a list of pairs, where each pair contains one letter and its frequency of appearance in the given text.
* Computation of the __entropy__ of a source of information.
* Creation of __extensions__ from said source.
* Implementation of __Shannon__ coding.
* Implementation of __Shannon fano__ coding.
* Implementation of __Huffman__ coding.


## Structure
It is composed by five files:

* __Shannon.py__, which implements Shannon coding.
* __Shannon_fano.py__, which implements Shannon fano coding.
* __Huffman.py__, which implements Huffman coding.
* __Utils.py__, which is the core and has all the important methods that lead to each implementation.
* __main.py__, which allows a direct route to use the methods defined in __Utils.py__
from the terminal.


## How it works
You can read about what this project implements in the following wikipedia entries:

* [Information theory](https://en.wikipedia.org/wiki/Information_theory).
* [Shannon](https://en.wikipedia.org/wiki/Shannon_coding).
* [Shannon Fano](https://en.wikipedia.org/wiki/Shannon%E2%80%93Fano_coding).
* [Huffman](https://en.wikipedia.org/wiki/Huffman_coding).

For each coding (Shannon, Shannon fano and Huffman), the mean length is provided too.

## Usage
You can test quickly each coding executing __main.py__ and providing it with a source file.

## LICENSE
```
Copyright 2017 Laura C.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

  http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```
