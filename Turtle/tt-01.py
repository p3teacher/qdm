# tt-01.py
#
import turtle as tt
win = tt.Screen()
win.setup(400,300)
tt.setposition(0,0)
t_color = ('red', 'cyan', 'green', 'blue', 'purple', 'black')

tt.setheading(90)
# tt.color('green')
for i in (1,2,3,4):
    tt.color('green')
    tt.forward(50)
    tt.left(90)
    # tt.setposition(0,0)
# end for
# win.mainloop()
# -----------------------
"""
tt.setheading(90)
for i in (0,1,2,3,4) :
    tt.color(t_color[i])
    for j in (1,2,3):
        tt.forward(50)
        tt.left(120)
    # end for
    tt.setheading(90+(i+1)*72)
# end for
#
# -----------------------
tt.setheading(90)
for i in (0,1,2,3,4,5) :
    tt.color(t_color[i])
    for j in (1,2,3,4):
        tt.forward(50)
        tt.left(90)
    # end for
    tt.setheading(90+(i+1)*60)
# end for
# -----------------------
tt.setheading(90)
for i in (0,1,2,3,4) :
    tt.color(t_color[i])
    for j in (1,2,3,4,5):
        tt.forward(50)
        tt.left(72)
    # end for
    tt.setheading(90+(i+1)*72)
# end for
# win.mainloop()
"""