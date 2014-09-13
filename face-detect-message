# This example modified based on examples by Matt Richardson and Shawn Wallace "Getting Started with Raspberry Pi"


from SimpleCV import Camera,Display, DrawingLayer, Color
from time import sleep

myCamera = Camera(prop_set={'width':320,'height':240})
myDisplay = Display(resolution=(320,240))
myDrawingLayer = DrawingLayer((320,240))
while not myDisplay.isDone():
    frame = myCamera.getImage()
    faces = frame.findHaarFeatures('face')
    if faces:
        for face in faces:
            print "Face at: " + str(face.coordinates())
            myDrawingLayer.setFontSize(80)
            myDrawingLayer.rectangle((18,148),(250,60),filled=True)
            myDrawingLayer.text("Toadman",(20,150),color=Color.GREEN)
            frame.addDrawingLayer(myDrawingLayer)
            frame.applyLayers()
            frame.save(myDisplay)

    else:
        print "No faces detected."
    frame.save(myDisplay)
    sleep(.1)
