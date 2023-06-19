#define PY_SSIZE_T_CLEAN
#include <Python.h>

#include "pyhelper.h"

static PyObject * klippy_get_monotonic(PyObject *self, PyObject *args) {
    return PyLong_FromLong(get_monotonic());
}

static PyObject * klippy_dummy(PyObject *self, PyObject *args) {
    return PyLong_FromLong(0);
}

static PyMethodDef methods[] = {
    {"get_monotonic", klippy_get_monotonic, METH_NOARGS, "get_monotonic"},
    {"new_char_array", klippy_dummy, METH_NOARGS, "new_char_array"},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef module = {
    PyModuleDef_HEAD_INIT,
    "klippy",
    NULL,
    -1,
    methods
};

PyMODINIT_FUNC PyInit__klippy(void) {
    return PyModule_Create(&module);
}
