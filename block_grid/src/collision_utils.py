def is_diamond_point_collision(p0, p1, p2, p3, pt):
	return is_triangle_point_collision(p0, p1, p2, pt) or is_triangle_point_collision(p2, p3, p0, pt)


def is_triangle_point_collision(p0, p1, p2, pt) :
    b1 = sign(pt, p0, p1) < 0.0
    b2 = sign(pt, p1, p2) < 0.0
    b3 = sign(pt, p2, p0) < 0.0

    return b1 == b2 and b2 == b3;

def is_circle_point_collision(centre, radius, pt):
	sq_x = (centre[0] - pt[0])**2
	sq_y = (centre[1] - pt[1])**2

	return sq_x + sq_y <= radius**2


def sign(p0, p1, p2):
    return (p0[0] - p2[0]) * (p1[1] - p2[1]) - (p1[0] - p2[0]) * (p0[1] - p2[1])