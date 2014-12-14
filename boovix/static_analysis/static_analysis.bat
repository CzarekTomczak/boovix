cd %~dp0..\

@rem ------------------------- autopep8 ---------------------------------------
@rem To remove trailing whitespace. VS2013 does not have such option.

autopep8 --in-place --recursive .

@rem --------------------------------------------------------------------------

@rem -------------------------- pylint ----------------------------------------
@rem pylint [options] module_or_package

pylint --reports=n --rcfile="%~dp0\.pylintrc" main
@if %ERRORLEVEL% neq 0 goto EOF

pylint --reports=n --rcfile="%~dp0\.pylintrc" utils
@if %ERRORLEVEL% neq 0 goto EOF
@rem --------------------------------------------------------------------------


@rem ---------------------------- pep8 ----------------------------------------
@rem --first option shows only first warning for a file
@rem pep --first main.py

pep8 --exclude=static_analysis/tests/ ./
@if %ERRORLEVEL% neq 0 goto EOF

@rem --------------------------------------------------------------------------


:EOF
