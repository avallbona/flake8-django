Change Log
==========

0.0.5 (2019-04-24)
------------------

**Improvements**

- Added `DJ09` - Model must define `class Meta`
- Added `DJ10` - Class Meta from Model has to define `verbose_name`
- Added `DJ11` - Class Meta from Model has to define `verbose_name_plural`
- Fixed some flake8 issues in package and tests and added pypi badge
- Refactored some tests
- Bumped version number

0.0.4 (2019-01-18)
------------------

**Improvements**

- Added `DJ06` check for ModelForm, should not use exclude (@rocioar)
- Added `DJ07` check for `ModelForm.META`, should not set fields to `'__all__'` (@rocioar)
- Added `DJ08` check for Model, should contain `__str__` method (@rodolfolottin)

0.0.3 (2018-10-03)
------------------

**Bugfixes**

- Fixed bug in setup.py missing some modules (@lithammer)

0.0.2 (2018-10-02)
------------------

**Bugfixes**

- Fixed bug in `ModelFieldChecker` where node is not one of Name or Attribute (@rocioar)

**Improvements**

- Added checks `DJ04` and `DJ05` for urls (@rocioar)
- Reorganized code, moved individual checkers to `checkers/`, `tests to tests/` (@rocioar)
- Added coverage checks (@rocioar)
- Moved from Travis to CircleCI (@rocioar)


0.0.1 (2018-09-28)
------------------

Initial version
