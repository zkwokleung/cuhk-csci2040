from distutils.core import setup, Extension
setup(name='myModule', version='1.0',
      # ext_modules=[Extension('myModule', ['fib.c'])])
      # ext_modules=[Extension('myModule', ['helloWorld.c'])])
      ext_modules=[Extension('myModule', ['selectSort.c'])])
