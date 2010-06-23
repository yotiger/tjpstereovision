#include <python2.6/Python.h>
#include "sgbm.cpp"

/* call from Python:
 * sgbm_run(String img1, String img2);
 */

static PyObject *
sgbm_run(PyObject *self, PyObject *args) {

    printf("Inside C function\n");

    /* parse python arguments */
    char *img1;
    char *img2;
    PyArg_ParseTuple(args, "ss", &img1, &img2);
    
    /* call the function */
    Mat result;
    result = do_sgbm(img1, img2);

    /* return result to python */
    return Py_BuildValue("O", result);
}

PyMODINIT_FUNC
initsgbm(void) {
    static PyMethodDef SgbmMethods[] = {
        {"Run", sgbm_run, METH_VARARGS, "Execute SGBM"}
    };

    (void) Py_InitModule("sgbm",SgbmMethods);
}











