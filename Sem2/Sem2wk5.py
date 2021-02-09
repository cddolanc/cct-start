from PIL import Image
# mac = Image.open('images/example.jpg')
# # Note this is a specialized file type from PIL (pillow)
# print(type(mac))
# # mac.show()

# # (width, height)
# print(mac.size)
# print(mac.filename)
# print(mac.format_description)

# mac_new = mac.crop((0,0,100,100))
# print(mac_new)

# pencils = Image.open("images/pencils.jpg")

# print(pencils.size)
# #  pencils.show()


# pencils.size

# # Start at top corner (0,0)
# x = 0
# y = 0
# # Grab about 10% in y direction , and about 30% in x direction
# w = 1950/3
# h = 1300/10

# pencils_new = pencils.crop((x,y,w,h))
# # pencils.show()
# print(pencils_new.size)
# pencils_new.save('pencils_new.png')




# computer = mac.crop((x,y,w,h))

# mac.paste(im=computer,box=(0,0))

# mac.show()

# mac.paste(im=computer,box=(796,0))

# mac.save()






# mac.size

# h,w = mac.size

# new_h = int(h/3)
# new_w = int(w/3)

# # Note this is not permanent change
# # for permanent change, do a reassignment
# # e.g. mac = mac.resize((100,100))
# mac.resize((new_h,new_w))



red = Image.open('images/red_color.jpg')
red.show()
blue = Image.open('images/purple.png')
# blue.show()
red.putalpha(128)
# red.show()
blue.putalpha(128)
# blue.show()
blue.paste(red,box=(0,0),mask=red)

# Get back an image that is more purple.
# blue.show()

blue.save('new_purple.png')