#!/usr/bin/env python

import arcade

# Resolution of the screen
WIDTH = 500
HEIGHT = 500

# Gravity constsnt
GRAVITY = 0.35



# This is a class that specifies objects of type "Ball"
class Ball:
    def __init__(self, posx, posy, velx, vely, radius, bounciness):     #this is called, when you set up an object with Ball(...)
        self.x = posx       #this creates a member variable called "x" and initializes it with posx
        self.y = posy       #this creates a member variable called "y" and initializes it with posy
        self.vel_x = velx   #you could store other interesting Ball properties like color, too
        self.vel_y = vely
        self.radius = radius
        self.bounciness = bounciness
    
    def drawBall(self,color):
        arcade.draw_circle_filled(self.x, self.y,self.radius,color)
    
    def updateBall(self):
        # Modify ball position based on velocity
        self.x += self.vel_x
        self.y += self.vel_y
        
        self.vel_y -= GRAVITY
        
        # Bounce off of left/right side of screen
        if self.x < self.radius and self.vel_x < 0:
            self.vel_x *= -self.radius
        elif self.x > WIDTH - self.radius and self.vel_x > 0:
            self.vel_x *= -self.bounciness
        
        # Do something different if we hit the bottom
        if self.y < self.radius and self.vel_y < 0:
            if self.vel_y * -1 > GRAVITY * 15:
                self.vel_y *= -self.bounciness
            else:
                self.vel_y *= -self.bounciness / 2



# This is our player class
class Player:
    """ Class to represent a player circle on the screen """
    
    def __init__(self, x, y, radius):
        """ Initialize our rectangle variables """
        # Position
        self.x = x
        self.y = y
        # Velocity
        self.vel_x = 0
        self.vel_y = 0
        self.radius = radius
    
    def drawPlayer(self):
        """ Draw our player circle """
        arcade.draw_circle_outline(self.x, self.y, self.radius, arcade.color.BLACK)
        arcade.draw_text("Feri", self.x-self.radius*0.75, self.y-self.radius*0.27, arcade.color.BLACK, 10)
    
    def updatePlayer(self):
        """ Move our player """
        
        # Move left or right
        self.x += self.vel_x
        self.y += self.vel_y
        
        # If we are leaving the sceen, reset position to border
        if self.x < self.radius:
            self.x = self.radius
        if self.x > WIDTH - self.radius:
            self.x = WIDTH - self.radius
        if self.y < self.radius:
            self.y = self.radius
        if self.y > HEIGHT - self.radius:
            self.y = HEIGHT - self.radius


#Very simple (box) collision test between Player p and Ball b. Brings ball to a halt.
def collide(p, b):
    if abs(b.x - p.x) < b.radius + p.radius and abs(b.y - p.y) < b.radius + p.radius:
        b.vel_x = 0
        b.vel_y = 0



#This is our main class. It inherits properties from the "arcade.Window" class
class MyGame(arcade.Window):
    """
        Main application class.
        """
    def __init__(self, width, height):
        super().__init__(width, height, title="Bouncy bounce")
        arcade.set_background_color(arcade.color.WHITE)
        self.player = None
        self.ball = None
    
    def setup(self):
        """ Set up the game and initialize the variables. """
        x = WIDTH / 2
        y = HEIGHT / 2
        self.player = Player(x, y, 15) #make player object with radius 15
        radius = 10
        bounciness = 0.85
        x = 25
        y = HEIGHT-25
        self.ball = Ball(x,y,2,0,radius,bounciness) #make ball object
    
    #This is called every frame
    def update(self, dt):
        """ Move everything """
        self.player.updatePlayer()
        self.ball.updateBall()
        #do something if player touches the ball
        collide(self.player,self.ball)
    
    #This is called every frame
    def on_draw(self):
        """
        Render the screen.
        """
        arcade.start_render()
        self.player.drawPlayer()
        self.ball.drawBall(arcade.color.BLUE)

    #This is called every time a key is pressed
    def on_key_press(self, key, modifiers):
        """
            Called whenever a key is pressed.
            """
        STEP = 4
        if key == arcade.key.LEFT:
            self.player.vel_x = -STEP
        elif key == arcade.key.RIGHT:
            self.player.vel_x = STEP
        elif key == arcade.key.UP:
            self.player.vel_y = STEP
        elif key == arcade.key.DOWN:
            self.player.vel_y = -STEP


    #This is called every time a key is released
    def on_key_release(self, key, modifiers):
        """
            Called when the user releases a key.
            """
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player.vel_x = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.player.vel_y = 0




def main():
    window = MyGame(WIDTH, HEIGHT) #this calls the _init_ function
    window.setup()
    arcade.run() #this will call the draw and update functions of the MyGame class




if __name__ == "__main__":
    main()




