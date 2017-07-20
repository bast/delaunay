import os
from .cffi_helpers import get_lib_handle


_this_path = os.path.dirname(os.path.realpath(__file__))

_build_dir = os.getenv('DELAUNAY_BUILD_DIR')
if _build_dir is None:
    _build_dir = _this_path
else:
    _build_dir = os.path.join(_build_dir, 'lib')

_include_dir = os.path.join(_this_path)

_lib = get_lib_handle(
    ['-DDELAUNAY_API=', '-DCPP_INTERFACE_NOINCLUDE'],
    'delaunay.h',
    'delaunay',
    _build_dir,
    _include_dir
)


def solve(points):
    res = _lib.delaunay2d_from(points, len(points))
    tres = _lib.tri_delaunay2d_from(res)
    _lib.delaunay2d_release(res)

    triangles = []
    for i in range(tres.num_triangles):
        triangles.append([tres.tris[i*3 + 0], tres.tris[i*3 + 1], tres.tris[i*3 + 2]])

    _lib.tri_delaunay2d_release(tres)

    return triangles
