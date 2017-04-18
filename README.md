# git Release and tag script

A generic flow to release a repository

### Usage

create file `package.json` with at least following content `{"version":"1.2.3"}`

Run from command line `python release.py 1.2.3` (where _1.2.3_ is a desired version and git tag number)

### What it does

- Update "version" number in `package.json` file
- Update version number in `VERSION` file (will create if not exists)
- Tag a commit with version
- Push the commit to git with new tag

:)
