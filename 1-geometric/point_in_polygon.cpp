#include <iostream>
using namespace std;
const int Nmax = 100;
struct point{int x, y;};
struct line{point p1, p2;};
point polygon[Nmax];

int ccw(point a, point b, point c) 
{return (b.x - a.x) * (c.y - a.y) - (c.x - a.x) * (b.y - a.y);
}

bool intersect(line a, line b) 
{if (ccw(a.p1, a.p2, b.p1) * ccw(a.p1, a.p2, b.p2) > 0) return false;
 if (ccw(b.p1, b.p2, a.p1) * ccw(b.p1, b.p2, a.p2) > 0) return false;
 return true;
}
int inside(point t, point p[], int N)
{int i, count = 0, j = 0;
 line lt,lp;
 p[0] = p[N]; p[N + 1] = p[1];
 lt.p1 = t; lt.p2 = t; lt.p2.x = INT_MAX;
 for (i = 1; i <= N; i++)
   {lp.p1 = p[i]; lp.p2 = p[i];
    if (!intersect(lp,lt))
      {lp.p2 = p[j]; j = i;
       if (intersect(lp, lt)) count++;
      }
   }
 return count;
}

int main()
{int n = 8;
 polygon[1].x = 0;
 polygon[1].y = 0;
 polygon[2].x = 2;
 polygon[2].y = 0;
 polygon[3].x = 2;
 polygon[3].y = 2;
 polygon[4].x = 3;
 polygon[4].y = 2;
 polygon[5].x = 3;
 polygon[5].y = 0;
 polygon[6].x = 4;
 polygon[6].y = 0;
 polygon[7].x = 4;
 polygon[7].y = 4;
 polygon[8].x = 0;
 polygon[8].y = 4;
 point test = {1, 1};
 cout << inside(test, polygon, 8) << endl;
 line l;
 l.p1 = polygon[3]; 
 l.p2 = polygon[4];
 cout << intersect(l, l) << endl;
 line l1, l2;
 l1.p1 = polygon[5];
 l1.p2 = polygon[5];
 l2.p1 = polygon[3];
 l2.p2 = polygon[4];
 cout << intersect(l1, l2) << endl;

 return 0;   
}
