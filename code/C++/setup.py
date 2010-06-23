from distutils.core import setup, Extension

module1 = Extension('sgbm', sources = ['sgbmmodule.cpp'])

setup (name = 'SGBM',
       version = '1.0',
       description = 'SG block matching link to c++',
       ext_modules = [module1])
