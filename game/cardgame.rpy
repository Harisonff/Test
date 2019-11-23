























init python:

    import pygame

    DRAG_NONE = 0
    DRAG_CARD = 1
    DRAG_ABOVE = 2
    DRAG_STACK = 3
    DRAG_TOP = 4



    def _m1_cardgame__rect_overlap_area(r1, r2):
        if r1 is None or r2 is None:
            return 0
        
        x1, y1, w1, h1 = r1
        x2, y2, w2, h2 = r2
        
        maxleft = max(x1, x2)
        minright = min(x1 + w1, x2 + w2)
        maxtop = max(y1, y2)
        minbottom = min(y1 + h1, y2 + h2)
        
        if minright < maxleft:
            return 0
        
        if minbottom < maxtop:
            return 0
        
        return (minright - maxleft) * (minbottom - maxtop)

    def _m1_cardgame__default_can_drag(table, stack, card):
        return table.get_faceup(card)

    class Table(renpy.Displayable):
        
        def __init__(self, back=None, base=None, springback=0.1, rotate=0.1, can_drag=_m1_cardgame__default_can_drag, doubleclick=.33, **kwargs):
            
            renpy.Displayable.__init__(self, **kwargs)
            
            
            
            self.cards = { }
            
            
            self.stacks = [ ]
            
            
            
            self.back = renpy.easy.displayable_or_none(back)
            
            
            
            self.base = renpy.easy.displayable_or_none(base)
            
            
            
            self.springback = springback
            
            
            
            self.rotate = rotate
            
            
            
            self.can_drag = can_drag
            
            
            
            self.doubleclick = doubleclick
            
            
            self.sensitive = True
            
            
            self.last_event = CardEvent()
            
            
            self.click_card = None
            
            
            self.click_stack = None
            
            
            self.drag_cards = [ ]
            
            
            self.dragging = False
            
            
            self.click_x = 0
            self.click_y = 0
            
            
            self.st = 0
        
        
        def show(self, layer='master'):
            
            for v in self.cards.itervalues():
                v.offset = _m1_cardgame__Fixed(0, 0)
            
            ui.layer(layer)
            ui.add(self)
            ui.close()
        
        
        def hide(self, layer='master'):
            ui.layer(layer)
            ui.remove(self)
            ui.close()
        
        
        def set_sensitive(self, value):
            self.sensitive = value
        
        def get_card(self, value):
            if value not in self.cards:
                raise Exception("No card has the value %r." % value)
            
            return self.cards[value]
        
        
        def set_faceup(self, card, faceup=True):
            self.get_card(card).faceup = faceup
            renpy.redraw(self, 0)
        
        def get_faceup(self, card):
            return self.get_card(card).faceup
        
        
        def set_rotate(self, card, rotation):
            _m1_cardgame__Rotate(self.get_card(card), rotation)
            renpy.redraw(self, 0)
        
        def get_rotate(self, card):
            return self.get_card(card).rotate.rotate_limit()
        
        def add_marker(self, card, marker):
            self.get_card(card).markers.append(marker)
            renpy.redraw(self, 0)
        
        def remove_marker(self, card, marker):
            self.get_card(card).markers.remove(marker)
            renpy.redraw(self, 0)
        
        
        def card(self, value, face, back=None):
            self.cards[value] = _m1_cardgame__Card(self, value, face, back)
        
        
        def stack(self, x, y, xoff=0, yoff=0, show=1024, base=None,
                  click=False, drag=DRAG_NONE, drop=False, hidden=False):
            
            rv = _m1_cardgame__Stack(self, x, y, xoff, yoff, show, base, click, drag, drop, hidden) 
            
            self.stacks.append(rv)
            return rv
        
        
        def per_interact(self):
            renpy.redraw(self, 0)
        
        
        def render(self, width, height, st, at):
            
            self.st = st
            
            rv = renpy.Render(width, height)
            
            for s in self.stacks:
                
                if s.hidden:
                    s.rect = None
                    for c in s.cards:
                        c.rect = None
                    continue
                
                s.render_to(rv, width, height, st, at)
                
                for c in s.cards:
                    c.render_to(rv, width, height, st, at)
            
            return rv
        
        def event(self, ev, x, y, st):
            
            self.st = st
            
            if not self.sensitive:
                return
            
            grabbed = renpy.display.focus.get_grab()
            
            if (grabbed is not None) and (grabbed is not self):
                return
            
            if ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1:
                
                if self.click_stack:
                    return
                
                stack = None
                card = None
                
                for s in self.stacks:
                    
                    sx, sy, sw, sh = s.rect
                    if sx <= x and sy <= y and sx + sw > x and sy + sh > y:
                        stack = s
                    
                    
                    for c in s.cards[-s.show:]:
                        if c.rect is None:
                            continue
                        
                        cx, cy, cw, ch = c.rect
                        if cx <= x and cy <= y and cx + cw > x and cy + ch > y:
                            card = c
                            stack = c.stack
                
                if stack is None:
                    return
                
                
                renpy.display.focus.set_grab(self)
                
                
                if card is not None:
                    xoffset, yoffset = card.offset.offset()
                    if xoffset or yoffset:
                        return
                
                
                self.stacks.remove(stack)
                self.stacks.append(stack)
                
                if stack.click or stack.drag:
                    self.click_card = card
                    self.click_stack = stack
                
                if card is None or not self.can_drag(self, card.stack, card.value):
                    self.drag_cards = [ ]
                elif card.stack.drag == DRAG_CARD:
                    self.drag_cards = [ card ]
                elif card.stack.drag == DRAG_ABOVE:
                    self.drag_cards = [ ]
                    for c in card.stack.cards:
                        if c is card or self.drag_cards:
                            self.drag_cards.append(c)
                elif card.stack.drag == DRAG_STACK:
                    self.drag_cards = list(card.stack.cards)
                elif card.stack.drag == DRAG_TOP:
                    if card.stack.cards[-1] is card:
                        self.drag_cards = [ card ]
                    else:
                        self.drag_cards = [ ]
                
                for c in self.drag_cards:
                    c.offset = _m1_cardgame__Fixed(0, 0)
                
                self.click_x = x
                self.click_y = y
                self.dragging = False
                
                renpy.redraw(self, 0)
                
                raise renpy.IgnoreEvent()
            
            if ev.type == pygame.MOUSEMOTION or (ev.type == pygame.MOUSEBUTTONUP and ev.button == 1):
                
                if abs(x - self.click_x) > 7 or abs(y - self.click_y) > 7:
                    self.dragging = True
                
                dx = x - self.click_x
                dy = y - self.click_y
                
                for c in self.drag_cards:
                    xoffset, yoffset = c.offset.offset()
                    
                    cdx = dx - xoffset
                    cdy = dy - yoffset
                    
                    c.offset = _m1_cardgame__Fixed(dx, dy)
                    
                    if c.rect:
                        cx, cy, cw, ch = c.rect
                        cx += cdx
                        cy += cdy
                        c.rect = (cx, cy, cw, ch)
                
                area = 0
                dststack = None 
                dstcard = None
                
                for s in self.stacks:
                    if not s.drop:
                        continue
                    
                    for c in self.drag_cards:
                        
                        if c.stack == s:
                            continue
                        a = _m1_cardgame__rect_overlap_area(c.rect, s.rect)
                        if a >= area:
                            dststack = s
                            dstcard = None
                            area = a
                        
                        for c1 in s.cards:
                            a = _m1_cardgame__rect_overlap_area(c.rect, c1.rect)
                            if a >= area:
                                dststack = s
                                dstcard = c1
                                area = a
                
                if area == 0:
                    dststack = None
                    dstcard = None
                
                renpy.redraw(self, 0)
                
                if ev.type == pygame.MOUSEMOTION:
                    raise renpy.IgnoreEvent()
            
            if ev.type == pygame.MOUSEBUTTONUP and ev.button == 1:
                
                
                renpy.display.focus.set_grab(None)
                
                evt = None
                
                if self.dragging:
                    if dststack is not None and self.drag_cards:
                        
                        evt = CardEvent()
                        evt.type = "drag"
                        evt.table = self
                        evt.stack = self.click_stack
                        evt.card = self.click_card.value
                        evt.drag_cards = [c.value for c in self.drag_cards]
                        evt.drop_stack = dststack
                        if dstcard:
                            evt.drop_card = dstcard.value
                        evt.time = st
                
                else:
                    
                    if self.click_stack.click:                    
                        
                        evt = CardEvent()
                        evt.type = "click"
                        evt.table = self
                        evt.stack = self.click_stack
                        if self.click_card:
                            evt.card = self.click_card.value
                        else:
                            evt.card = None
                        
                        evt.time = st
                        
                        if (evt.type == self.last_event.type
                            and evt.stack == self.last_event.stack
                            and evt.card == self.last_event.card
                            and evt.time < self.last_event.time + self.doubleclick):
                            
                            evt.type = "doubleclick"
                
                if evt is not None:
                    self.last_event = evt
                
                for c in self.drag_cards:
                    c.springback()
                
                self.click_card = None
                self.click_stack = None
                self.drag_cards = [ ]
                
                if evt is not None: 
                    return evt
                else:
                    raise renpy.IgnoreEvent()


    class CardEvent(object):
        
        def __init__(self):
            self.type = None
            self.stack = None
            self.card = None
            self.drag_cards = None
            self.drop_stack = None
            self.drop_card = None
            self.time = 0



    class _m1_cardgame__Stack(object):
        
        def __init__(
            self, table,
            x, y,
            xoff, yoff,
            show, base,
            click, drag, drop,
            hidden):
            
            
            
            self.table = table
            
            
            
            self.x = x
            self.y = y
            
            
            
            self.xoff = xoff
            self.yoff = yoff
            
            
            
            
            self.show = show
            
            
            
            self.base = base
            
            
            self.click = click
            
            
            self.drag = drag
            
            
            self.drop = drop
            
            
            self.hidden = hidden
            
            
            self.cards = [ ]
            
            
            self.rect = None
        
        def insert(self, index, card):
            card = self.table.get_card(card)
            
            if card.stack:
                card.stack.cards.remove(card)
            
            card.stack = self
            self.cards.insert(index, card)
            
            self.table.stacks.remove(self)
            self.table.stacks.append(self)
            
            card.springback()
        
        def append(self, card):
            if card in self.cards:                
                self.insert(len(self.cards) - 1, card)
            else:
                self.insert(len(self.cards), card)
        
        def remove(self, card):
            card = self.table.get_card(card)            
            self.cards.remove(card)
            card.stack = None
            card.rect = None
        
        def deal(self):
            if not self.cards:
                return None
            
            card = self.cards[-1]
            self.remove(card.value)
            return card.value
        
        def shuffle(self):
            renpy.random.shuffle(self.cards)
            renpy.redraw(self.table, 0)
        
        def __len__(self):
            return len(self.cards)
        
        def __getitem__(self, idx):
            return self.cards[idx].value
        
        def __iter__(self):
            for i in self.cards:
                yield i.value
        
        def __contains__(self, item):
            return self.table.get_card(card) in self.cards
        
        def render_to(self, rv, width, height, st, at):
            
            base = self.base or self.table.base
            
            if base is None:
                return
            
            surf = renpy.render(base, width, height, st, at)
            cw, ch = surf.get_size()
            
            cx = self.x - cw / 2
            cy = self.y - ch / 2
            
            self.rect = (cx, cy, cw, ch)
            rv.blit(surf, (cx, cy))

    class _m1_cardgame__Card(object):
        
        def __init__(self, table, value, face, back):
            
            
            self.table = table
            
            
            self.value = value
            
            
            self.face = renpy.easy.displayable(face)
            
            
            
            self.back = renpy.easy.displayable_or_none(back)
            
            
            self.faceup = True
            
            
            
            self.rotate = None
            
            
            self.highlights = [ ]
            
            
            self.stack = None
            
            
            
            self.offset = _m1_cardgame__Fixed(0, 0)
            
            
            
            self.rect = None
            
            _m1_cardgame__Rotate(self, 0)
        
        
        def place(self):
            s = self.stack
            offset = max(len(s.cards) - s.show, 0)
            index = max(s.cards.index(self) - offset, 0)
            
            return (s.x + s.xoff * index, s.y + s.yoff * index)
        
        def springback(self):
            if self.rect is None:
                self.offset = _m1_cardgame__Fixed(0, 0)
            else:
                self.offset = _m1_cardgame__Springback(self)
        
        def render_to(self, rv, width, height, st, at):
            
            x, y = self.place()
            xoffset, yoffset = self.offset.offset()
            x += xoffset
            y += yoffset
            
            if self.faceup:
                d = self.face
            else:
                d = self.back or self.table.back
            
            
            
            if self.highlights:
                d = Fixed(* ([d] + [renpy.easy.displayable(i) for i in self.highlights]))
            
            r = self.rotate.rotate()
            if r:
                d = RotoZoom(r, r, 0, 1, 1, 0)(d)
            
            surf = renpy.render(d, width, height, st, at)
            w, h = surf.get_size()
            
            x -= w / 2
            y -= h / 2
            
            self.rect = (x, y, w, h)
            
            rv.blit(surf, (x, y))
        
        def __repr__(self):
            return "<__Card %r>" % self.value


    class _m1_cardgame__Springback(object):
        
        def __init__(self, card):
            self.card = card
            self.table = table = card.table
            
            self.start = table.st
            
            cx, cy, cw, ch = self.card.rect
            x = cx + cw / 2
            y = cy + ch / 2
            
            self.startx = x
            self.starty = y
        
        def offset(self):
            
            t = (self.table.st - self.start) / self.table.springback
            t = min(t, 1.0)
            
            if t < 1.0:
                renpy.redraw(self.table, 0)
            
            px, py = self.card.place() 
            
            return int((self.startx - px) * (1.0 - t)), int((self.starty - py) * (1.0 - t))


    class _m1_cardgame__Fixed(object):
        def __init__(self, x, y):
            self.x = x
            self.y = y
        
        def offset(self):
            return self.x, self.y


    class _m1_cardgame__Rotate(object):
        def __init__(self, card, amount):
            
            self.table = table = card.table
            self.start = table.st
            
            if card.rotate is None:
                self.start_rotate = amount
            else:
                self.start_rotate = card.rotate.rotate()
            
            self.end_rotate = amount
            
            card.rotate = self
        
        
        def rotate(self):
            
            if self.start_rotate == self.end_rotate:
                return self.start_rotate
            
            t = (self.table.st - self.start) / self.table.springback
            t = min(t, 1.0)
            
            if t < 1.0:
                renpy.redraw(self.table, 0)
            
            return self.start_rotate + (self.end_rotate - self.start_rotate) * t
        
        def rotate_limit(self):
            return self.end_rotate
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
