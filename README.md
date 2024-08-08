# Interview problem solutions

The repository contains the solutions for the interview problems. 
Each problem has its dedicated module inside the `problems` folder. 
The tests for each module are located in a corresponding test module
within the same folder. The test module for each problem is named after
the problem's module, prefixed with `test_`. Tests can be run using the pytest tool.

---

The repository is powered by [Pants](https://www.pantsbuild.org/). 
You can also easily run the tests by first [installing Pants](https://www.pantsbuild.org/2.21/docs/getting-started/installing-pants)
and then running:

```shell
pants test problems/::
```

If you would like to contribute to the project, you can format your code
and lint it using [black](https://black.readthedocs.io/en/stable/) and 
[flake8](https://flake8.pycqa.org/en/latest/) 
to ensure your code is consistent with the existing codebase. To do that
first run:

```shell
pants fmt problems/::
```

to format the code using `black` and then lint it with `flake8` by running:

```shell
pants lint problems/::
```

The MyPy static type checker is also enabled, and you can run it with the following command:

```shell
pants check problems/::
```