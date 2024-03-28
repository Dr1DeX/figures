# FiguresLib
![workflow](https://github.com/Dr1DeX/figures/actions/workflows/main.yml/badge.svg) 

## What it is? ##
This module reads the user data and calculates the radius of a circle or triangle (there will be other shapes in the future).
##A little guide... ##
Основной модуль запуска имеет следующую структуру:

	params = Commander.parse_command()
    if params:
        print(detector(len(params), params))


First, the input parameters are read, if the parameter exists, then they are passed on to the detector function,
where the logic for defining a figure and calling the corresponding method of the figure class is implemented.


----------



### Using ###
The module can be launched in several ways
1) Installing the package ``pip install pip install -i https://test.pypi.org/simple/ FiguresLib-Dr1DeX==0.0.2``
2) Create file ``test.py``
3) Import module ``Figures.utils.runner import runner``
4) Call function ``runner``

Example:

    def main():
        # other code.
        runner()
    if __name__ == '__main__':
        main()
    

We follow further instructions.


## Developer ##
Dr1DeX