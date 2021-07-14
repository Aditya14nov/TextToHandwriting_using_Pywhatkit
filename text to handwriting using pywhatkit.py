import pywhatkit as kit
import cv2

text = input("Enter your text here: ")
kit.text_to_handwriting(text, save_to="handwriting.png")
img = cv2.imread("handwriting.png")
h,w = img.shape[:2]
print("Height = {}, width = {}".format(h,w))
cv2.namedWindow("Text to Handwriting", cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty("Text to Handwriting", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

#img_stretch = cv2.resize(img, (780, 540),interpolation=cv2.INTER_NEAREST)
cv2.imshow("Text to Handwriting", img)
key = cv2.waitKey(0)
if (key==2):
    cv2.destroyAllWindows()
