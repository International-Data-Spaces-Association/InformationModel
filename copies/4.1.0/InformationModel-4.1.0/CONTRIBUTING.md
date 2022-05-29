# How to contribute

This file documents the decisions we made for our processes and quality.

## Changelog

We document changes in the CHANGELOG.md on root level which is formatted and
maintained according to the rules documented on http://keepachangelog.com.

## General source code rules

- strip whitespace at the end of lines
- do not use tabs (use 4 spaces instead)
- end each file with a newline (its easier to concat them then)

## Commits

### Requirements

Good commits serve at least these important purposes:

- To speed up the reviewing process
- To help us write a good release note
- To help the future maintainers and developers to find out why a particular change was made to the code or why a specific feature was added
- generate changelog automatically

### Meta Data

Please create commits with valid meta data only. This means, you have to configure your name and mail address like this:

```
git config --global user.name "$name"
git config --global user.email "$email"
```

### Structure

The format of the commit message should be:

```
<subject>

<body>

<footer>
```

Where
- subject is a short summary of changes
- body includes motivation for the change and contrasts with previous behavior
- footer referencing issues, breaking changes etc.

Here is an example

```
a short (50 chars or less) summary of changes

Body of the commit message, a more detailed explanatory text, if necessary.
Wrap it to about 72 characters or so. In some contexts, the first
line is treated as the subject of an email and the rest of the text
as the body. The blank line separating the summary from the body is
critical (unless you omit the body entirely); tools like rebase
can get confused if you run the two together.

Further paragraphs come after blank lines.

- Bullet points are okay, too
- a hyphen is used for the bullet, preceded by a single space, with blank lines in between
```

### Style

Basic recommendations are:

- Write the subject line of what you have done in the imperative mode, that is as if you were commanding someone.
- Write "fix", "add", "change" instead of "fixed", "added", "changed".
- Don't end the subject line with a period - it's a title and titles don't end with a period.
- Don't add parentheses or other stylish elements to the subject line.
- Always leave the second line blank (the line between the subject line and the body)
- Line break the commit message at about 72 chars (to make the commit message readable without having to scroll horizontally
- Add a newline at the end of every document/file which is part of the repository

A properly formed git commit subject line should always be able to complete the following sentence:

- If applied, this commit will your subject line here

For example:

- If applied, this commit will refactor subsystem X for readability
- If applied, this commit will update getting started documentation
- If applied, this commit will release version 1.0.0

Notice how this doesn't work for the other non-imperative forms:

- If applied, this commit will fixed bug with Y
- If applied, this commit will changing behavior of X
- If applied, this commit will more fixes for broken stuff
- If applied, this commit will sweet new class

    Use of the imperative is important only in the subject line. You can relax this restriction when you're writing the body.

    If it seems difficult to summarize what your commit does, it may be because it includes several logical changes or bug fixes, and are better split up into several commits using `git add -p`.

### Branching Model

The branching model defines the basic workflow for different activities in the repository. These activities include:

- add a new feature
- fix a bug and provide this fix on different versions
- prepare and release a version

Our used branching model is an enhanced version of the model by [Vincent Driessen](http://nvie.com/posts/a-successful-git-branching-model/).
The important variation is the back-merge from the the tagged master onto the develop branch.
This enables the power of the `git describe --always --dirty` command, which outputs an ID for the whole process.

#### Requirements

- we want to use git describe in order to get valid version identifiers on every commit checkout
    - more accurate, we want to use `git describe --always --dirty`
- we want to manage all of our versions with tags, including full versions, release candidates, ...

#### Feature Branches

- Every new feature will be developed in its own feature branch off from develop
- Each feature will follow this naming: feature/featureName (where feature name is some descriptive feature name, 2 words most, camel case)
- Regularly push your work to the same named feature branch on the server
- If you need newest changes from develop merge it into your feature branch using git merge --no-ff
- Avoid cross-merging of other feature branches
- CONVENTION: merge your feature branch into develop by opening a pull request
    - Always merge your feature branch into develop using git merge --no-ff
    - BEWARE: Do not execute git config --global --add merge.ff false! Once you have this parameter as a default, it will provoke merge commits even when updating a branch (pull).

### LTS branches
  - The Long-Term-Support version of the Information Model should be provided on a separate `LTS` branch.  
  - LTS version may only be changed via pull requests, which contain only bugfixes.

#### Bugfix Branches

- Same procedure as with feature branches. The only difference is the naming policy: `bugfix/bugfixName` (where bugfix name is some descriptive name for the fixed problem, 2 words most, camel case)
- It should be checked beforehand, if the bugfix affects both Information Model versions (Normal / LTS).

#### Release Branches

- Release branches follow this naming: release/vX.Y.Z
- Release branches are created from the develop branch
    - git checkout develop; git checkout -b release/vX.Y.Z
- The first fix commit in a release branch CAN be tagged as a release candidate
    - git commit -m "fix important bug for release"; git tag vX.Y.Z-rc1 -s
    - use GPG signed tags
    - the intention of an RC is to state the version as 'almost stable' in the sense that it can be tested as a release artefact there are no further modifications planned, other than small bugfixes required if found during testing. If fixes occur after declaring an RC (e.g. rc1), then a new RC should be published (rc2)
- Once a release branch is stabilized, it will be **FIRST** merged to master and **THEN** tagged with the version tag
    - git checkout master; git pull; git merge --no-ff release/vX.Y.Z; git tag vX.Y.Z -s
- After the release tag is pushed, the TAG (not the master branch) is merged into develop
    - git checkout develop; git merge vX.Y.Z
- Afterwards, set the next pre-version (e.g. you just release version 3.2.0, you tag the develop to 3.2.1-pre)
    - git tag -s vX.Y.Z+1-pre
- Note: After creating tags, you need to upload them, as well as the changed branches
    - git push --tags; git push origin master; git push origin develop
