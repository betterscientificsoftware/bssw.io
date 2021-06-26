# Utilities supporting the bssw.io site

## wikize_refs.py

The tool `wikize_refs.py` helps to manage [Github Favored Markdown
references/citations](https://betterscientificsoftware.github.io/bssw.io/bssw_styling_common.html#citationsreferences)
in `*.md` files that are used on the bssw.io site.  This is typically run in
place as:

```
$ ./wikize_refs.py -i <base>.md
```

but can also be run to produce an output document `<base>-gen.md` and not disturbing the input file `<base>.md` while debugging the citations/references using:

```
$ ./wikize_refs.py -o <base>-gen.md  <base>.md
```

Run `./wikize_refs.py --help` or see
[here](https:../Articles/Blog/ReferencesInMarkdownHybridApproach.md) for more
details.

## Testing the bssw.io utilities

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

One can also run the tests locally and submit to CDash with:

```
./run_tests.sh --submit-to-cdash
```

(or just `-s` for short).

By default, tests that check links and require network communication are
disabled but they can be enabled by running:

```
./run_tests.sh --enable-link-check-tests
```

(or just `l` for short).

For more details, see:

```
./run_tests.sh -h
```
