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

#ifndef __SHARED_ARRAY_H__
#define __SHARED_ARRAY_H__

#define NPY_NO_DEPRECATED_API	NPY_1_8_API_VERSION
#define PY_ARRAY_UNIQUE_SYMBOL	SHARED_ARRAY_ARRAY_API
#define NO_IMPORT_ARRAY

#include <Python.h>
#include <structseq.h>
#include <numpy/arrayobject.h>

/* Magic header */
#define SHARED_ARRAY_MAGIC	"[SharedArray]"

/* Array metadata */
struct array_meta {
	char	magic[16];
	size_t	size;
	int	typenum;
	int	itemsize;
	int	ndims;
	npy_intp dims[NPY_MAXDIMS];
} __attribute__ ((packed));

/* ArrayDesc object */
extern PyStructSequence_Desc PyArrayDescObject_Desc;
extern PyTypeObject PyArrayDescObject_Type;

/* Main functions */
extern PyObject *shared_array_create(PyObject *self, PyObject *args, PyObject *kwds);
extern PyObject *shared_array_attach(PyObject *self, PyObject *args);
extern PyObject *shared_array_delete(PyObject *self, PyObject *args);

/* SHM list function */
#ifdef __linux__
extern PyObject *shared_array_list(PyObject *self, PyObject *args);
#endif

/* Support functions */
extern int open_file(const char *name, int flags, mode_t mode);
extern int unlink_file(const char *name);

#endif /* !__SHARED_ARRAY_H__ */
