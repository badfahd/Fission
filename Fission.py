from math import cos, pi, sin
import vpython as vp
scene = vp.canvas(title="Nuclear Fission", width=1600, height=900,center=vp.vector(0,0,0),resizable=True)


Nucleus = vp.sphere(pos=vp.vector(0, 0, 0), color=vp.color.red, radius=2)
Neutron = vp.sphere(pos=vp.vector(-4, 0, 0), radius=0.2, color=vp.color.white)

v = 2
dt = 0.01
fission_occured = False


while True:
  vp.rate(100)

  if not fission_occured:
    Neutron.pos.x += v * dt

    
    if vp.mag(Neutron.pos) <= Nucleus.radius:
      v = 0
      Nucleus.visible = False
      Neutron.visible = False

      
      frag_1 = vp.sphere(pos=Nucleus.pos, radius=1.0, color=vp.color.orange)
      v_frag1 = vp.vector(3 * cos(pi / 3), 3 * sin(pi / 3), 0)

      
      frag_2 = vp.sphere(pos=Nucleus.pos, radius=1.0, color=vp.color.orange)
      v_frag2 = vp.vector(3 * cos(-pi / 3), 3 * sin(-pi / 3), 0)

    
      neutrons = []
      vels = [
          vp.vector(6, 1, 0),  
          vp.vector(6, -1, 0),  
          vp.vector(5, 0, 0),  
      ]
      for vel in vels:
        n = vp.sphere(pos=Nucleus.pos, radius=0.2, color=vp.color.cyan)
        neutrons.append((n, vel))

      fission_occured = True
  else:
    
    frag_1.pos += v_frag1 * dt
    frag_2.pos += v_frag2 * dt

    
    for n, vel in neutrons:
      n.pos += vel * dt