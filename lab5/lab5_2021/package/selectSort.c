#include <Python.h>

void swap(int *a, int *b)
{
    int tmp = *a;
    *a = *b;
    *b = tmp;
}

void CselectSort(long arr[], int n)
{
    for (int i = 0; i < n - 1; ++i)
    {
        int min_idx = i;

        // minPos = position of the smallest element in the array A;
        for (int j = i + 1; j < n; ++j)
            if (arr[j] < arr[min_idx])
                min_idx = j;

        // Swap A[i] with A[minPos];
        swap(&arr[min_idx], &arr[i]);
    }
}

static PyObject *selectSort(PyObject *self, PyObject *args)
{
    long arr[20000] = {0}, n = 0;
    PyObject *pObj;

    // Parse arguments
    if (!PyArg_ParseTuple(args, "O", &pObj))
    {
        return NULL;
    }

    // Get Iterator from PyObject to retrieve the list
    PyObject *iter = PyObject_GetIter(pObj);
    if (!iter)
    {
        return NULL;
    }

    // Iter through the list to build a C array
    while (1)
    {
        PyObject *next = PyIter_Next(iter);
        if (!next)
        {
            break;
        }

        arr[n++] = PyLong_AsLong(next);
    }

    // Perform Selection Sort
    CselectSort(arr, n);

    // Convert the C array into Python List
    PyObject *lst = PyList_New(n);
    if (!lst)
        return NULL;

    for (int i = 0; i < n; i++)
    {
        PyObject *num = PyLong_FromLong(arr[i]);
        PyList_SET_ITEM(lst, i, num);
    }

    return lst;
}

// Our Module's Function Definition struct
// We require this `NULL` to signal the end of our method
// definition
static PyMethodDef myMethods[] = {{"selectSort", selectSort, METH_VARARGS, "Sort an array with selection sort"},
                                  {NULL, NULL, 0, NULL}};

// Our Module Definition struct
static struct PyModuleDef myModule = {PyModuleDef_HEAD_INIT, "myModule", "CSCI2040 Lab5", -1, myMethods};

// Initializes our module using our above struct
PyMODINIT_FUNC PyInit_myModule(void)
{
    return PyModule_Create(&myModule);
}
