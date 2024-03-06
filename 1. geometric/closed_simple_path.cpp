// A C++ program to find simple closed path for n points 
#include <cstdlib>
#include <iostream>
using namespace std; 

struct point 
{ int x, y; 
}; 

// A global point needed for sorting points with reference 
// to the first point. Used in compare function of qsort() 
point p0; 

// A utility function to swap two points 
void swap(point &p1, point &p2) 
{point temp = p1; 
 p1 = p2; 
 p2 = temp; 
} 

// A utility function to return square of distance between 
// p1 and p2 
int dist(point p1, point p2) 
{return (p1.x - p2.x) * (p1.x - p2.x) + 
		(p1.y - p2.y) * (p1.y - p2.y); 
} 

// To find orientation of ordered triplet (p, q, r). 
// The function returns following values 
// 0 --> p, q and r are colinear 
// 1 --> Clockwise 
// 2 --> Counterclockwise 
int orientation(point p, point q, point r) 
{int val = (q.y - p.y) * (r.x - q.x) - 
			(q.x - p.x) * (r.y - q.y); 
 if (val == 0) return 0; // colinear 
 return (val > 0)? 1: 2; // clockwise or counterclock wise 
} 

// A function used by library function qsort() to sort 
// an array of points with respect to the first point 
int compare(const void *vp1, const void *vp2) 
{point *p1 = (point *)vp1; 
 point *p2 = (point *)vp2; 
 // Find orientation 
 int o = orientation(p0, *p1, *p2);
 if (o == 0) // p0,p1,p2 colinear
	return (dist(p0, *p2) >= dist(p0, *p1))? -1 : 1; 
 return (o == 2)? -1: 1; 
} 

// Prints simple closed path for a set of n points. 
void printClosedPath(point points[], int n) 
{// Find the bottommost point 
 int ymin = points[0].y, min = 0; 
 for (int i = 1; i < n; i++) 
   {int y = points[i].y; 

	// Pick the bottom-most. In case of tie, chose the 
	// left most point 
	if ((y < ymin) || (ymin == y && 
		points[i].x < points[min].x)) 
		ymin = points[i].y, min = i; 
   } 

 // Place the bottom-most point at first position 
 swap(points[0], points[min]); 

 // Sort n-1 points with respect to the first point. 
 // A point p1 comes before p2 in sorted ouput if p2 
 // has larger polar angle (in counterclockwise 
 // direction) than p1 
 p0 = points[0]; 
 qsort(&points[1], n-1, sizeof(point), compare); 

 // Now stack has the output points, print contents 
 // of stack 
 for (int i = 0; i < n; i++) 
	cout << "(" << points[i].x << ", "
		 << points[i].y <<"), "; 
 cout << endl;		 
} 

// Driver program to test above functions 
int main() 
{ 
	point points[] = {{0, 3}, {1, 1}, {2, 2}, {4, 4}, 
					  {0, 0}, {1, 2}, {3, 1}, {3, 3}}; 
	int n = sizeof(points)/sizeof(points[0]); 
	printClosedPath(points, n); 
	return 0; 
} 

