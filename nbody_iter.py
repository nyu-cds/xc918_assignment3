"""
    N-body simulation.

    Author: Xing Cui
    NetID: xc918

    Combination of improvement.
    "Reducing function call overhead
    Using alternatives to membership testing of lists
    Using local rather than global variables
    Using data aggregation to reduce loop overheads"
        
    First test, 86s.
    Second test, 86.9s.

    Running time of OPT: 25.9s(two times), and 26.5s. Happy ending.

    average_origin_time = (86+86.9)/2 = 86.45
    average_opt_time = (25.9*2+26.5)/3 = 26.1

    R = L_origin/L_opt = 3.31226
"""

"""
    Assignment5
    Date: Feb 25.
    Author: Xing Cui
    NetID: xc918
    
    Test 1: since last time I have used combinations from itertools, the first test I used *rest.
    Three trials of running time of nbody_iter.py: 25.8s, 25.5s, 25.8s.


"""

from itertools import combinations






def advance(dt, BODIES):
    '''
        advance the system one timestep
    '''

    for body1, body2 in Pairwise_name:
        ([x1, y1, z1], v1, m1) = BODIES[body1]
        ([x2, y2, z2], v2, m2) = BODIES[body2]
        (dx, dy, dz) = (x1-x2, y1-y2, z1-z2)#compute_deltas(x1, x2, y1, y2, z1, z2) modified.
        #update_vs(v1, v2, dt, dx, dy, dz, m1, m2) removed.
        mag = dt * ((dx * dx + dy * dy + dz * dz) ** (-1.5))
        mag_b1 = m1 * mag
        mag_b2 = m2 * mag
        v1[0] -= dx * mag_b2#compute_b(m2, dt, dx, dy, dz) modified.
        v1[1] -= dy * mag_b2#compute_b(m2, dt, dx, dy, dz) modified.
        v1[2] -= dz * mag_b2#compute_b(m2, dt, dx, dy, dz) modified.
        v2[0] += dx * mag_b1#compute_b(m1, dt, dx, dy, dz) modified.
        v2[1] += dy * mag_b1#compute_b(m1, dt, dx, dy, dz) modified.
        v2[2] += dz * mag_b1#compute_b(m1, dt, dx, dy, dz) modified.
        

    for body in BODIES.keys():
        (r, [vx, vy, vz], m) = BODIES[body]
        #update_rs(r, dt, vx, vy, vz) removed
        r[0] += dt * vx
        r[1] += dt * vy
        r[2] += dt * vz
    
    
def report_energy(BODIES, e=0.0):
    '''
        compute the energy and return it so that it can be printed
    '''
    for body1, body2 in Pairwise_name:
        ([x1, y1, z1], v1, m1) = BODIES[body1]
        ([x2, y2, z2], v2, m2) = BODIES[body2]
        (dx, dy, dz) = (x1-x2, y1-y2, z1-z2)#compute_deltas(x1, x2, y1, y2, z1, z2) removed.
        e -= (m1 * m2) / ((dx * dx + dy * dy + dz * dz) ** 0.5)#compute_energy(m1, m2, dx, dy, dz) removed.
    
        
    for body in BODIES:
        (r, [vx, vy, vz], m) = BODIES[body]
        e += m * (vx * vx + vy * vy + vz * vz) / 2.
        
    return e

def offset_momentum(ref, *rest):
    '''
        ref is the body in the center of the system
        offset values from this reference
    '''
    
    px=0.0
    py=0.0
    pz=0.0
    for arg in rest:
        for body in rest[0]:
            (r, [vx, vy, vz], m) = BODIES[body]
            px -= vx * m
            py -= vy * m
            pz -= vz * m
            
    (r, v, m) = ref
    v[0] = px / m
    v[1] = py / m
    v[2] = pz / m


def nbody(loops, *rest):#, reference, iterations, BODIES):
    '''
        nbody simulation
        loops - number of loops to run
        reference - body at center of system
        iterations - number of timesteps to advance
    '''
    # Set up global state
    offset_momentum(BODIES[rest[0]], BODIES)


    for _ in range(loops):
        for _ in range(rest[1]):#iterations):
            advance(0.01, rest[2])#BODIES)
        print(report_energy(rest[2]))#BODIES))
        

if __name__ == '__main__':
    PI = 3.14159265358979323
    SOLAR_MASS = 4 * PI ** 2
    DAYS_PER_YEAR = 365.24

    BODIES = {
        'sun': ([0.0, 0.0, 0.0], [0.0, 0.0, 0.0], SOLAR_MASS),

        'jupiter': ([4.84143144246472090e+00,
                     -1.16032004402742839e+00,
                     -1.03622044471123109e-01],
                    [1.66007664274403694e-03 * DAYS_PER_YEAR,
                     7.69901118419740425e-03 * DAYS_PER_YEAR,
                     -6.90460016972063023e-05 * DAYS_PER_YEAR],
                    9.54791938424326609e-04 * SOLAR_MASS),

        'saturn': ([8.34336671824457987e+00,
                    4.12479856412430479e+00,
                    -4.03523417114321381e-01],
                   [-2.76742510726862411e-03 * DAYS_PER_YEAR,
                    4.99852801234917238e-03 * DAYS_PER_YEAR,
                    2.30417297573763929e-05 * DAYS_PER_YEAR],
                   2.85885980666130812e-04 * SOLAR_MASS),

        'uranus': ([1.28943695621391310e+01,
                    -1.51111514016986312e+01,
                    -2.23307578892655734e-01],
                   [2.96460137564761618e-03 * DAYS_PER_YEAR,
                    2.37847173959480950e-03 * DAYS_PER_YEAR,
                    -2.96589568540237556e-05 * DAYS_PER_YEAR],
                   4.36624404335156298e-05 * SOLAR_MASS),

        'neptune': ([1.53796971148509165e+01,
                     -2.59193146099879641e+01,
                     1.79258772950371181e-01],
                    [2.68067772490389322e-03 * DAYS_PER_YEAR,
                     1.62824170038242295e-03 * DAYS_PER_YEAR,
                     -9.51592254519715870e-05 * DAYS_PER_YEAR],
                    5.15138902046611451e-05 * SOLAR_MASS)}


    Pairwise_name = set(combinations(BODIES,2))# combination gives all pairs of 5 factors, such as (sun, jupiter), (sun, uranus).

    nbody(100, 'sun', 20000, BODIES)
    

