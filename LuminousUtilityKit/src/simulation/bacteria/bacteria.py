import pygame
import math

class Bacteria:
    def __init__(self, x, y, color, r, vx, vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.color = color
        self.radius = r

    def attract(self, other_bacteria):
        distance = math.hypot(self.x - other_bacteria.x, self.y - other_bacteria.y)
        force = 10 / distance
        force_repulsion = -1 / distance

        alpha = math.atan2(other_bacteria.y - self.y, other_bacteria.x - self.x)

        def reflect_velocity(b):
            if b.x <= 0 or b.x >= 1000:
                b.vx = -b.vx
            if b.y <= 0 or b.y >= 800:
                b.vy = -b.vy

        reflect_velocity(self)
        reflect_velocity(other_bacteria)

        def update_velocity_and_position(b1, b2, force):
            b1.vx += force * math.cos(alpha)
            b1.vy += force * math.sin(alpha)
            b1.x += b1.vx
            b1.y += b1.vy
            b2.vx -= force * math.cos(alpha)
            b2.vy -= force * math.sin(alpha)
            b2.x += b2.vx
            b2.y += b2.vy

        if distance > self.radius + other_bacteria.radius:
            update_velocity_and_position(self, other_bacteria, force)
        elif distance < self.radius + other_bacteria.radius:
            update_velocity_and_position(self, other_bacteria, force_repulsion)
        else:
            print('Exception!')
            print('x coordinate', self.x, other_bacteria.x)
            print('y coordinate', self.y, other_bacteria.y)

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)
