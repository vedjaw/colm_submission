PROBLEMS = [
  {
    "id": "length_hard_01",
    "category": "length",
    "coord": "Triangle ABC has vertices A(0,0), B(5,0), and C(3,4). Find the length of the internal angle bisector of angle A, terminating at side BC.",
    "euclid": "In Triangle ABC, the side lengths are AB = 5, AC = 5, and BC = 2√5. Find the length of the internal angle bisector drawn from vertex A to side BC.",
    "vector": "Let vectors u = (5,0) and v = (3,4). Find the length of the segment along the angle bisector of u and v, extending from the origin to the line segment connecting the endpoints of u and v.",
    "answer": "3.162"
  },
  {
    "id": "length_hard_02",
    "category": "length",
    "coord": "Find the perpendicular distance between the parallel lines 3x + 4y - 10 = 0 and 3x + 4y + 15 = 0.",
    "euclid": "Two parallel lines have a slope of -0.75. The vertical distance (difference in y-intercepts) between them is 6.25. Find the perpendicular distance between these two lines.",
    "vector": "Two lines share the normal vector n = (3, 4). One line satisfies n·r = 10 and the other satisfies n·r = -15. Find the distance between these two lines.",
    "answer": "5"
  },
  {
    "id": "length_hard_03",
    "category": "length",
    "coord": "Triangle vertices are A(-2, 0), B(6, 0), and C(2, 6). Find the length of the median drawn from vertex C to side AB.",
    "euclid": "A triangle has side lengths AC = √52, BC = √52, and AB = 8. Find the length of the median drawn to side AB.",
    "vector": "Let position vectors a = (-2, 0), b = (6, 0), and c = (2, 6). Let m be the midpoint of the segment connecting a and b. Find the magnitude of vector (c - m).",
    "answer": "6"
  },
  {
    "id": "length_hard_04",
    "category": "length",
    "coord": "Point P is at (10, 7). A circle is defined by the equation (x-2)^2 + (y-1)^2 = 36. Find the length of the tangent segment from P to the circle.",
    "euclid": "A circle has a radius of 6. A point P is located at a distance of 10 units from the center of the circle. Find the length of the tangent segment drawn from P to the circle.",
    "vector": "Let point p = (10, 7) and the center of a circle c = (2, 1). The circle has a radius magnitude of 6. Find the magnitude of the tangent vector from p to the circle.",
    "answer": "8"
  },
  {
    "id": "length_hard_05",
    "category": "length",
    "coord": "Find the length of the projection of the segment connecting A(1,1) and B(4,5) onto the line 4x - 3y = 0.",
    "euclid": "A line segment AB has length 5. The line containing AB has a slope of 4/3. Find the length of the projection of AB onto a line that also has a slope of 4/3.",
    "vector": "Let vector u = (3, 4). Find the scalar projection of u onto the direction vector v = (3, 4).",
    "answer": "5"
  },
  {
    "id": "length_hard_11",
    "category": "length",
    "coord": "Find the shortest distance from the point P(10, 0) to the circle x^2 + y^2 = 36.",
    "euclid": "A point P is at a distance of 10 from the center of a circle with radius 6. Find the shortest distance from P to the circumference of the circle.",
    "vector": "Let c = (0,0) be the center of a circle with radius magnitude 6. Let p = (10,0). Find the value of |p - c| - radius.",
    "answer": "4"
  },
  {
    "id": "length_hard_12",
    "category": "length",
    "coord": "Find the length of the segment of the line 3x + 4y = 12 intercepted between the coordinate axes.",
    "euclid": "A straight line forms a right-angled triangle with the axes. The legs of the triangle have lengths 4 and 3. Find the length of the hypotenuse.",
    "vector": "Find the magnitude of the vector connecting the points a and b, where a is the intersection of the line n·r = 12 with the x-axis, and b is the intersection with the y-axis. Normal n=(3,4).",
    "answer": "5"
  },
  {
    "id": "length_hard_13",
    "category": "length",
    "coord": "Two points A(-2, -3) and B(4, 5) are given. Find the length of the projection of AB onto the x-axis.",
    "euclid": "A line segment AB has length 10. The angle it makes with the horizontal axis is arcsin(0.8). Find the length of the horizontal component of the segment.",
    "vector": "Let u = (6, 8) be the vector from A to B. Find the scalar projection of u onto the unit vector i = (1, 0).",
    "answer": "6"
  },
  {
    "id": "length_hard_14",
    "category": "length",
    "coord": "Find the side length of an equilateral triangle whose vertices lie on a circle of radius 10.",
    "euclid": "A circle with radius 10 circumscribes an equilateral triangle. Find the side length of the triangle.",
    "vector": "Three vectors of magnitude 10 sum to zero (origin at circumcenter). The angle between any two is 120 degrees. Find the magnitude of the difference between any two vectors.",
    "answer": "17.32"
  },
  {
    "id": "length_hard_15",
    "category": "length",
    "coord": "Find the length of the diagonal of a rectangle with vertices (0,0), (8,0), (8,6), (0,6).",
    "euclid": "A rectangle has sides of length 8 and 6. Find the length of the diagonal.",
    "vector": "Let u = (8, 0) and v = (0, 6). Find the magnitude of the vector u + v.",
    "answer": "10"
  },
  {
    "id": "area_hard_11",
    "category": "area",
    "coord": "Find the area of the rhombus with vertices at (2,0), (0,3), (-2,0), and (0,-3).",
    "euclid": "A rhombus has diagonals of lengths 4 and 6. Find its area.",
    "vector": "The diagonals of a quadrilateral are represented by vectors d1 = (4, 0) and d2 = (0, 6). The diagonals are perpendicular. Find the area using 0.5 * |d1| * |d2|.",
    "answer": "12"
  },
  {
    "id": "area_hard_12",
    "category": "area",
    "coord": "Find the area of the triangle formed by the tangent to the circle x^2 + y^2 = 25 at the point (3, 4) and the coordinate axes.",
    "euclid": "In a right triangle formed by a tangent line and the axes, the altitude to the hypotenuse is 5 (radius). The point of tangency divides the hypotenuse into segments. Actually, simpler: The distance from origin to line is 5. The normal vector is (3,4). Intercepts are 25/3 and 25/4. Find area.",
    "vector": "A line has normal vector n = (3, 4) and passes through p = (3, 4). Find the area of the triangle formed by this line and the axes (directions (1,0) and (0,1)).",
    "answer": "26.04"
  },
  {
    "id": "area_hard_13",
    "category": "area",
    "coord": "Calculate the area of the triangle with vertices A(1, 1), B(2, 3), and C(5, 1).",
    "euclid": "A triangle has a base of length 4 (horizontal segment from x=1 to x=5). The height corresponding to this base is 2 (y=3 minus y=1). Find the area.",
    "vector": "Let u = (4, 0) and v = (1, 2). Find the area of the triangle spanned by these vectors using the cross product magnitude / 2.",
    "answer": "4"
  },
  {
    "id": "area_hard_14",
    "category": "area",
    "coord": "Find the area of the sector of the circle x^2 + y^2 = 100 subtended by the arc between (10,0) and (6, 8).",
    "euclid": "A circle has radius 10. An arc subtends a central angle where cos(theta) = 0.6. Find the area of the sector. (theta = 53.13 degrees). Area = (theta/360) * pi * r^2.",
    "vector": "Let u = (10, 0) and v = (6, 8). Find the angle theta between them. Calculate area = 0.5 * |u|^2 * theta (in radians).",
    "answer": "46.36"
  },
  {
    "id": "area_hard_15",
    "category": "area",
    "coord": "Find the area of the region bounded by the ellipse x^2/16 + y^2/9 = 1.",
    "euclid": "An ellipse has a semi-major axis of 4 and a semi-minor axis of 3. Find its area using the formula Area = pi * a * b.",
    "vector": "A linear transformation maps the unit circle (area pi) to an ellipse by scaling x by 4 and y by 3. The determinant of the transformation is 12. Find the new area.",
    "answer": "37.70"
  },

  
  {
    "id": "ratio_hard_21",
    "category": "ratio",
    "coord": "In triangle A(0,0), B(6,0), C(3,9), the centroid G divides the median from C in the ratio 2:1. Find the y-coordinate of G.",
    "euclid": "A triangle has a height of 9 relative to base AB. The centroid is located on the median. Find the perpendicular distance from the centroid to the base.",
    "vector": "Let a=(0,0), b=(6,0), c=(3,9). Centroid g = (a+b+c)/3. Find the y-component of g.",
    "answer": "3"
  },
  {
    "id": "ratio_hard_22",
    "category": "ratio",
    "coord": "Two similar triangles have side lengths in the ratio 1:3. Find the ratio of their areas.",
    "euclid": "Triangle A is similar to Triangle B. The sides of B are 3 times the length of the sides of A. Find the ratio of Area(A) to Area(B).",
    "vector": "Let Area1 be defined by 0.5|u x v|. Area2 is defined by 0.5|(3u) x (3v)|. Find the ratio Area1/Area2.",
    "answer": "0.111"
  },

  
  {
    "id": "ratio_hard_06",
    "category": "ratio",
    "coord": "Triangle ABC has vertices A(0,6), B(0,0), C(8,0). Point D is on AB such that AD:DB = 1:2. Point E is on AC such that AE:EC = 1:2. Find DE.",
    "euclid": "In a right triangle with legs 6 and 8, a line segment connects points on the two legs that divide the legs in a 1:2 ratio from the vertex A (hypotenuse not involved). Find length DE.",
    "vector": "Let a=(0,6), b=(0,0), c=(8,0). d = (2a+1b)/3. e = (2a+1c)/3. Actually, section formula is (m x2 + n x1)/(m+n). AD:DB=1:2 means D is 1/3 way from A. Find |d-e|.",
    "answer": "2.667"
  },
  {
    "id": "ratio_hard_07",
    "category": "ratio",
    "coord": "Point P(x,y) divides the segment connecting A(1,1) and B(9,9) externally in the ratio 3:1.",
    "euclid": "Segment AB has length 8sqrt(2). Point P is on the extension of AB such that AP = 3 * BP. Find the distance from Origin to P.",
    "vector": "Let a=(1,1), b=(9,9). p = (3b - 1a) / (3-1). Find magnitude |p|.",
    "answer": "18.385"
  },
  {
    "id": "ratio_hard_08",
    "category": "ratio",
    "coord": "In Triangle ABC (A=0,4; B=-3,0; C=3,0), the Incenter I divides the angle bisector of A in what ratio AI:ID? (D is on BC).",
    "euclid": "In an isosceles triangle with sides 5, 5, 6, find the ratio in which the incenter divides the altitude (angle bisector) from the vertex.",
    "vector": "Let a=(0,4), b=(-3,0), c=(3,0). Side lengths c=5, b=5, a=6. Ratio AI:ID = (b+c)/a.",
    "answer": "1.667"
  },
  {
    "id": "angle_hard_06",
    "category": "angle",
    "coord": "Find the angle in degrees between the tangents drawn from point P(5, 0) to the circle x^2 + y^2 = 9.",
    "euclid": "A circle has radius 3. A point P is at distance 5 from the center. Tangents are drawn from P to the circle. Find the angle between the two tangents.",
    "vector": "Let center c=(0,0) and point p=(5,0). Radius r=3. The angle theta between tangents is 2 * arcsin(r / |p-c|).",
    "answer": "73.74"
  },
  {
    "id": "angle_hard_07",
    "category": "angle",
    "coord": "Two circles intersect: x^2+y^2=4 and (x-3)^2+y^2=4. Find the angle of intersection (angle between tangents at intersection).",
    "euclid": "Two circles with radius 2 have centers 3 units apart. Find the angle between their tangents at the point of intersection.",
    "vector": "Let r1 and r2 be radius vectors to the intersection point. Find angle between the normal vectors (radii) alpha. Intersection angle = 180 - alpha.",
    "answer": "82.82"
  },
  {
    "id": "angle_hard_08",
    "category": "angle",
    "coord": "Find the angle between the lines y = 2x and y = 0.5x.",
    "euclid": "Two lines pass through the origin. One has slope 2, the other slope 0.5. Find the angle between them.",
    "vector": "Let u=(1,2) and v=(2,1). Find the angle between u and v.",
    "answer": "36.87"
  },
  {
    "id": "angle_hard_09",
    "category": "angle",
    "coord": "Triangle ABC has A(0,0), B(5,0), C(3, 4). Find angle C in degrees.",
    "euclid": "Triangle sides are c=5, b=5, a=sqrt(20). It is isosceles. Find the angle opposite the base c.",
    "vector": "Let u = (0,0)-(3,4) = (-3,-4) and v = (5,0)-(3,4) = (2,-4). Find angle between u and v.",
    "answer": "63.43"
  },
  {
    "id": "angle_hard_10",
    "category": "angle",
    "coord": "Find the angle between the vector (1,1,1) and the x-axis (1,0,0).",
    "euclid": "A diagonal of a cube connects opposite corners. Find the angle this diagonal makes with one of the edges meeting at the corner.",
    "vector": "Let u=(1,1,1) and v=(1,0,0). Calculate arccos((u.v) / (|u||v|)).",
    "answer": "54.74"
  },
  {
    "id": "area_hard_06",
    "category": "area",
    "coord": "Find the area of the quadrilateral with vertices (1,1), (3,4), (5,3), and (4,1).",
    "euclid": "A quadrilateral has vertices at (1,1), (3,4), (5,3), and (4,1) taken in order. Find the area of the quadrilateral.",
    "vector": "Let a=(1,1), b=(3,4), c=(5,3), and d=(4,1). Find the area of the quadrilateral using the shoelace (polygon area) formula.",
    "answer": 7
  },
  {
    "id": "area_hard_07",
    "category": "area",
    "coord": "Find the area of the triangle formed by the tangent to the curve y = 4 - x^2 at x = 1, the normal at x = 1, and the x-axis.",
    "euclid": "A right-angled triangle has a vertex at (1,3). The altitude from this vertex to the hypotenuse is 3. The hypotenuse lies on the x-axis. The slopes of the two legs are -2 (tangent) and 0.5 (normal). Find the area.",
    "vector": "Let v1 be a vector along the tangent (1, -2) and v2 be a vector along the normal (2, 1). Find the area of the triangle bounded by these vectors originating from (1,3) and the line y=0.",
    "answer": "11.25"
  },
  {
    "id": "area_hard_08",
    "category": "area",
    "coord": "Find the area of the incircle of the triangle with vertices A(0,0), B(6,0), and C(0,8).",
    "euclid": "In a right triangle with legs 6 and 8, find the area of the inscribed circle (Use pi = 3.14159).",
    "vector": "Triangle defined by vectors u=(6,0) and v=(0,8). Find area of its incircle.",
    "answer": "12.566"
  },
  {
    "id": "area_hard_09",
    "category": "area",
    "coord": "Find the area of the region satisfying 1 <= x^2 + y^2 <= 9.",
    "euclid": "Find the area of the annulus formed by two concentric circles with radii 1 and 3.",
    "vector": "Let R be the region where the magnitude of position vector r satisfies 1 <= |r| <= 3. Find the area of R.",
    "answer": "25.133"
  },
  {
    "id": "area_hard_10",
    "category": "area",
    "coord": "Find the area of a regular hexagon with vertices at (±1, 0), (±0.5, ±0.866).",
    "euclid": "A regular hexagon has a side length of 1. Find its area.",
    "vector": "Six vectors of magnitude 1 radiate from the origin, separated by 60 degrees. Find the total area of the 6 equilateral triangles formed.",
    "answer": "2.598"
  },
  {
    "id": "length_hard_06",
    "category": "length",
    "coord": "Find the length of the chord formed by the intersection of the line x - y + 2 = 0 and the circle x^2 + y^2 = 25.",
    "euclid": "A circle has a radius of 5. A chord is drawn at a perpendicular distance of √2 from the center. Find the length of this chord.",
    "vector": "Let a circle be defined by |r| = 5. A line is defined by r·n = 2 where n is the unit normal vector (1/√2, -1/√2). Find the length of the segment of the line intersecting the circle.",
    "answer": "9.591"
  },
  {
    "id": "length_hard_07",
    "category": "length",
    "coord": "Two circles have equations (x-1)^2 + y^2 = 4 and (x-9)^2 + y^2 = 36. Find the length of their common external tangent.",
    "euclid": "Two circles have radii 2 and 6. The distance between their centers is 8. Find the length of the common external tangent segment connecting the two points of tangency.",
    "vector": "Two circles with centers c1=(1,0) and c2=(9,0) have radii r1=2 and r2=6. Find the magnitude of the vector connecting the points of tangency of the common external tangent.",
    "answer": "6.928"
  },
  {
    "id": "length_hard_08",
    "category": "length",
    "coord": "Triangle ABC has vertices A(0, 5), B(12, 0), and C(0, 0). Find the length of the altitude drawn from vertex C to the hypotenuse AB.",
    "euclid": "In a right-angled triangle with legs of length 5 and 12, find the length of the altitude drawn from the right angle to the hypotenuse.",
    "vector": "Let a=(0,5), b=(12,0) and c=(0,0) define a triangle. Find the length of the perpendicular from c to the line segment ab.",
    "answer": "4.615"
  },
  {
    "id": "length_hard_09",
    "category": "length",
    "coord": "Find the distance between the Centroid and the Circumcenter of the triangle with vertices A(0,0), B(6,0), C(0,8).",
    "euclid": "In a right triangle with legs 6 and 8, find the distance between the intersection of the medians (centroid) and the midpoint of the hypotenuse (circumcenter).",
    "vector": "Let a=(0,0), b=(6,0), c=(0,8). Let g be its centroid and o its circumcenter. Find |g - o|.",
    "answer": "1.667"
  },
  {
    "id": "length_hard_10",
    "category": "length",
    "coord": "Point P(2,3) lies inside a rectangle with vertices at (0,0), (6,0), (6,4), (0,4). Find the sum of the squares of the distances from P to the four corners.",
    "euclid": "A point P is inside a rectangle of width 6 and height 4. P is 2 units from the left edge and 3 units from the bottom edge. Calculate PA^2 + PB^2 + PC^2 + PD^2.",
    "vector": "Let p=(2,3). Vertices are a=(0,0), b=(6,0), c=(6,4), d=(0,4). Find the sum of the squares of the distances from p to the four vertices.",
    "answer": "60"
  },
  {
    "id": "ratio_hard_31",
    "category": "ratio",
    "coord": "In Triangle ABC with vertices A(0,0), B(5,0), C(0,12), point P is the incenter. Find the ratio of the x-coordinate of P to the y-coordinate of P.",
    "euclid": "In a right triangle with side lengths 5, 12, and 13, find the ratio of the x-coordinate to the y-coordinate of the incenter, assuming the right angle is at the origin and the legs lie along the coordinate axes.",
    "vector": "Let points a=(0,0), b=(5,0), and c=(0,12) form a triangle. Let P be its incenter. Find the ratio of the x-coordinate of P to its y-coordinate.",
    "answer": "1"
  },
  {
    "id": "ratio_hard_32",
    "category": "ratio",
    "coord": "Point P divides the segment connecting A(1,1) and B(4,10) in the ratio k:1. If P lies on the line y = 2x, find k.",
    "euclid": "A line segment connects (1,1) and (4,10). A point P on this segment also lies on the line y=2x. Find the ratio AP/PB.",
    "vector": "Let points a=(1,1) and b=(4,10) define a line segment. A point p on this segment also lies on the line y = 2x. Find the ratio in which p divides the segment ab.",
    "answer": "0.5"
  },
  {
    "id": "ratio_hard_33",
    "category": "ratio",
    "coord": "Find the ratio of the area of the circle inscribed in an equilateral triangle to the area of the circumscribed circle.",
    "euclid": "For an equilateral triangle, find the ratio of the area of its incircle to the area of its circumcircle.",
    "vector": "An equilateral triangle has an inscribed circle and a circumscribed circle. Find the ratio of the areas of these two circles.",
    "answer": "0.25"
  },
  {
    "id": "ratio_hard_34",
    "category": "ratio",
    "coord": "Point P lies on the segment AB with A(0,0) and B(6,8). If distance AP = 5, find the ratio AP:AB.",
    "euclid": "Segment AB has length 10. Point P is on the segment at distance 5 from A. Find the ratio of the length AP to the length AB.",
    "vector": "Let points a and b define a segment of length 10, and let point p lie on the segment at a distance 5 from a. Find the ratio of the length ap to the length ab.",
    "answer": "0.5"
  },
  {
    "id": "ratio_hard_35",
    "category": "ratio",
    "coord": "Two squares have diagonals of length 2 and 6. Find the ratio of their areas.",
    "euclid": "Two squares have diagonals of lengths 2 and 6. Find the ratio of their areas.",
    "vector": "Two squares have diagonals of lengths 2 and 6. Find the ratio of their areas.",
    "answer": "0.111"
  },
  {
    "id": "angle_hard_31",
    "category": "angle",
    "coord": "Find the angle in degrees between the line 2x - y = 0 and the parabola y = x^2 at the point (2,4).",
    "euclid": "A line connects the origin to (2,4). Find the angle between the line and the tangent.",
    "vector": "Let vector direction of line be (1, 2). Let vector direction of tangent be (1, 4). Find the angle between these two vectors.",
    "answer": "12.53"
  },
  {
    "id": "angle_hard_32",
    "category": "angle",
    "coord": "Find the angle between the vectors u = (3, 4) and v = (-4, 3).",
    "euclid": "Two vectors have slopes 4/3 and -3/4. What is the angle?",
    "vector": "Find the angle between the vectors (3,4) and (−4,3).",
    "answer": "90"
  },
  {
    "id": "angle_hard_33",
    "category": "angle",
    "coord": "Find the angle subtended by the side of a regular pentagon at the center.",
    "euclid": "A regular pentagon is inscribed in a circle. Find the central angle subtended by one side.",
    "vector": "Let five unit vectors originate from a common point and point toward the vertices of a regular pentagon arranged symmetrically in a plane. Find the angle between any two consecutive vectors.",
    "answer": "72"
  },
  {
    "id": "angle_hard_34",
    "category": "angle",
    "coord": "A circular sector has a perimeter equal to half the circumference of its circle. Find the angle of the sector.",
    "euclid": "In a circle, a sector is formed such that the total length of its boundary is equal to half the circumference of the circle. Determine the measure of the sector’s angle.",
    "vector": "Two radius vectors of a circle form a sector whose boundary length equals half the circumference of the circle. Find the angle between the two vectors.",
    "answer": "60"
  },
  {
    "id": "angle_hard_35",
    "category": "angle",
    "coord": "Find the angle between the diagonal of a cube and the diagonal of one of its faces (meeting at the same vertex).",
    "euclid": "In a unit cube, find the angle between the vector (1,1,1) and the vector (1,1,0).",
    "vector": "Let two vectors originate from the same point in three-dimensional space, one directed along a body diagonal of a cube and the other along a diagonal of one of its faces. Find the angle between the two vectors.",
    "answer": "35.26"
  },
  {
    "id": "area_hard_31",
    "category": "area",
    "coord": "Find the area of the regular hexagon inscribed in the circle x^2 + y^2 = 100.",
    "euclid": "A regular hexagon is inscribed in a circle of radius 10. Find its area.",
    "vector": "Six vectors of equal magnitude originate from the same point and are equally spaced in a plane. Their magnitude is 10. The endpoints of the vectors form a regular polygon. Find the area enclosed by this polygon.",
    "answer": "259.81"
  },
  {
    "id": "area_hard_32",
    "category": "area",
    "coord": "Find the area of the triangle formed by the normal to the curve y = x^2 at (1,1), the tangent at (1,1), and the x-axis.",
    "euclid": "At the point (1,1) on the curve y=x^2 passing through that point, a tangent and a normal are drawn. These two lines intersect the x-axis at distinct points. Find the area of the triangle formed by the point (1,1) and these two intersection points.",
    "vector": "From the point (1,1), two perpendicular directions are determined by the geometry of the curve y=x^2 at that point. Lines drawn in these directions intersect the x-axis at two points. Find the area of the triangle formed by the point (1,1) and these two intersection points.",
    "answer": "1.25"
  },
################################
################################################################
################################################################
################################################################
################################################################
  # i was here previously
################################################################

################################################################
################################################################

  {
    "id": "area_hard_33",
    "category": "area",
    "coord": "Find the area of the quadrilateral with vertices A(1,1), B(2,4), C(5,5), D(6,1).",
    "euclid": "A quadrilateral has four vertices A, B, C, and D arranged in order in a plane. The positions of these vertices are A(1, 1), B(2, 4), C(5, 5), and D(6, 1). Find the area of the quadrilateral.",
    "vector": "Let a, b, c, and d be the position vectors of four points in the plane such that. Let a=(1,1), b=(2,4), c=(5,5), d=(6,1). Find the area of the quadrilateral formed by these points using the shoelace formula.",
    "answer": "14"
  },
  {
    "id": "area_hard_34",
    "category": "area",
    "coord": "Find the area of the region bounded by the inequality max(|x|, |y|) <= 2.",
    "euclid": "A square is centered at the origin with side length 4 (sides are x=2, x=-2, etc). Find its area.",
    "vector": "Find the area of the polygon vertices (2,2), (-2,2), (-2,-2), (2,-2).",
    "answer": "16"
  },
  {
    "id": "area_hard_35",
    "category": "area",
    "coord": "Find the surface area of a sphere inscribed in a cube of volume 64.",
    "euclid": "A cube has volume 64. A sphere is placed inside the cube so that it touches all six faces. Find the surface area of the sphere.",
    "vector": "Consider a cube of volume 64. A sphere is positioned inside the cube such that it touches each face of the cube. Find the surface area of the sphere.",
    "answer": "50.27"
  },
  {
    "id": "length_hard_31",
    "category": "length",
    "coord": "Find the distance from the point (5, 12) to the circle x^2 + y^2 = 1.",
    "euclid": "A point is located at coordinates (5,12). A circle with radius 1 is centered at the origin. Find the shortest distance from the point to the circle.",
    "vector": "Let p be the position vector of a point in the plane such that p = 5i + 12j. Let C be the set of all position vectors r satisfying ‖r‖ = 1. Find the shortest distance from the point represented by p to the set C.",
    "answer": "12"
  },
  {
    "id": "length_hard_32",
    "category": "length",
    "coord": "Triangle ABC has vertices A(1,1), B(4,5), C(1,5). Find the length of the altitude from A to BC.",
    "euclid": "In the plane, triangle ABC has vertices A(1,1), B(4,5), and C(1,5). An altitude is drawn from vertex A to the side BC. Find the length of this altitude.",
    "vector": "Let a, b, and c be the position vectors of three points in the plane such that a=(1,1), b=(4,5), c=(1,5). Find the length of the perpendicular from point a to the line defined by points b and c.",
    "answer": "4"
  },
  {
    "id": "length_hard_33",
    "category": "length",
    "coord": "Find the length of the segment of the line y = x cut off by the parabola y = x^2 - 2.",
    "euclid": "A straight line passes through the origin and makes equal angles with the coordinate axes. A parabola opens upward and intersects this line at two distinct points. The line and the parabola are given by the relations y=x and y=x^2−2 respectively. Find the length of the segment of the line lying between the two points of intersection.",
    "vector": "Find the magnitude of the difference vector between the two solutions to the system r_y = r_x and r_y = r_x^2 - 2.",
    "answer": "4.243"
  },
  {
    "id": "length_hard_34",
    "category": "length",
    "coord": "Find the distance between the circumcenter and the orthocenter of the triangle with vertices (0,0), (6,0), (0,8).",
    "euclid": "In a right triangle with legs 6 and 8, find the distance between the circumcenter and the orthocenter.",
    "vector": "Let a=(0,0), b=(6,0), c=(0,8). Orthocenter is denoted by h and the circumcenter by o. Find |o-h|.",
    "answer": "5"
  },

  
  {
    "id": "ratio_hard_36",
    "category": "ratio",
    "coord": "Point P lies on the line segment connecting A(1, 1) and B(4, 7). The y-coordinate of P is 5. Find the ratio AP:PB.",
    "euclid": "Segment AB has vertical height 6. Point P is at vertical height 4 from A. Find the ratio of the segments cut by P.",
    "vector": "Let a and b be position vectors of two distinct points in the plane, where a=i+j,b=4i+7j. A point with position vector p lies on the line segment joining a and b. The j-component of p is equal to 5. Find the ratio in which p divides the segment joining a and b..",
    "answer": "2"
  },
  {
    "id": "ratio_hard_37",
    "category": "ratio",
    "coord": "In a parallelogram ABCD, E is the midpoint of BC. Diagonal BD intersects AE at F. Find the ratio BF:FD.",
    "euclid": "A line is drawn from vertex A to the midpoint of the opposite side BC. It intersects the diagonal BD. The centroid of triangle ABC lies on the median AE? No, BD is a diagonal. Use mass points or similarity. Triangles BFE and DFA are similar. Ratio BE:DA = 1:2.",
    "vector": "Let a, b, c, d be vertices. e = (b+c)/2. Intersect line(a,e) and line(b,d). Find ratio.",
    "answer": "0.5"
  },
  {
    "id": "ratio_hard_38",
    "category": "ratio",
    "coord": "Triangle ABC has vertices A(0,0), B(3,0), C(0,4). The circle inscribed in the triangle touches BC at P. Find the ratio BP:PC.",
    "euclid": "In a right-angled triangle with side lengths 3, 4, and 5, a circle is inscribed in the triangle. The circle touches the hypotenuse at point P. Find the ratio in which point P divides the hypotenuse.",
    "vector": "Let triangle ABC have position vectors A=(0,0),B=(3,0),C=(0,4). A circle is inscribed in the triangle and touches segment BC at point P. Determine the ratio",
    "answer": "0.667"
  },
  {
    "id": "ratio_hard_39",
    "category": "ratio",
    "coord": "Find the ratio of the volume of a sphere to the volume of the cylinder circumscribing it.",
    "euclid": "A sphere of radius r is inside a cylinder of radius r and height 2r. Find V_sphere / V_cylinder.",
    "vector": "Calculate (4/3 pi r^3) / (pi r^2 * 2r).",
    "answer": "0.667"
  },
  {
    "id": "ratio_hard_40",
    "category": "ratio",
    "coord": "Points A(2,2) and B(8,8) define a line segment. A point P divides the segment AB externally in the ratio 3:1. Find the distance from A to P.",
    "euclid": "A line segment AB has length 6√2. A point P lies on the extension of AB such that P divides AB externally in the ratio 3:1. Find the distance from A to P.",
    "vector": "Let points A and B have position vectors (2,2) and (8,8) respectively. A point P divides the segment AB externally in the ratio 3:1. Determine the magnitude of the vector AP.",
    "answer": "12.72"
  },
  {
    "id": "angle_hard_36",
    "category": "angle",
    "coord": "Find the angle in degrees between the planes 2x - y + z = 0 and x + y + 2z = 0.",
    "euclid": "Two planes have normal vectors (2, -1, 1) and (1, 1, 2). Find the angle between the planes.",
    "vector": "Let n1 = (2, -1, 1) and n2 = (1, 1, 2). Determine the angle in degrees between the directions represented by these vectors.",
    "answer": "60"
  },
  {
    "id": "angle_hard_37",
    "category": "angle",
    "coord": "Find the angle between the asymptotes of the hyperbola x^2 - y^2 = 1.",
    "euclid": "A rectangular hyperbola has asymptotes y=x and y=-x. Find the angle between them.",
    "vector": "Find the angle between the vectors (1,1) and (1,-1).",
    "answer": "90"
  },
  {
    "id": "angle_hard_38",
    "category": "angle",
    "coord": "Find the angle subtended by the arc of a circle of radius 10 if the chord length is 10.",
    "euclid": "A chord of length 10 is drawn in a circle of radius 10. Find the central angle.",
    "vector": "Two position vectors u, v have magnitude 10. |u-v| = 10. Find the angle between u and v.",
    "answer": "60"
  },
  {
    "id": "angle_hard_39",
    "category": "angle",
    "coord": "Find the inclination angle (in degrees) of the line joining (2,3) and (5, 6).",
    "euclid": "A line has a slope of 1. What angle does it make with the positive x-axis?",
    "vector": "Find the angle between the vector (1, 0) and the vector (3, 3).",
    "answer": "45"
  },
  {
    "id": "angle_hard_40",
    "category": "angle",
    "coord": "Find the angle between the face diagonal and the space diagonal of a cube intersecting at a vertex.",
    "euclid": "In a unit cube, find the angle between the vector (1,1,0) and the vector (1,1,1).",
    "vector": "Let u = (1, 1, 0) and v = (1, 1, 1). Find the angle between them in degrees.",
    "answer": "35.26"
  },
  {
    "id": "area_hard_36",
    "category": "area",
  "coord": "Find the area of the polygon formed by the points (0,0), (2,1), (1,3), and (-1,2).",
  "euclid": "A quadrilateral has vertices at the points (0,0), (2,1), (1,3), and (-1,2). Find the area of the quadrilateral.",
  "vector": "Let a = (0,0), b = (2,1), c = (1,3), and d = (-1,2) be position vectors of the vertices of a quadrilateral taken in order. Determine the area of the quadrilateral.",
    "answer": "5"
  },
  {
    "id": "area_hard_37",
    "category": "area",
    "coord": "Find the area of the region defined by x^2 + y^2 <= 4 and y >= 0.",
    "euclid": "Find the area of a semi-circle with radius 2.",
    "vector": "Consider all vectors in the plane whose magnitude is at most 2 and whose endpoints lie in the upper half-plane. Find the area of the region formed by these vectors.",
    "answer": "6.283"
  },
  {
    "id": "area_hard_38",
    "category": "area",
    "coord": "Find the area of the triangle formed by the tangent to y=1/x at x=1, the x-axis, and the y-axis.",
    "euclid": "A curve y=1/x has a tangent drawn at (1,1). This tangent forms a triangle with the coordinate axes. Find its area.",
    "vector": "Consider the curve defined by the position vector r(t)=(t,1/t). A tangent is drawn to this curve at t=1. This tangent forms a triangle with the coordinate axes. Find the area of this triangle.",
    "answer": "2"
  },
  {
    "id": "area_hard_39",
    "category": "area",
    "coord": "Find the area of the quadrilateral bounded by 2x + 3y = 12, x=0, y=0, and x=3.",
    "euclid": "A plane region is bounded by the x-axis, the y-axis, the vertical line x = 3, and a straight line passing through the points (0,4) and (3,2). Find the area of the region.",    
    "vector": "Consider the region in the plane bounded by the vectors corresponding to the points (0,0), (3,0), (3,2), and (0,4), taken in order. Determine the area of this region.",
    "answer": "9"
  },
  {
    "id": "area_hard_40",
    "category": "area",
    "coord": "Find the area of the locus of points P such that the sum of the distances from P to (3,0) and (-3,0) is 10.",
    "euclid": "The locus is an ellipse with foci at (+/-3, 0) and major axis length 2a=10. Find the area of the ellipse",
    "vector": "Calculate the area for an ellipse where 2a=10 and 2ae = 6.",
    "answer": "62.83"
  },
  {
    "id": "length_hard_36",
    "category": "length",
    "coord": "Find the distance from the point P(1, 2, 3) to the z-axis.",
  "euclid": "Given a point P with coordinates (1, 2, 3) in three-dimensional space, find its perpendicular distance from the z-axis.",    
  "vector": "Let the position vector of a point be (1, 2, 3). Determine the shortest distance from this point to the z-axis.",
    "answer": "2.236"
  },
  {
    "id": "length_hard_37",
    "category": "length",
    "coord": "Find the length of the segment of the line x/3 + y/4 = 1 intercepted by the coordinate axes.",
    "euclid": "A ladder rests against a wall. The foot of the ladder is 3 units from the wall, and the top is 4 units from the floor. Find the length of the ladder.",
    "vector": "Find the magnitude of the vector connecting the points where the line n·r = 12 (with n=(4,3)) intersects the axes.",
    "answer": "5"
  },
  {
    "id": "length_hard_38",
    "category": "length",
    "coord": "Two circles are given by the equations x^2 + y^2 = 4 and (x - 3)^2 + y^2 = 1. The circles touch externally at a point P. Find the distance from P to the point (-2, 0).",
    "euclid": "Two circles have radii 2 and 1, and their centers are 3 units apart. They touch externally at a point P. Find the distance from P to the point on the larger circle that lies directly opposite P along the line joining the centers.",
    "vector": "Two circles have centers at (0,0) and (3,0) with radii 2 and 1 respectively. They touch externally at a point P. Determine the distance from P to the point (-2, 0).",
    "answer": "4"
  },
  {
    "id": "length_hard_39",
    "category": "length",
    "coord": "Find the maximum distance from the origin to any point on the ellipse x^2 + 4y^2 = 16.",
    "euclid": "An ellipse has a major axis of length 8 and minor axis of length 4. Find the length of the semi-major axis.",
  "vector": "Let r = (x, y) be the position vector of a point on an ellipse centered at the origin whose major axis has length 8 and minor axis has length 4. Determine the maximum possible magnitude of r.",
          "answer": "4"
  },
  {
    "id": "length_hard_40",
    "category": "length",
    "coord": "Find the length of the projection of vector A(2, 3, 6) onto the vector B(1, 2, 2).",
  "euclid": "A directed segment from the origin ends at the point (2, 3, 6). Find the component of this segment in the direction of the vector (1, 2, 2).",
  "vector": "Let two vectors be given by (2, 3, 6) and (1, 2, 2). Determine the magnitude of the component of the first vector in the direction of the second vector.",
          "answer": "6.667"
  },

  {
    "id": "length_hard_35",
    "category": "length",
    "coord": "Find the length of the curve defined by r(t) = (3cos(t), 3sin(t)) for 0 <= t <= pi.",
    "euclid": "Find the length of a semi-circle with radius 3.",
    "vector": "Let r(t)=(3cos⁡t,3sin⁡t) for 0≤t≤π. Find the length of the curve traced by this vector.",
    "answer": "9.425"
  },
  {
    "id": "ratio_hard_26",
    "category": "ratio",
    "coord": "Point P divides the chord connecting A(5,0) and B(0,5) on the circle x^2+y^2=25 in the ratio 1:1. Find the distance from the origin to P.",
    "euclid": "Find the distance from the center of a circle to the midpoint of a chord of length 5sqrt(2). Radius is 5.",
    "vector": "Let a=(5,0) and b=(0,5). p is the midpoint of ab. Find |p|.",
    "answer": "3.536"
  },
  {
    "id": "ratio_hard_27",
    "category": "ratio",
    "coord": "In triangle ABC with vertices A(0,0), B(10,0), C(5, 8.66), find the ratio of the circumradius to the inradius.",
    "euclid": "An equilateral triangle has side length 10. Find the ratio R/r.",
    "vector": "Calculate R (circumradius) and r (inradius) for the triangle defined by a,b,c. Return R/r.",
    "answer": "2"
  },

  ################################
################################################################
################################################################
################################################################
################################################################
  # i was here previously
################################################################

################################################################
################################################################
  {
  "id": "ratio_hard_28",
  "category": "ratio",
  "coord": "Line L passes through A(2,0) and B(0,4). Point P lies on L and has x-coordinate -1. Find the ratio AP:AB.",
  "euclid": "Points A and B are 2 units right and 4 units up from the origin respectively. A line passes through A and B. A point P on this line has x-coordinate -1. Find the ratio of the distance from A to P to the distance from A to B.",
  "vector": "Let a = (2,0) and b = (0,4). A point p lies on the line through a and b and has x-coordinate -1. Determine the ratio |p-a| / |b-a|.",
  "answer": "1.5"
},
  {
  "id": "ratio_hard_29",
  "category": "ratio",
  "coord": "Square ABCD has vertices (0,0), (4,0), (4,4), (0,4). Point E lies on BC such that BE:EC = 1:3. Line AE intersects diagonal BD at F. Find the ratio BF:FD.",
  "euclid": "In a square of side length 4, a point E lies on side BC such that BE:EC = 1:3. A line is drawn from vertex A to E and it meets diagonal BD at F. Find the ratio BF:FD.",
  "vector": "Let a = (0,0), b = (4,0), c = (4,4), and d = (0,4). A point e lies on segment bc such that BE:EC = 1:3. The line joining a and e intersects the line joining b and d at f. Determine the ratio |f-b| / |d-f|.",
  "answer": "0.25"
},
  {
  "id": "ratio_hard_30",
  "category": "ratio",
  "coord": "Two spheres have radii 2 and 3 units respectively. Find the ratio of their surface areas.",
  "euclid": "The volumes of two spheres are in the ratio 8:27. Determine the ratio of their surface areas.",
  "vector": "Two spheres are centered at the origin with radii equal to the magnitudes of vectors of lengths 2 and 3. Find the ratio of their surface areas.",
  "answer": "0.444"
}
,
  {
  "id": "angle_hard_26",
  "category": "angle",
  "coord": "Find the angle in degrees between the hour and minute hands of a clock at 3:30.",
  "euclid": "At 3:30, determine the smaller angle formed between the hour hand and the minute hand of a clock.",
  "vector": "Represent the hour and minute hands of a clock at 3:30 as two rays originating from the center. Find the measure in degrees of the angle between them.",
  "answer": "75"
},
  {
    "id": "angle_hard_27",
    "category": "angle",
    "coord": "Find the angle of elevation of the vector (1, 1, sqrt(2)) from the xy-plane.",
    "euclid": "A line segment connects the origin to (1,1,0) (length sqrt(2)). A vertical pole of height sqrt(2) stands at (1,1). Find the angle of elevation from the origin to the top of the pole.",
    "vector": "Let u = (1, 1, sqrt(2)). Find the angle between u and its projection on the xy-plane v = (1, 1, 0).",
    "answer": "45"
  },
  {
    "id": "angle_hard_28",
    "category": "angle",
    "coord": "Find the angle between the two tangents drawn from (0,0) to the circle (x-5)^2 + y^2 = 9.",
    "euclid": "A circle has radius 3 and its center is 5 units from point P. Find the angle between the two tangents drawn from P.",
    "vector": "Let c = (5, 0) be the center of a circle of radius 3, and let p = (0, 0) be a point outside the circle. Two tangent segments are drawn from p to the circle. Find the angle between these two tangent segments.",
    "answer": "73.74"
  },
  {
    "id": "angle_hard_29",
    "category": "angle",
    "coord": "Find the angle between the diagonals of a rhombus with vertices (0,0), (5,0), (8,4), (3,4).",
    "euclid": "A rhombus has vertices (0,0), (5,0), (8,4), and (3,4). Find the angle between its diagonals.",    
    "vector": "Let a = (0,0), b = (5,0), c = (8,4), and d = (3,4) be the vertices of a rhombus taken in order. Determine the angle between the diagonals ac and bd.",
    "answer": "90"
  },
  {
    "id": "angle_hard_30",
    "category": "angle",
    "coord": "Find the angle in degrees between the lines connecting (1,0) to (0,1) and (1,0) to (2,1).",
    "euclid": "Triangle with vertices A(1,0), B(0,1), C(2,1). Find the angle at vertex A.",
    "vector": "Let a=(1,0), b=(0,1), c=(2,1). Find the angle between vector (b-a) and (c-a).",
    "answer": "90"
  },
  {
    "id": "area_hard_26",
    "category": "area",
    "coord": "Find the area of the largest square that can be inscribed in a circle of radius 2.",
    "euclid": "A circle has diameter 4. A square is inscribed in it. Find the area of the square.",
    "vector": "Four vectors of magnitude 2 form the vertices of a square centered at the origin. Find the area of the polygon formed by these vectors.",
    "answer": "8"
  },
  {
    "id": "area_hard_27",
    "category": "area",
    "coord": "Find the area of the region bounded by y = 0, x = 1, x = 4, and y = 3x.",
    "euclid": "A trapezoid has parallel vertical sides of height 3 and 12. The width of the base connecting them is 3. Find the area.",
    "vector": "Find the area of the trapezoid with vertices (1,0), (4,0), (4,12), (1,3).",
    "answer": "22.5"
  },
  {
    "id": "area_hard_28",
    "category": "area",
    "coord": "Find the total surface area of a tetrahedron with vertices (0,0,0), (1,0,0), (0,1,0), (0,0,1).",
    "euclid": "A tetrahedron has vertices at (0,0,0), (1,0,0), (0,1,0), and (0,0,1). Find its total surface area.",
    "vector": "Calculate the sum of the areas of the four triangular faces defined by the origin and unit vectors i, j, k.",
    "answer": "2.366"
  },
  {
    "id": "area_hard_29",
    "category": "area",
    "coord": "Find the area of a sector of a circle with radius 4 and arc length 2pi.",
    "euclid": "A circle has radius 4. A sector of the circle has arc length 2π. Find the area of the sector.",
    "vector": "Two radius vectors of length 4 form a sector whose arc between their endpoints has length 2π. Determine the area of this sector.",
    "answer": "12.566"
  },
  {
  "id": "area_hard_30",
  "category": "area",
  "coord": "Find the area of the triangle formed by the lines y = x, y = -x, and y = 6.",
  "euclid": "A triangle is bounded by the lines y = x, y = -x, and y = 6. Find its area.",
  "vector": "Find the area of the triangle with vertices (0,0), (6,6), and (-6,6).",
  "answer": "36"
},
  {
    "id": "length_hard_26",
    "category": "length",
    "coord": "Find the length of the common chord of the circles x^2 + y^2 = 25 and (x-4)^2 + y^2 = 25.",
    "euclid": "Two circles of radius 5 intersect. The distance between their centers is 4. Find the length of the common chord connecting their intersection points.",
    "vector": "Two circles have centers at the origin and at (4,0), both with radius magnitude 5. Find the magnitude of the vector connecting the two intersection points.",
    "answer": "9.165"
  },
  {
    "id": "length_hard_27",
    "category": "length",
    "coord": "Find the distance from the point (1, 2, 3) to the origin.",
    "euclid": "A box has dimensions 1, 2, and 3. Find the length of the space diagonal connecting opposite corners.",
    "vector": "Let position vector p = (1, 2, 3). Find the magnitude |p|.",
    "answer": "3.742"
  },
  {
    "id": "length_hard_28",
    "category": "length",
    "coord": "Find the length of the altitude to the side of length 10 in a triangle with sides 10, 10, 12.",
    "euclid": "An isosceles triangle has sides of length 10, 10, and 12. Find the length of the altitude drawn to one of the sides of length 10.",
    "vector": "Let vectors u and v represent sides of a triangle such that |u|=10, |v|=12, and |u-v|=10. Find the magnitude of the component of v perpendicular to u.",
    "answer": "9.6"
  },
  {
    "id": "length_hard_29",
    "category": "length",
    "coord": "Find the distance between the point (2,2) and the line x + y = 8.",
    "euclid": "A line intersects the axes at (8,0) and (0,8). Find the shortest distance from the point (2,2) to this line.",
    "vector": "Let point p = (2,2). A line is defined by normal n=(1,1) and passes through a point where n.r = 8. Find the distance from p to the line.",
    "answer": "2.828"
  },
  {
    "id": "length_hard_30",
    "category": "length",
    "coord": "Find the radius of the circumcircle of the triangle with vertices (0,0), (6,0), (0,8).",
    "euclid": "A right-angled triangle has legs of length 6 and 8. Find the radius of the circle that passes through all three vertices.",
    "vector": "Three points a, b, c form a right triangle. |b-a|=6, |c-a|=8. Find the magnitude of the vector from the hypotenuse midpoint to any vertex.",
    "answer": "5"
  },

  {
    "id": "ratio_hard_23",
    "category": "ratio",
    "coord": "Point P divides the segment connecting A(2,2) and B(5,5) such that AP:PB = 2:1. Find the x-coordinate of P.",
    "euclid": "A segment AB has horizontal projection length 3. Point P divides the segment in ratio 2:1 from A. Find the horizontal coordinate of P given A's x is 2.",
    "vector": "Let a = (2,2) and b = (5,5). A point p lies on the segment joining a and b such that AP:PB = 2:1. Find the first coordinate of p.",
    "answer": "4"
  },
  {
    "id": "ratio_hard_24",
    "category": "ratio",
    "coord": "The diagonals of a parallelogram with vertices (0,0), (4,0), (5,2), (1,2) intersect at M. Find the ratio AM:MC.",
    "euclid": "In any parallelogram, the diagonals bisect each other. Find the ratio of the segments of the diagonal.",
    "vector": "Let a=(0,0) and c=(5,2). Let m be the midpoint of ac. Find the ratio |m-a| / |c-m|.",
    "answer": "1"
  },
  {
    "id": "ratio_hard_25",
    "category": "ratio",
    "coord": "A point P lies on the line passing through A(0,0) and B(4,3). If P has x-coordinate 8, find the ratio AP:AB.",
    "euclid": "A segment AB has length 5. Point P lies on the extension of AB such that its distance from the origin is 10. Find the ratio of the distance AP to the distance AB.",
    "vector": "Let a=(0,0) and b=(4,3). Point p is such that p = 2b. Find the ratio |p-a| / |b-a|.",
    "answer": "2"
  },
  {
    "id": "angle_hard_21",
    "category": "angle",
    "coord": "Find the angle in degrees between the planes x + y + z = 0 and z = 0.",
    "euclid": "One plane is the xy-plane. Another plane passes through the origin and satisfies the equation x + y + z = 0. Find the angle between these two planes.",
    "vector": "Consider two planes passing through the origin: one defined by z = 0 and the other defined by x + y + z = 0. Determine the acute angle between them.",
    "answer": "54.74"
  },
  {
    "id": "angle_hard_22",
    "category": "angle",
    "coord": "Find the angle subtended by a diameter of the circle x^2 + y^2 = 1 at any point on the circumference (excluding the diameter endpoints).",
    "euclid": "A triangle is inscribed in a circle such that one side is the diameter. Find the angle of the vertex opposite the diameter.",
    "vector": "Let a = (-1,0) and b = (1,0). Let p be any point satisfying x^2 + y^2 = 1, where p is not equal to a or b. Find the angle between the vectors (p - a) and (p - b).",
    "answer": "90"
  },
  {
    "id": "angle_hard_23",
    "category": "angle",
    "coord": "Find the angle between the lines y = x and y = 3x.",
"euclid": "Two straight lines pass through the origin. One rises one unit vertically for every unit horizontally, and the other rises three units vertically for every unit horizontally. Find the angle between the two lines.",
    "vector": "Let u = (1, 1) and v = (1, 3). Find the angle between u and v.",
    "answer": "26.57"
  },
  {
    "id": "angle_hard_24",
    "category": "angle",
    "coord": "Find the angle in degrees of the sector of a circle of radius 5 if the arc length is 5.",
    "euclid": "An arc of length 5 is drawn on a circle of radius 5. Find the central angle subtended by this arc in degrees.",
    "vector": "A circle has radius 5. A sector is formed by two radius vectors whose endpoints on the circle are separated by an arc of length 5. Determine the measure of the angle between the two radius vectors in degrees.",
    "answer": "57.30"
  },
  {
    "id": "angle_hard_25",
    "category": "angle",
    "coord": "Find the angle between the position vector of point P(1, sqrt(3)) and the position vector of point Q(-sqrt(3), 1).",
    "euclid": "Points P and Q lie on a circle centered at the origin with radius 2. The coordinates of P are (1, √3) and the coordinates of Q are (−√3, 1). Find the angle between OP and OQ.",
    "vector": "Let p = (1, sqrt(3)) and q = (-sqrt(3), 1). Find the angle between p and q.",
    "answer": "90"
  },
  {
    "id": "area_hard_21",
    "category": "area",
    "coord": "Find the area of the triangle defined by the vertices A(1,0,0), B(0,1,0), and C(0,0,1) in 3D space.",
    "euclid": "A triangle in three-dimensional space has vertices at (1,0,0), (0,1,0), and (0,0,1). Find its area.",
    "vector": "Let a = (1,0,0), b = (0,1,0), and c = (0,0,1). Determine the area of the triangle formed by these three points.",

    "answer": "0.866"
  },
  {
    "id": "area_hard_22",
    "category": "area",
    "coord": "Find the area of the region bounded by |x| + |y| = 2.",
    "euclid": "A square is centered at the origin and rotated 45 degrees such that its vertices lie on the axes at distance 2 from the center. Find the area of the square.",
    "vector": "Find the area of the polygon with vertices v1=(2,0), v2=(0,2), v3=(-2,0), v4=(0,-2).",
    "answer": "8"
  },
  {
    "id": "area_hard_23",
    "category": "area",
    "coord": "Find the area of the parallelogram formed by the vectors representing sides from origin to A(3,0) and B(1,2).",
    "euclid": "Two adjacent sides of a parallelogram are represented by segments from the origin to the points (3,0) and (1,2). Find the area of the parallelogram formed by these sides.",    
    "vector": "Let u = (3,0) and v = (1,2). Determine the area of the parallelogram formed by these two vectors.",
    "answer": "6"
  },
  {
    "id": "area_hard_24",
    "category": "area",
    "coord": "Find the area of the ellipse defined by x^2/4 + y^2 = 1.",
    "euclid": "An ellipse has a semi-major axis of 2 and a semi-minor axis of 1. Find its area.",
    "vector": "A linear map scales the unit circle (area pi) by a factor of 2 in the x-direction and 1 in the y-direction. Find the area of the resulting shape.",
    "answer": "6.283"
  },
  {
    "id": "area_hard_25",
    "category": "area",
    "coord": "Find the area of the triangle with vertices A(0,0), B(4,2), and C(2,4).",
    "euclid": "A triangle has vertices at (0,0), (4,2), and (2,4). Find its area.",
    "vector": "Let u = (4,2) and v = (2,4). Determine the area of the triangle formed by the origin and the endpoints of u and v.",
    "answer": "6"
  },
  {
    "id": "length_hard_21",
    "category": "length",
    "coord": "Find the length of the shortest path from A(0, 1) to the x-axis and then to B(4, 1).",
    "euclid": "Points A and B are both located 1 unit vertically above a straight line L. The horizontal distance between A and B is 4 units. Find the minimum length of a path that goes from A to a point on L and then to B.",
    "vector": "Let a = (0, 1) and b = (4, 1). Find the minimum magnitude of |p - a| + |b - p| where p is a vector of the form (x, 0).",
    "answer": "4.472"
  },
  {
    "id": "length_hard_22",
    "category": "length",
    "coord": "Find the distance between the parallel lines 2x + y = 0 and 2x + y - 10 = 0.",
    "euclid": "Two parallel lines have a slope of -2. One passes through the origin, and the other has a y-intercept of 10. Find the perpendicular distance between them.",
    "vector": "Two lines share the normal vector n = (2, 1). One satisfies n·r = 0, the other n·r = 10. Find the distance between the lines.",
    "answer": "4.472"
  },
  {
    "id": "length_hard_23",
    "category": "length",
    "coord": "Find the length of the tangent from the point P(8, 6) to the circle x^2 + y^2 = 25.",
    "euclid": "A circle has radius 5 and is centered at the origin. A point P has coordinates (8, 6). Find the length of the tangent drawn from P to the circle.",
    "vector": "Let c be the origin (0,0) and p = (8, 6). A circle centered at c has radius magnitude 5. Find the magnitude of the vector from p to a point t on the circle such that (p-t) is perpendicular to t.",
    "answer": "8.660"
  },
  {
    "id": "length_hard_24",
    "category": "length",
    "coord": "In the triangle with vertices A(0,0), B(6,0), and C(0,8), find the length of the segment connecting the midpoints of sides AB and AC.",
    "euclid": "A right-angled triangle has legs of length 6 and 8. Find the length of the midline segment connecting the midpoints of these two legs.",
    "vector": "Let a = (0,0), b = (6,0), and c = (0,8). Let m1 and m2 be the midpoints of segments ab and ac respectively. Find the distance between m1 and m2.",
    "answer": "5"
  },
  {
    "id": "length_hard_25",
    "category": "length",
    "coord": "Find the distance from the point (1, 1, 1) to the plane z = 0.",
    "euclid": "A point in 3D space is located at coordinates (1,1,1). Find the shortest distance from this point to the xy-plane.",
    "vector": "Let p = (1, 1, 1). Determine the shortest distance from p to the plane defined by z = 0.",
    "answer": "1"
  },
  {
    "id": "ratio_hard_16",
    "category": "ratio",
    "coord": "Point P divides the segment connecting A(10, 0) and B(0, 10) such that the distance from P to the origin is minimized. Find the ratio AP:PB.",
    "euclid": "In an isosceles right triangle with legs of length 10, a point P lies on the hypotenuse. P is the foot of the altitude from the right angle vertex to the hypotenuse. Find the ratio in which P divides the hypotenuse.",
    "vector": "Let a = (10, 0) and b = (0, 10). Find the point p on the line passing through a and b such that vector p is perpendicular to vector (b-a). Find the ratio |p-a| : |b-p|.",
    "answer": "1"
  },
  {
    "id": "ratio_hard_17",
    "category": "ratio",
    "coord": "In Triangle A(0,0) B(6,0) C(3, 3sqrt(3)), the orthocenter H divides the altitude from C in what ratio CH:HM (where M is on AB)?",
    "euclid": "A triangle has vertices at (0,0), (6,0), and (3, 3√3). Let H be its orthocenter and M the foot of the perpendicular from the top vertex to the base. Find the ratio CH:HM.",
    "vector": "Let a=(0,0), b=(6,0), c=(3, 3sqrt(3)). H is the orthocenter. M is the projection of C onto AB. Find the ratio |c-h| / |h-m|.",
    "answer": "2"
  },
  {
    "id": "ratio_hard_18",
    "category": "ratio",
    "coord": "Point P lies on the line joining A(2,2) and B(8,8). If the x-coordinate of P is 4, find the ratio AP:AB.",
    "euclid": "Points A, P, and B lie on the same straight line in that order. A has coordinates (2,2) and B has coordinates (8,8). The point P has coordinates (4,4). Find the ratio AP:AB.",
    "vector": "Let a = (2,2) and b = (8,8). A point p lies on the segment joining a and b and has coordinates (4,4). Determine the ratio |p - a| : |b - a|.",
    "answer": "0.333"
  },
  {
    "id": "ratio_hard_19",
    "category": "ratio",
    "coord": "Line L passes through A(0,4) and B(6,0). Point P on the line has y-coordinate 2. Find the ratio AP:PB.",
    "euclid": "A line segment connects the points (0,4) and (6,0). A point P on this segment has a height of 2 above the horizontal axis. Find the ratio AP:PB.",
    "vector": "Let a = (0,4) and b = (6,0). Point p on the segment ab has a vertical component of 2. Find the ratio |p-a| : |b-p|.",
    "answer": "1"
  },
  {
    "id": "ratio_hard_20",
    "category": "ratio",
    "coord": "Triangle ABC has vertices A(0,0), B(5,0), C(0,12). The bisector of angle B meets AC at D. Find the ratio AD:DC.",
    "euclid": "In a right triangle with legs AC=12 and AB=5, the hypotenuse is 13. The angle bisector of angle B divides the opposite side AC into segments AD and DC. Find the ratio AD:DC.",
    "vector": "Let a = (0,0), b = (5,0), and c = (0,12). The internal bisector of angle ABC meets the segment AC at point d. Find the ratio AD:DC.",
    "answer": "0.385"
  },
  {
    "id": "angle_hard_16",
    "category": "angle",
    "coord": "Find the angle in degrees between the lines x - 2y + 3 = 0 and 2x + y - 4 = 0.",
    "euclid": "Two straight lines are given by the equations x − 2y + 3 = 0 and 2x + y − 4 = 0. Find the angle between these lines in degrees.",
    "vector": "Find the angle between two lines with normal vectors n1 = (1, -2) and n2 = (2, 1).",
    "answer": "90"
  },
  {
    "id": "angle_hard_17",
    "category": "angle",
    "coord": "Find the angle subtended by the arc of the circle x^2 + y^2 = 1 from (1,0) to (-1,0) at the point (0,1).",
    "euclid": "A diameter of a circle connects points A and B. Point P is on the circumference equidistant from A and B. Find the angle APB.",
    "vector": "Let a=(1,0), b=(-1,0), and p=(0,1). Find the angle between the vector (a-p) and (b-p).",
    "answer": "90"
  },
  {
    "id": "angle_hard_18",
    "category": "angle",
    "coord": "Find the angle between the diagonal of the rectangle with vertices (0,0), (sqrt(3),0), (sqrt(3),1), (0,1) and the x-axis.",
    "euclid": "A rectangle has a base of length sqrt(3) and height 1. Find the angle the diagonal makes with the base.",
    "vector": "Let u = (sqrt(3), 1). Find the angle between u and the standard unit vector i = (1, 0).",
    "answer": "30"
  },
  {
    "id": "angle_hard_19",
    "category": "angle",
    "coord": "Two lines intersect at the origin. Line 1 passes through (3, 4). Line 2 passes through (4, 3). Find the acute angle between them.",
    "euclid": "Two straight lines pass through the origin. One passes through the point (3,4) and the other passes through the point (4,3). Find the acute angle between the two lines.",
    "vector": "Let u = (3,4) and v = (4,3). Determine the acute angle between the directions represented by these two vectors.",
    "answer": "16.26"
  },
  {
    "id": "angle_hard_20",
    "category": "angle",
    "coord": "Find the angle of intersection between the curves y = x^2 and y = sqrt(x) at the point (1,1).",
    "euclid": "The curves y = x^2 and y = √x intersect at the point (1,1). Find the angle between the two curves at this point.",
    "vector": "Let the curves be defined by y = x^2 and y = √x. Determine the angle between their tangent directions at the point (1,1).",
    "answer": "36.87"
  },
  {
    "id": "area_hard_16",
    "category": "area",
    "coord": "Find the area of the region strictly between the curves y = x^2 and y = 2x.",
    "euclid": "The curves y = x^2 and y = 2x enclose a finite region. Find the area of this region.",
  "vector": "Let r1(t) = (t, t^2) and r2(t) = (t, 2t). Determine the area of the region enclosed between these two curves.",

    "answer": "1.333"
  },
  {
    "id": "area_hard_17",
    "category": "area",
    "coord": "Find the area of the quadrilateral formed by the lines y = x, y = -x, y = x + 4, and y = -x + 4.",
    "euclid": "Four straight lines are given by the equations y = x, y = −x, y = x + 4, and y = −x + 4. These lines enclose a quadrilateral. Find its area.",
    "vector": "Find the area of the parallelogram defined by the intersection of four lines with normal vectors n1=(1,-1), n2=(1,1) and constants d1=0, d2=0, d3=-4, d4=4.",
    "answer": "8"
  },
  #below this
  {
    "id": "area_hard_18",
    "category": "area",
    "coord": "Find the area of the triangle with vertices A(0,0), B(5, 12), and C(12, 5).",
    "euclid": "A triangle has vertices at (0,0), (5,12), and (12,5). Find its area.",
    "vector": "Let u = (5,12) and v = (12,5). Determine the area of the triangle formed by the origin and the endpoints of these two vectors.",

    "answer": "59.5"
  },
  {
    "id": "area_hard_19",
    "category": "area",
    "coord": "Find the area of the largest rectangle that can be inscribed in the ellipse x^2/25 + y^2/9 = 1.",
    "euclid": "An ellipse has semi-major axis 5 and semi-minor axis 3. A rectangle is inscribed in the ellipse with its sides parallel to the coordinate axes. Find the maximum possible area of such a rectangle.",
    "vector": "Let the ellipse be defined by (x/5)^2 + (y/3)^2 = 1. A rectangle with vertices at (±x, ±y) lies inside this ellipse. Determine the greatest possible area of the rectangle.",
    "answer": "30"
  },
  {
    "id": "area_hard_20",
    "category": "area",
    "coord": "Find the area of the pentagon with vertices (0,0), (4,0), (5,2), (3,4), (0,3).",
    "euclid": "A pentagon has vertices at (0,0), (4,0), (5,2), (3,4), and (0,3), taken in order. Find its area.",
    "vector": "Let v1 = (0,0), v2 = (4,0), v3 = (5,2), v4 = (3,4), and v5 = (0,3). Determine the area of the polygon formed by these five points in this order.",
    "answer": "12.5"
  },
  
  {
    "id": "length_hard_16",
    "category": "length",
    "coord": "Two circles are defined by (x-1)^2 + y^2 = 9 and (x-9)^2 + y^2 = 16. Find the length of the internal common tangent segment connecting the two circles.",
    "euclid": "Two circles with radii 3 and 4 have their centers separated by a distance of 8 units. Find the length of the internal common tangent segment.",
    "vector": "Let c1 = (1, 0) and c2 = (9, 0) be the centers of two circles with radii r1 = 3 and r2 = 4 respectively. Find the magnitude of the internal common tangent vector connecting the circles.",
    "answer": "3.873"
  },
  {
    "id": "length_hard_17",
    "category": "length",
    "coord": "Find the distance from the point (4, 3) to the orthocenter of the triangle with vertices (0,0), (4,0), and (0,3).",
    "euclid": "A triangle has vertices at (0,0), (4,0), and (0,3). Let H be its orthocenter. Find the distance from H to the point (4,3).",
    "vector": "Let o = (0,0), a = (4,0), and b = (0,3) be the vertices of a triangle. If h denotes the orthocenter of this triangle, determine the distance from h to the point p = (4,3).",
    "answer": "5"
  },
  {
    "id": "length_hard_18",
    "category": "length",
    "coord": "Find the length of the chord cut from the line 3x + 4y = 12 by the circle x^2 + y^2 = 9.",
    "euclid": "A circle has a radius of 3. A straight line is located at a perpendicular distance of 2.4 units from the center of the circle. Find the length of the chord formed by the intersection of the line and the circle.",
    "vector": "A circle is defined by |r| = 3. A line is defined by n·r = 12, where n = (3, 4). Find the length of the segment of the line that lies inside the circle.",
    "answer": "3.6"
  },
  {
    "id": "length_hard_19",
    "category": "length",
    "coord": "Find the perimeter of the triangle formed by the points A(2,5), B(2,2), and C(6,2).",
    "euclid": "A right-angled triangle has a vertical leg of length 3 and a horizontal leg of length 4. Find the total perimeter of the triangle.",
    "vector": "Let a = (2,5), b = (2,2), and c = (6,2). Determine the perimeter of the triangle formed by these three vectors.",
    "answer": "12"
  },
  {
    "id": "length_hard_20",
    "category": "length",
    "coord": "Find the length of the bisector of the exterior angle at vertex A of the triangle with vertices A(0,0), B(4,0), C(0,3). (The bisector terminates on the extended line BC).",
    "euclid": "A triangle has vertices A, B, and C such that AB = 4, AC = 3, and BC = 5. The bisector of the exterior angle at vertex A meets the extension of side BC at point D. Find the length of AD.",
    "vector": "Let a = (0,0), b = (4,0), and c = (0,3). The exterior angle at a has a bisector that intersects the line through b and c at a point d. Determine the distance between a and d.",
    "answer": "16.97"
  },
  {
    "id": "ratio_hard_11",
    "category": "ratio",
    "coord": "Point P lies on the segment connecting A(1, 2) and B(9, 10). If the x-coordinate of P is 3, find the ratio AP:AB.",
    "euclid": "A point P lies on a line segment AB. The horizontal distance from A to B is 8. The horizontal distance from A to P is 2. Find the ratio of the length AP to the total length AB.",
    "vector": "Let a = (1,2) and b = (9,10). A point p lies on the segment joining a and b and has first coordinate equal to 3. Determine the ratio of the length AP to the length AB.",
    "answer": "0.25"
  },
  {
    "id": "ratio_hard_12",
    "category": "ratio",
    "coord": "Find the ratio in which the line y = x divides the segment connecting A(2, 3) and B(6, 1).",
    "euclid": "A segment connects the points (2,3) and (6,1). The straight line y = x intersects this segment. Determine the ratio in which the line divides the segment.",
    "vector": "Let a = (2,3) and b = (6,1). A point p lies on the segment joining a and b and also satisfies p_x = p_y. Determine the ratio AP:PB.",
    "answer": "0.2"
  },
  {
    "id": "ratio_hard_13",
    "category": "ratio",
    "coord": "In triangle ABC with vertices A(0,0), B(4,0), C(2,3), the centroid G divides the median from C in the ratio 2:1. Find the y-coordinate of G.",
    "euclid": "The height of a triangle is 3. The centroid is located at 1/3 of the height from the base. Find the perpendicular distance from the centroid to the base.",
    "vector": "Let a = (0,0), b = (4,0), and c = (2,3). If g denotes the centroid of triangle abc, determine the y-coordinate of g.",
    "answer": "1"
  },
  {
    "id": "ratio_hard_14",
    "category": "ratio",
    "coord": "Point C(-1, 2) divides the segment AB externally in the ratio 2:1. If A is (1, 4), find the distance AB.",
    "euclid": "Point C lies on the line determined by A and B but outside the segment AB. The distances satisfy AC : CB = 2 : 1. If A is (1,4) and C is (-1,2), find the length of AB.",
    "vector": "Let a = (1,4) and c = (-1,2). A point b lies on the line through a and c such that c divides the segment AB externally in the ratio 2:1. Determine the distance between a and b.",
    "answer": "1.414"
  },
  {
    "id": "ratio_hard_15",
    "category": "ratio",
    "coord": "Two similar triangles have areas 50 and 200. Find the ratio of their corresponding perimeters.",
    "euclid": "The area of shape A is 50. The area of similar shape B is 200. Find the ratio of the perimeter of A to the perimeter of B.",
    "vector": "Two similar figures are represented by corresponding vectors u, v and by scaled vectors u', v'. The areas of the two figures are 50 and 200. Determine the ratio of their corresponding perimeters.",
    "answer": "0.5"
  },
  {
    "id": "angle_hard_11",
    "category": "angle",
    "coord": "Find the acute angle in degrees between the lines y = 0 and y = x.",
    "euclid": "A line passes through the origin dividing the first quadrant exactly in half. What angle does it make with the horizontal axis?",
    "vector": "Find the angle between the vector i = (1, 0) and the vector v = (1, 1).",
    "answer": "45"
  },
  {
    "id": "angle_hard_12",
    "category": "angle",
    "coord": "Find the angle in degrees between the line x + sqrt(3)y + 5 = 0 and the x-axis.",
    "euclid": "A line has a slope of -1/sqrt(3). Find the acute angle this line makes with the horizontal.",
    "vector": "Let n = (1, √3). Determine the acute angle in degrees between the line defined by n · r + 5 = 0 and the x-axis.",
    "answer": "30"
  },
  {
    "id": "angle_hard_13",
    "category": "angle",
    "coord": "Find the angle subtended by the chord x + y = 1 at the center of the circle x^2 + y^2 = 1.",
    "euclid": "A chord of length sqrt(2) is drawn in a circle of radius 1. Find the central angle subtended by this chord in degrees.",
    "vector": "Points A(1,0) and B(0,1) lie on a unit circle. Find the angle between position vectors a and b.",
    "answer": "90"
  },
  {
    "id": "angle_hard_14",
    "category": "angle",
    "coord": "Find the interior angle A of the triangle with vertices A(0,0), B(3,0), C(1, sqrt(3)).",
    "euclid": "Triangle ABC has vertices A(0,0), B(3,0), and C(1, √3). Determine the measure of the interior angle at vertex A.",
    "vector": "Let u = (3, 0) and v = (1, sqrt(3)). Find the angle between u and v.",
    "answer": "60"
  },
  {
    "id": "angle_hard_15",
    "category": "angle",
    "coord": "Two vectors from the origin end at P(2,1) and Q(-1, 2). Find the angle between them.",
    "euclid": "Line OP has slope 0.5. Line OQ has slope -2. The product of slopes is -1. What is the angle?",
    "vector": "Let u = (2, 1) and v = (-1, 2). Calculate the dot product u·v. If zero, what is the angle?",
    "answer": "90"
  },

  {
    "id": "area_hard_01",
    "category": "area",
    "coord": "Find the area of the quadrilateral with vertices A(0,0), B(4,2), C(6,6), and D(2,5) listed in counterclockwise order.",
    "euclid": "A quadrilateral has vertices A(0,0), B(4,2), C(6,6), and D(2,5), taken in counterclockwise order. Find its area.",
    "vector": "Let position vectors be a=(0,0), b=(4,2), c=(6,6), and d=(2,5). Calculate the area of the quadrilateral formed by these points.",
    "answer": "13"
  },
  {
    "id": "area_hard_02",
    "category": "area",
    "coord": "Find the area of the triangle bounded by the lines y = x, y = 2x, and x + y = 6.",
    "euclid": "A triangle is formed by three straight lines. Two of the lines pass through the origin with slopes 1 and 2 respectively. The third line has both x and y intercepts equal to 6. Find the area of this triangle.",
    "vector": "Find the area of the triangle with vertices defined by the intersection of the vector lines r = s(1,1), r = t(1,2), and r = (6,0) + k(-1,1).",
    "answer": "3"
  },
  {
    "id": "area_hard_03",
    "category": "area",
    "coord": "Find the area of a triangle with vertices at coordinates (0,0), (14,0), and (5, 12).",
    "euclid": "Find the area of a triangle with side lengths 13, 14, and 15.",
    "vector": "Let vectors u and v represent two sides of a triangle such that |u| = 14, |v| = 13, and their dot product u·v = 70. Find the area of the triangle.",
    "answer": "84"
  },
  {
    "id": "area_hard_04",
    "category": "area",
    "coord": "Find the area of the triangle with vertices A(2, 3), B(5, 7), and C(5, 3).",
    "euclid": "A right-angled triangle has a hypotenuse of length 5. One leg is vertical and has length 4. The other leg is horizontal. Find the area of the triangle.",
    "vector": "Let a = (2,3), b = (5,7), and c = (5,3). Find the area of the triangle defined by these vectors.",
    "answer": "6"
  },
  {
    "id": "area_hard_05",
    "category": "area",
    "coord": "Find the area of the closed region defined by the inequality |x| + |y| ≤ 5.",
    "euclid": "A square is centered at the origin such that its diagonals lie on the x and y axes. The length of each diagonal is 10 units. Find the area of the square.",
    "vector": "Consider the polygon with vertices at v1=(5,0), v2=(0,5), v3=(-5,0), and v4=(0,-5). Find the area enclosed by this polygon.",
    "answer": "50"
  },


  {
    "id": "angle_hard_01",
    "category": "angle",
    "coord": "Find the acute angle in degrees between the lines 3x - y + 2 = 0 and 2x + y - 1 = 0.",
    "euclid": "Line A has a slope of 3. Line B has a slope of -2. Find the acute angle between Line A and Line B in degrees.",
    "vector": "Find the acute angle in degrees between two lines with normal vectors n1 = (3, -1) and n2 = (2, 1).",
    "answer": "45"
  },
  {
    "id": "angle_hard_02",
    "category": "angle",
    "coord": "Triangle ABC has vertices A(1,1), B(4,1), and C(1,5). Find the tangent of angle B.",
    "euclid": "A right-angled triangle has legs of length 3 and 4. Find the tangent of the angle adjacent to the leg of length 3.",
    "vector": "Let vector u = (-3, 0) and vector v = (-3, 4). Find the tangent of the angle between vectors u and v.",
    "answer": "1.333"
  },
  {
    "id": "angle_hard_03",
    "category": "angle",
    "coord": "Find the angle in degrees between the vectors represented by the diagonals of the quadrilateral with vertices (0,0), (2,0), (2,2), and (0,2).",
    "euclid": "Find the angle in degrees between the diagonals of a square.",
    "vector": "Let d1 = (2, 2) and d2 = (-2, 2). Find the angle between vectors d1 and d2 in degrees.",
    "answer": "90"
  },
  {
    "id": "angle_hard_04",
    "category": "angle",
    "coord": "Find the obtuse angle in degrees formed by the intersection of the line y = 0 and the line passing through the origin and (-1, √3).",
    "euclid": "A line passes through the origin and makes an angle of 120 degrees with the positive x-axis. Find the obtuse angle between this line and the positive x-axis.",
    "vector": "Let u = (1, 0) and v = (-0.5, 0.866). Find the angle between vectors u and v in degrees.",
    "answer": "120"
  },
  {
    "id": "angle_hard_05",
    "category": "angle",
    "coord": "Find the angle in degrees between the line passing through (0,0) and (1, √3) and the line passing through (0,0) and (√3, 1).",
    "euclid": "Line A has an inclination of 60 degrees. Line B has an inclination of 30 degrees. Find the angle between Line A and Line B.",
    "vector": "Let u = (1, √3) and v = (√3, 1). Find the angle between vectors u and v in degrees.",
    "answer": "30"
  },


  {
    "id": "ratio_hard_01",
    "category": "ratio",
    "coord": "Triangle ABC has vertices A(0,0), B(6,0), and C(0,8). The angle bisector of angle A intersects side BC at point D. Find the ratio BD : DC.",
    "euclid": "In a right-angled triangle with legs of length 6 and 8, the bisector of the right angle divides the hypotenuse into two segments. Find the ratio of the segment adjacent to the side of length 6 to the segment adjacent to the side of length 8.",
    "vector": "Let vectors b = (6,0) and c = (0,8) originate from a common point A. The angle bisector of the angle between b and c intersects the segment connecting the tips of b and c. Find the ratio in which the intersection point divides this segment.",
    "answer": "0.75"
  },
  {
    "id": "ratio_hard_02",
    "category": "ratio",
    "coord": "Point P(x, y) divides the segment connecting A(2, 2) and B(12, 7) internally in the ratio 3:2. Find the x-coordinate of P.",
    "euclid": "A line segment has endpoints A with x-coordinate 2 and B with x-coordinate 12. A point P divides the segment internally in the ratio 3:2, measured from A to B. Find the x-coordinate of P.",
    "vector": "Let a = (2, 2) and b = (12, 7). A point p lies on the segment joining a and b and divides it internally in the ratio 3:2 from a to b. Find the first component of p.",
    "answer": "8"
  },
  {
    "id": "ratio_hard_03",
    "category": "ratio",
    "coord": "In Triangle ABC, G is the centroid. A line is drawn from vertex A through G to intersect side BC at M. Find the numerical value of the ratio AG : GM.",
    "euclid": "In any triangle, a median connects a vertex to the midpoint of the opposite side. The centroid lies on this median. Find the ratio of the distance from the vertex to the centroid to the distance from the centroid to the midpoint.",
    "vector": "Let A, B, and C be position vectors of the vertices of a triangle. Let G be the centroid of the triangle, and let M be the midpoint of the side opposite A. A line is drawn from A through G meeting the opposite side at M. Find the ratio AG : GM.",
    "answer": "2"
  },
  {
    "id": "ratio_hard_04",
    "category": "ratio",
    "coord": "Line L intersects the x-axis at (4,0) and the y-axis at (0,3). Point P lies on L and has an x-coordinate of 2. Find the ratio AP : PB, where A is the x-intercept and B is the y-intercept.",
    "euclid": "A line segment connects the points (4,0) and (0,3). A point P lies on this segment and has an x-coordinate equal to 2. Find the ratio in which P divides the segment.",
    "vector": "Let a = (4, 0) and b = (0, 3). Point p lies on the segment ab such that its first component is 2. Find the ratio |p - a| / |b - p|.",
    "answer": "1"
  },
  {
    "id": "ratio_hard_05",
    "category": "ratio",
    "coord": "Triangle ABC has vertices A(0,0), B(4,0), and C(2,4). A line parallel to BC passes through the midpoint of AB and intersects AC at E. Find the ratio of the Area of triangle ADE to the Area of triangle ABC, where D is the midpoint of AB.",
    "euclid": "In triangle ABC, D is the midpoint of side AB. A line is drawn through D parallel to side BC and meets side AC at point E. Find the ratio of the area of triangle ADE to the area of triangle ABC.",
    "vector": "Let triangle ABC be defined by position vectors A, B, and C. Let D be the midpoint of AB. A line through D parallel to BC intersects AC at E. Find the ratio of the area of triangle ADE to the area of triangle ABC.",
    "answer": "0.25"
  }
]