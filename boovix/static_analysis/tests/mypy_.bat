@rem python C:\Python34\Scripts\mypy main.py
@rem >> main.py, line 6: No module named 'wx'
@rem Not yet possible to use non-standard libraries with mypy, see issues:
@rem "Ignore specific lines" 
@rem https://github.com/JukkaL/mypy/issues/500
@rem "Include Python's sys.path into build.default_lib_path?"
@rem https://github.com/JukkaL/mypy/issues/486

echo ON
set PATH=C:\Windows\system32;C:\Windows;C:\Windows\System32\Wbem;C:\Python34;C:\Python34\Scripts;
python C:\Python34\Scripts\mypy test.py
python C:\Python34\Scripts\mypy test2.py
pause
