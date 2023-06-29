from setuptools import setup

setup(
    name="klippy",
    version="0.0.1",
    description="Klipper host service",
    long_description="Klipper host service for mcu management",
    setup_requires=["cffi>=1.0.0"],
    packages=["klippy", "klippy.kinematics",
              "klippy.extras", "klippy.extras.display"],
    package_dir={"klippy": "src"},
    package_data={"klippy.extras": ["*.cfg"],
                  "klippy": ["chelper/*.c", "chelper/*.h"],
                  "klippy.extras.display": ["*.cfg"]},
    cffi_modules=["src/chelper_builder.py:ffibuilder"],
    install_requires=["cffi>=1.0.0"]
)
