#include <cstdlib>
#include <ctime>
#include <stdio.h>

#include "delaunay.h"

int main()
{
    using namespace std;

    const int NUM_POINTS = 1000;

    del_point2d_t *points = new del_point2d_t[NUM_POINTS];

    //  printf("%i\n", NUM_POINTS);
    for (int i = 0; i < NUM_POINTS; i++)
    {
        points[i].x =
            static_cast<double>(rand()) / static_cast<double>(RAND_MAX);
        points[i].y =
            static_cast<double>(rand()) / static_cast<double>(RAND_MAX);
        //      printf("%f %f\n", points[i].x, points[i].y);
    }

    clock_t begin = clock();

    delaunay2d_t *res = delaunay2d_from(points, NUM_POINTS);
    tri_delaunay2d_t *tdel = tri_delaunay2d_from(res);

    clock_t end = clock();
    double elapsed_secs = double(end - begin) / CLOCKS_PER_SEC;
    printf("num points: %i elapsed secs: %f\n", NUM_POINTS, elapsed_secs);

    //  printf("%i\n", tdel->num_triangles);
    //  for (int i = 0; i < tdel->num_triangles; i++)
    //  {
    //      printf("%i %i %i\n", tdel->tris[i*3 + 0],
    //                           tdel->tris[i*3 + 1],
    //                           tdel->tris[i*3 + 2]);
    //  }

    tri_delaunay2d_release(tdel);
    delaunay2d_release(res);

    delete[] points;

    return 0;
}
