#coding=utf-8
Room_1 = "The star's hydrogen hiccups blot your vision-"
List_1 = ['look away','avert eyes','shut eyes','close eyes','rub eyes','look down','look up']
Room_2 = "an abrupt desire: wandering the flaming hedges \n despite the burn, the melting ship. \n It’s on autopilot, step away, \n"
List_2 = ['step away','walk away','check controls','look out window']
Room_3 = "peculiar leathery sky \n nearby, someone’s unbuttoning the heat bales \n north from here, bright startle in the heat."
List_3 = ['steer north','look north','go north','sit down','look out window','close window','close eyes','shut eyes']
Room_4 = "Even lightweight travelers become transient, \n suffocating in the want of coffee and log fire, \n thin lake breeze, unfiltered speech on a dank bar’s stool. \n \n A silver tumbler glass sits empty on the dashboard."
List_4 = ['take glass','fill glass','walk to kitchen','walk away','leave room','leave']
Room_5 = "There is a water tank behind the closed door."
List_5 = ['fill glass','pour water','open door','enter door','open closed door','get water']
Room_6 = "You fill the glass to the brim and the ripples cross and cross and cross."
List_6 = ['go north','go south','go east','go west','look out window']
Room_7 = "The sequins of a galaxy, economically thin, frame \n other stars budding, tiny capillary pulses twisting into life. \n \n Your heart is beating like a scratched record. The radar’s picking up something down West Sphere."
List_7 = ['turn west','go west','steer west','head west','go west']
Room_8 = "A scratch on the sky is the recent dust of the red dwarf \n we wished on in a tiny day—the brief, exciting fold \n of time when we wanted more. \n \n Your throat is tight and dry..."
List_8 = ['drink water','get water','pick up water','take water','drink']
Room_9 = "The water, lukewarm, is not enough. Why can't it, why can't anything be cold? These technetiums are unbearable. Unbearable and unavoidable this far west."
List_9 = ['drink water','go east','go west','go north','go south','turn away','sit down']
Room_10 = "You were late to your boat that day \n rising without me like a ghostly alarm, unapologetic \n smoke clouding my eyes and the sky and the sun. \n \n This heat, why is it so hot..."
List_10 = ['look outside','look out window','drink water','go east','go west','go north','go south','turn away','sit down']
Room_11 = "How lucky I am alone, a small thing clipped together \n in a storm of static appearing still, completely inverted, \n an empty hourglass, the radio wave out of context."
Room_12 = "The technetium passes slowly out of sight. The heat remains- \n your eyes, thick and red with veins."
Room_13 = "end"
prompt = ">"

print Room_1
while True:
	command_1 = raw_input(prompt)
	if command_1 in List_1:
		print(Room_2)
	else:
		command_1 = raw_input(prompt)
		print("What does that mean?") 
		break


command_2 = raw_input(prompt)
if command_2 in List_2:
	print(Room_3)
else:
	print("What does that mean?")

command_3 = raw_input(prompt)
if command_3 in List_3:
	print(Room_4)
else:
	print("What does that mean?")

command_4 = raw_input(prompt)
if command_4 in List_4:
	print(Room_5)
else:
	print("What does that mean?")

command_5 = raw_input(prompt)
if command_5 in List_5:
	print(Room_6)
else:
	print("What does that mean?")

command_6 = raw_input(prompt)
if command_6 in List_6:
	print(Room_7)
else:
	print("What does that mean?")

command_7 = raw_input(prompt)
if command_7 in List_7:
	print(Room_8)
else:
	print("What does that mean?")

	command_8 = raw_input(prompt)
if command_8 in List_8:
	print(Room_9)
else:
	print("What does that mean?")

	command_9 = raw_input(prompt)
if command_9 in List_9:
	print(Room_10)
else:
	print("What does that mean?")

print Room_11 
time.sleep(10)
print Room_12 
time.sleep(10)
print Room_13


