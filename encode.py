from PIL import Image
import  cv2

import dependancies as dep
encodeEnc = dep.textInImageDependancies()

class encode:
    def encodeTextInImage(self):
        img = input("::Enter Cover Images full location::\n> ")
        image = Image.open(img, 'r')

        data = input("::Enter your secrect data::\n> ")
        if (len(data) == 0):
            raise ValueError('Data is empty')

        newimg = image.copy()
        encodeEnc.encode_enc(newimg, data)
        # encode_enc(newimg, data)

        new_img_name = input("Enter the name of new image(with extension) : ")
        newimg.save(new_img_name, str(new_img_name.split(".")[1].upper()))


    def encodeImageInImage(self):
        cover_img = cv2.imread(input("::Enter cover images full location::\n> "))
        hide_img = cv2.imread(input("::Enter secret images full location::\n> "))

        for i in range(hide_img.shape[0]):
            for j in range(hide_img.shape[1]):
                for l in range(3):
                    v1 = format(cover_img[i][j][l], '08b')
                    v2 = format(hide_img[i][j][l], '08b')
                    v3 = v1[:4] + v2[:4]

                    cover_img[i][j][l] = int(v3, 2)
        cv2.imwrite(input("::Enter Your stegan saving path with image name::\n> "))
        print(":)Happy Hacking:)")










