project('klippy', 'c', version: '0.0.1')

py_mod = import('python')
py = py_mod.find_installation()

includes = include_directories(['src'])
sources_c = files('src/klippy.c')
sources_py = files('src/__init__.py')

py.install_sources(
    sources_py,
    subdir: 'klippy',
    pure: false
)

py.extension_module(
    '_klippy',
    sources_c,
    install: true,
    subdir: 'klippy',
    include_directories: includes
)
