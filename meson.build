project('klippy', 'c', version: '0.0.1')

py_mod = import('python')
py = py_mod.find_installation()

includes = include_directories(['src/c'])
sources_c = files('src/c/klippy.c')

sources_py = files(
    'src/__init__.py',
    'src/clocksync.py',
    'src/configfile.py',
    'src/console.py',
    'src/gcode.py',
    'src/mathutil.py',
    'src/mcu.py',
    'src/msgproto.py',
    'src/parsedump.py',
    'src/pins.py',
    'src/queuelogger.py',
    'src/reactor.py',
    'src/serialhdl.py',
    'src/stepper.py',
    'src/toolhead.py',
    'src/util.py',
    'src/webhooks.py',
)

py.install_sources(sources_py, subdir: 'klippy', pure: false)

py.extension_module(
    '_klippy',
    sources_c,
    install: true,
    subdir: 'klippy',
    include_directories: includes,
)
