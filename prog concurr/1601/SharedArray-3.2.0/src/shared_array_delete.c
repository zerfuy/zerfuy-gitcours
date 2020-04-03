/* 
 * This file is part of SharedArray.
 * Copyright (C) 2014-2017 Mathieu Mirmont <mat@parad0x.org>
 * 
 * SharedArray is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 2 of the License, or
 * (at your option) any later version.
 * 
 * SharedArray is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License
 * along with SharedArray.  If not, see <http://www.gnu.org/licenses/>.
 */

#define NPY_NO_DEPRECATED_API	NPY_1_8_API_VERSION
#define PY_ARRAY_UNIQUE_SYMBOL	SHARED_ARRAY_ARRAY_API
#define NO_IMPORT_ARRAY

#include <Python.h>
#include <sys/types.h>
#include <sys/mman.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>
#include "shared_array.h"

/*
 * Delete a numpy array from shared memory
 */
static PyObject *do_delete(const char *name)
{
	struct array_meta *meta;
	int fd;
	struct stat file_info;
	size_t map_size;
	void *map_addr;

	/* Open the file */
	if ((fd = open_file(name, O_RDWR, 0)) < 0)
		return PyErr_SetFromErrnoWithFilename(PyExc_OSError, name);

	/* Find the file size */
	if (fstat(fd, &file_info) < 0) {
		close(fd);
		return PyErr_SetFromErrnoWithFilename(PyExc_OSError, name);
	}

	/* Ignore short files */
	if (file_info.st_size < sizeof (*meta)) {
		close(fd);
		PyErr_SetString(PyExc_IOError, "No SharedArray at this address");
		return NULL;
	}
	map_size = file_info.st_size;

	/* Map the whole file into memory */
	map_addr = mmap(NULL, map_size, PROT_READ, MAP_SHARED, fd, 0);
	close(fd);
	if (map_addr == MAP_FAILED)
		return PyErr_SetFromErrnoWithFilename(PyExc_OSError, name);

	/* Check the meta data */
	meta = (struct array_meta *) (map_addr + (map_size - sizeof (*meta)));
	if (strncmp(meta->magic, SHARED_ARRAY_MAGIC, sizeof (meta->magic))) {
		munmap(map_addr, map_size);
		PyErr_SetString(PyExc_IOError, "No SharedArray at this address");
		return NULL;
	}
	munmap(map_addr, map_size);

	/* Unlink the file */
	if (unlink_file(name) < 0)
		return PyErr_SetFromErrnoWithFilename(PyExc_OSError, name);

	Py_RETURN_NONE;
}

/*
 * Method: SharedArray.delete()
 */
PyObject *shared_array_delete(PyObject *self, PyObject *args)
{
	const char *name;

	/* Parse the arguments */
	if (!PyArg_ParseTuple(args, "s", &name))
		return NULL;

	/* Now do the real thing */
	return do_delete(name);
}
