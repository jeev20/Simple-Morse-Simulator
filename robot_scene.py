from morse.builder import * 

#importing robot
atrv = ATRV()

# Adding motion
motion = MotionVW()
motion.translate (z=0.3)
atrv.append(motion)   # attributes to robot

# Adding postion 
pose =Pose()
pose.translate(z=0.83)
atrv.append(pose)


#Keyboard controls
keyboard = Keyboard()
keyboard.properties(Speed=5.0)
atrv.append(keyboard)
keyboard.properties(ControlType = 'Position')


#Camera
semanticL = SemanticCamera()
semanticL.translate(x=0.2, y=0.3, z=0.9)
atrv.append(semanticL)
semanticL.properties(cam_width = 600, cam_height = 600, Vertical_Flip = True)

semanticR = SemanticCamera()
semanticR.translate(x=0.2, y=-0.3, z=0.9)
atrv.append(semanticR)
semanticR.properties(cam_width = 600, cam_height = 600, Vertical_Flip = True)

#position
pose.add_stream("socket")
pose.add_service("socket")

#Motion
motion.add_service("socket")


#Enviornment 
env =Environment("outdoors")
env.set_camera_location([1.0470, 0, 0.7854])
env.set_camera_rotation([1.0470, 0, 0.7854])
env.select_display_camera(semanticL)
