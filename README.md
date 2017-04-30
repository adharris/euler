![Project Euler](https://projecteuler.net/profile/adharris.png)

This is a repository of my [Project Euler](https://projecteuler.net) solutions.

This is a [Click](http://click.pocoo.org/) program, with a command for each
problem. Installing the package provides an `euler` command which is used to 
run each problem.

Wherever possible, I try to solve these problems in a way more generic than
the specific language. In these cases, each command supports additional
options. These options should always default to whatever the original problem
specifies.

Additionally, the `euler generate N` command generates a python file in the 
appropriate directory, with the Click command pre-built and the problem 
language as the function docstring.

I reset my progress on April 21st 2017. Old solutions up to problem 110ish are
on the legacy branch.