























init python:

    class Puzzle(object):
        
        
        def __init__(self):
            
            
            
            LEFT=100
            TOP=100
            COL_SPACING = 200
            ROW_SPACING = 200
            self.COL_NUM = 4
            self.ROW_NUM = 3
            
            
            self.table = t = Table(base="card/base.png", back="card/base.png")
            
            rotate_random = [0,0,0,90,180,270]
            deck = []
            
            for i in range(0, self.COL_NUM):
                for j in range(0, self.ROW_NUM):
                    value = (i, j)
                    t.card(value, "card/room-%d-%d.png" % (i,j))
                    t.set_faceup(value, True)
                    t.set_rotate(value, renpy.random.choice(rotate_random))
                    deck.append(value)
            renpy.random.shuffle(deck)        
            
            
            self.foundations = [ ]
            for i in range(0, self.COL_NUM):
                for j in range(0, self.ROW_NUM):
                    s = t.stack(LEFT + COL_SPACING * i, TOP + ROW_SPACING * j, xoff=0, yoff=0, drag=DRAG_TOP, drop=True, click=True)
                    self.foundations.append(s)
                    s.append(deck.pop())
        
        
        
        
        def show(self):
            self.table.show()
        
        def hide(self):
            self.table.hide()
        
        
        def foundation_drag(self, evt):
            
            
            if len(evt.drag_cards) != 1:
                return False
            
            orig_s = evt.stack
            target_s = evt.drop_stack
            
            
            orig_c = evt.drag_cards[0]
            target_c = evt.drop_stack[-1]
            
            
            target_s.append(orig_c)
            orig_s.append(target_c)
            
            return "foundation_drag"
        
        def card_click(self, evt):
            orig_s = evt.stack
            
            
            
            if orig_s:
                orig_c = orig_s[-1]
                self.table.set_rotate(orig_c, self.table.get_rotate(orig_c) + 90)
            return "card_click %d" % self.table.get_rotate(orig_c)
        
        
        
        
        def interact(self):
            
            evt = ui.interact()
            rv = False
            
            
            
            if evt.type == "drag":
                if evt.drop_stack in self.foundations:
                    rv = self.foundation_drag(evt)
            
            elif evt.type == "click":
                rv = self.card_click(evt)
            
            
            
            
            
            for i in range(0, self.COL_NUM):
                for j in range(0, self.ROW_NUM):
                    f = self.foundations[j + (i*self.ROW_NUM)]
                    ii, jj =  f[0] 
                    
                    if (self.table.get_rotate(f[0]) % 360 != 0):
                        return rv
                    
                    if ii != i or jj != j:
                        return rv
            
            
            return "puzzlewin"
        
        
        def set_sensitive(self, value):
            self.table.set_sensitive(value)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
