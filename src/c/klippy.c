#define PY_SSIZE_T_CLEAN
#include <Python.h>

static PyObject * add(PyObject *self, PyObject *args) {
    int a, b;

    if(!PyArg_ParseTuple(args, "ii", &a, &b))
        return NULL;

    return PyLong_FromLong(a + b);
}

static PyMethodDef methods[] = {
    {"add", add, METH_VARARGS, "Add two integers."},
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
