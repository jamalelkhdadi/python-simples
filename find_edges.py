from PIL import Image, ImageFilter


before = Image.open("ex.png")
edges  = before.filter(ImageFilter.FIND_EDGES)
blur   = before.filter(ImageFilter.BoxBlur(10))

blur.save('out.png')
edges.save('out2.png')
