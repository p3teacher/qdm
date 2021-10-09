# code-01.py
#
import turtle as tt
#
win = tt.Screen()
win.setup(400,300)
tt.setposition(0,0)
tt.setheading(90)
# tt.color('green')
for i in (1,2,3,4):
    if (i % 2) == 0:
        tt.color('green')
    else :
        tt.color('red')
    # end if
    tt.forward(50)
    tt.left(90)
    # tt.setposition(0,0)
# end for
# win.mainloop()