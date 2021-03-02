# Utilities supporting the bssw.io site

## wikize_refs.py

The tool `wikize_refs.py` help to manage Github Favored Markdown
references/citations in `*.md` files that are used on the bssw.io site.

Run `./wikize_refs.py --help` for details.

## Testing the bssw.io utilties

The tests for these utilities is managed and run as a simple CMake/CTest
project.  Setting up and running these tests is a simple as:

```
$ mdkir <test_build_dir>
$ cd <test_build_dir>/
$ cmake ..
$ ctest
```

This can also be done in one shot by running:

```
./run_tests.sh
```
