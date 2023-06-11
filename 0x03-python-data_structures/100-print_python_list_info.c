#include "Python.h"
#include <stdio.h>

/**
 *print_python_list_info - prints information about
 *Python lists
 *@p: is the pointer to the list object
 *Return: nothing
 */

void print_python_list_info(PyObject *p)
{
	int i;
	PyListObject *ll;

	ll = (PyListObject *)p;
	printf("[*] Size of the Python List = %ld\n", ll->ob_base.ob_size);
	printf("[*] Allocated = %ld\n", ll->allocated);
	for (i = 0; i < ll->ob_base.ob_size; i++)
	{
		printf("Element %d: %s\n", i, ll->ob_item[i]->ob_type->tp_name);
	}
}
