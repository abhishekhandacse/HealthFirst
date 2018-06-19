# create a splash screen, 80% of display screen size, centered,
# displaying a GIF image with needed info, disappearing after 5 seconds
import tkinter as tk
root = tk.Tk()
# show no frame
root.overrideredirect(True)
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.geometry('%dx%d+%d+%d' % (width*0.8/2, height*0.8/2, width*0.1, height*0.1))
# take a .jpg picture you like, add text with a program like PhotoFiltre
# (free from http://www.photofiltre.com) and save as a .gif image file
image_file = "LakeSplash.gif"
#assert os.path.exists(image_file)
# use Tkinter's PhotoImage for .gif files
image = tk.PhotoImage(file=image_file)
canvas = tk.Canvas(root, height=height*0.9, width=width*0.9, bg="white")
canvas.create_image(width*0.8/4, height*0.8/4, image=image)
canvas.pack()
# show the splash screen for 5000 milliseconds then destroy
root.after(5000, root.destroy)
root.mainloop()
# your console program can start here ...
print ("How did you like m4y informative splash screen?")